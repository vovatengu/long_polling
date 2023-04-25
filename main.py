import asyncio

from fastapi import FastAPI , HTTPException

app = FastAPI()

event = asyncio.Event()

@app.get("/new_invoice/")
async def new_invoice():
    try:
        await asyncio.wait_for(event.wait(), 30)
    except asyncio.TimeoutError:
        raise HTTPException(status_code=404, detail="Timeout")
    event.clear()
    return {"succeed": True}

@app.get("/pay/")
async def pay():
    event.set()
    return {"succeed": True}