from req_handler import bar_handle
from aiohttp import web

# Coroutine 
app = web.Application()
app.add_routes([web.get('/bar', bar_handle)])

if __name__ == '__main__':
    web.run_app(app)
