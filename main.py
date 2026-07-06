from fastapi import FastAPI

app = FastAPI(title="TestApp")

@app.get('/items')
async def list_items():
    return []

@app.get('/test')
async def get_test():
    return {"message": "test"}
