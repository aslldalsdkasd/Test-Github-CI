from fastapi import FastAPI
app = FastAPI()


@app.get("/")
async def root():
    """Приветственная страница"""
    return {"message": "Hello World"}
