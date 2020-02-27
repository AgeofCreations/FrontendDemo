from aiohttp import web
from views import index_page


def init_server():
    app = web.Application()
    app.add_routes(
        [
            web.get(r"/", index_page),
            web.static("/public", "static")
        ]
    )
    return app


if __name__ == "__main__":
    app = init_server()
    web.run_app(app, host='0.0.0.0', port=8080)
