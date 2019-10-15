import asyncio
from flask import Flask

# Coroutine 2
@server.route("/bar")
async def run():
    await output = requests.get("/bar")
    if output:
       return "I am bar" 
