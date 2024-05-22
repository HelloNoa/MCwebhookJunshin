from fastapi import FastAPI
import os
import asyncio
import subprocess

app = FastAPI()


# /home/opc
async def server1():
    script_name = "start.sh"
    subprocess.run(f"sh {script_name}", shell=True)
    # os.system('./start.sh')
async def say1(arg):
    script_name = "test.sh"
    subprocess.run(f"sh {script_name} '{arg}'", shell=True)
    # os.system(f'./test.sh "{arg}"')


async def server2():
    os.system('./start2.sh')


@app.get("/")
async def HealthCheck():
    return {"message": "Hello World"}


@app.get(
    "/MFwwDQYJKoZIhvcNAQEBBQADSwAwSAJBAJxauSJISd6+C88OzRfJtX44ZArNGp7R6untVzaLMjL4MHglWSXeFfC/6IaBNXuuaMIah0B69nPDDnRwmD7ED4sCAwEAAQ==")
def restartServer1():
    asyncio.run(server1())
    return {"message": "server1 restart!"}

@app.get(
    "/say/{arg}")
def sayServer1(arg: str):
    asyncio.run(say1(arg))
    return {"message": "say server1"}


@app.get(
    "/MFwwDQYJKoZIhvcNAQEBBQADSwAwSAJBAMXloF6aFigQ6QnDcnox9CsdcCVvCctsRYEtYnN+s0tVrXMzuthCm5y7wGHLrhOD3BpJt6ql4Tx4fkBfJecq378CAwEAAQ==")
def restartServer2():
    asyncio.run(server2())
    return {"message": "server2 restart!"}

# @app.get("/hello/{name}")
# async def say_hello(name: str):
#     return {"message": f"Hello {name}"}
