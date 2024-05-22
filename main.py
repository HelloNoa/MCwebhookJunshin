from fastapi import FastAPI
import os
app = FastAPI()
# /home/opc

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/MFwwDQYJKoZIhvcNAQEBBQADSwAwSAJBAJxauSJISd6+C88OzRfJtX44ZArNGp7R6untVzaLMjL4MHglWSXeFfC/6IaBNXuuaMIah0B69nPDDnRwmD7ED4sCAwEAAQ==")
async def root():
    os.system('./test.sh')
    return {"message": "server1 restart!"}

@app.get("/start")
async def start():
    os.system('./start.sh')
    return {"message": "server2 restart!"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
