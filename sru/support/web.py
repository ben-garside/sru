from aiohttp import web

def Response(body=None, status=200, reason=None, text=None, headers=None, content_type=None, charset=None):
    return web.Response(body=body, status=status, reason=reason, text=text, headers=headers, content_type=content_type, charset=charset)