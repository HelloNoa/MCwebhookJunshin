from fastapi import FastAPI
import os
import asyncio

app = FastAPI()
# /home/opc
async def server1():
    os.system('./start.sh')

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/start2")
async def root():
    os.system('./test.sh')
    return {"message": "server1 restart!"}

@app.get("/MFwwDQYJKoZIhvcNAQEBBQADSwAwSAJBAJxauSJISd6+C88OzRfJtX44ZArNGp7R6untVzaLMjL4MHglWSXeFfC/6IaBNXuuaMIah0B69nPDDnRwmD7ED4sCAwEAAQ==")
def start():
    asyncio.run(server1())
    return {"message": "server2 restart!"}



@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
