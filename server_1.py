from req_handler import foo_handle
from aiohttp import web

routes = web.RouteTableDef()
app = web.Application()

# Coroutine 1
@routes.get('/foo')
def main():
    app.add_routes([web.get('/foo', foo_handle)])


if __name__ == '__main__':
    web.run_app(routes)
