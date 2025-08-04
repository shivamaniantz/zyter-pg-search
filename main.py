# server.py
from fastapi import FastAPI
from contextlib import asynccontextmanager
from member_module.member_routes import router as member_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    print("Server starting up...")

    yield

    # Shutdown
    print("Server shutting down...")

app = FastAPI(
    title="Member API",
    description="API for managing members",
    version="1.0.0",
    lifespan=lifespan
)

# Include member routes
app.include_router(member_router, prefix="/api/v1")

@app.get("/")
async def root():
    return {"message": "Member API is running"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}