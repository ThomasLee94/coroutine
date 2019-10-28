from req_handler import foo_handle
from aiohttp import web
from flask_api import status

# Coroutine 1
app = web.Application()
app.add_routes([web.get('/foo', foo_handle)])

if __name__ == '__main__':
    web.run_app(app)
