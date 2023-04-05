from fastapi import Request
from fastapi import Response
from starlette.middleware.base import BaseHTTPMiddleware
import json
import requests


class IPCheck(BaseHTTPMiddleware):
    def __init__(self, app):
        super().__init__(app)

    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)
        result = requests.get("https://ip.useragentinfo.com/json", params={
            "ip": request.client.host
        }).json()
        raw = b""
        async for i in response.body_iterator:
            raw += i
        if result["short_name"] != "" and result["short_name"] != "CN":
            if request.scope["path"] == "/af":
                data = json.loads(raw)
                data["items"] = []
            else:
                data = {"detail": "Your region is not allowed to visit temporarily"}
                response.status_code = 403
            raw = json.dumps(data).encode()
        headers = dict(response.headers)
        headers["content-length"] = str(len(raw))
        return Response(raw, response.status_code, headers, response.media_type)
