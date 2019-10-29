from aiohttp import web

# Handlers


async def foo_handle(request):
    return web.Response(text="I am foo")


async def bar_handle(request):
    # data = await request.query.get('foo')
    data = await foo_handle(request)
    print(data)
    if data:
        return web.Response(text=data)

# web app instance
app = web.Application()
app.router.add_get('/foo', foo_handle)
app.router.add_get('/bar', bar_handle)

# run app
web.run_app(app)

# bar?foo=bar
