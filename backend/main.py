"""
main.py: Application entry point that creates the application
"""

from fastapi import FastAPI
from router import router as process_router

app = FastAPI() # App initialization
app.include_router(process_router) # Moves data to the right api endopoint

# @app.get("/") # <-- Endpoint(GET Method)
# async def root():
#     return {"message": "Server Running"} 