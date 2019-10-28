from aiohttp import web

routes = web.RouteTableDef()


@routes.get('/foo')
async def foo_handle(request):
    return web.Response(text="I am foo")


@routes.get('/bar')
async def bar_handle(request):
    output = await web.get('foo', foo_handle)
    if output:
        return web.Response(text="I am bar")

app.router.add_routes(routes)
