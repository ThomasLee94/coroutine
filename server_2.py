from req_handler import bar_handle
from aiohttp import web

routes = web.RouteTableDef()
app = web.Application()

# Coroutine 1
@routes.get('/bar')
def main():
    app.add_routes([web.get('/bar', bar_handle)])


if __name__ == '__main__':
    web.run_app(routes)
