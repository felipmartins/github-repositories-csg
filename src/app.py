from fastapi import FastAPI


app = FastAPI()


@app.get("/health")
async def sanity_check():
    return {"message": "Hello World"}
