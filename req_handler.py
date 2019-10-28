from aiohttp import web

async def foo_handle(request):
        return web.Response(text="I am foo")

async def bar_handle(request):
    await output = web.get('foo', foo_handle)
    if output:
        return web.Response(text="I am bar")
