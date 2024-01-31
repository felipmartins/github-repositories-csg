from fastapi import FastAPI
from src.controllers.user_controller import router as user_router

app = FastAPI()

app.include_router(user_router, tags=["users"])


@app.get("/health")
async def sanity_check():
    return {"message": "Hello World"}
