from fastapi import FastAPI
import os
import asyncio

app = FastAPI()
# /home/opc
async def server1():
    os.system('./start.sh')
async def server2():
    os.system('./start2.sh')

@app.get("/")
async def HealthCheck():
    return {"message": "Hello World"}

@app.get("/MFwwDQYJKoZIhvcNAQEBBQADSwAwSAJBAMXloF6aFigQ6QnDcnox9CsdcCVvCctsRYEtYnN+s0tVrXMzuthCm5y7wGHLrhOD3BpJt6ql4Tx4fkBfJecq378CAwEAAQ==")
async def restartServer2():
    asyncio.run(server2())
    return {"message": "server1 restart!"}

@app.get("/MFwwDQYJKoZIhvcNAQEBBQADSwAwSAJBAJxauSJISd6+C88OzRfJtX44ZArNGp7R6untVzaLMjL4MHglWSXeFfC/6IaBNXuuaMIah0B69nPDDnRwmD7ED4sCAwEAAQ==")
def restartServer1():
    asyncio.run(server1())
    return {"message": "server2 restart!"}



# @app.get("/hello/{name}")
# async def say_hello(name: str):
#     return {"message": f"Hello {name}"}
