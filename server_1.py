from req_handler import foo_handle
from aiohttp import web
from flask_api import status

asyincio.run(main())
server = Flask(__name__)

# Coroutine 1
@server.route("/foo")
async def run():
    await asyncio.sleep(5)
    print("I am foo")
    return status.HTTP_200_ok

    
