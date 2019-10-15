import asyncio
from flask import Flask

server = Flask(__name__)

# Coroutine 2
@server.route("/bar")
async def run():
    await output = requests.get("/bar")
    if output:
       return "I am bar" 
