import asyncio
from flask import Flask
from flask_api import status

asyincio.run(main())
server = Flask(__name__)

# Coroutine 1
@server.route("/foo")
async def run():
    await asyncio.sleep(5)
    print("I am foo")
    return status.HTTP_200_ok

    
