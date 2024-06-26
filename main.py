from fastapi import FastAPI
import os
import asyncio
import libtmux
svr = libtmux.Server()

app = FastAPI()


# /home/opc
async def server1():
    ss = svr.sessions.get(session_name="server")
    window = ss.active_window
    pane = window.panes[0]
    pane.send_keys('cd /home/opc')
    pane.send_keys('sh log.sh')
    pane.send_keys('sh run.sh')

async def say1(arg):
    ss = svr.sessions.get(session_name="server")
    window = ss.active_window
    pane = window.panes[0]
    pane.send_keys('cd /home/opc')
    pane.send_keys(arg)
    # session_name = "server"
    # process = await asyncio.create_subprocess_exec("tmux", "switch-client", "-t", session_name)
    # await process.wait()

    # script_name = "test.sh"
    # process = await asyncio.create_subprocess_exec("sh", script_name, arg)
    # await process.wait()

async def server2():
    ss = svr.sessions.get(session_name="server")
    window = ss.active_window
    pane = window.panes[0]
    pane.send_keys('cd /home/opc')
    pane.send_keys('sh log2.sh')
    pane.send_keys('sh run2.sh')
    # script_name = "start2.sh"
    # process = await asyncio.create_subprocess_exec("sh", script_name)
    # await process.wait()


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
