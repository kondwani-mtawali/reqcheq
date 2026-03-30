from fastapi import FastAPI

app = FastAPI()


@app.get("/") # <-- Endpoint(GET Method)
async def root():
    return {"message": "Server Running"} 