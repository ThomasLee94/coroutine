from aiohttp import web

# Handlers


async def foo_handle(request):
    return web.Response(text="I am foo")


async def bar_handle(request):
    output = await web.get('foo', foo_handle)
    if output:
        return web.Response(text="I am bar")

# web app instance
app = web.Application()
app.router.add_get('/foo', foo_handle)
app.router.add_get('/bar', bar_handle)

# run app
web.run_app(app)
