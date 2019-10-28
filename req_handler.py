import asyncio

async def foo_handle(request):
        return web.Response(text="I am foo")

async def bar_handle(request):
    return web.Response(text="I am bar")



