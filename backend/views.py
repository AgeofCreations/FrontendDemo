from aiohttp import web


def index_page(input_request):
    return web.FileResponse("./static/index.html")