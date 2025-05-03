from contextlib import asynccontextmanager
from fastapi import FastAPI
from src.routes.predict import router as predict_router
from src.routes.submit import router as submit_router
from src.db.database import create_db_and_tables

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("✅ Starting up... creating DB if needed")
    create_db_and_tables()
    yield
    print("✅ Shutting down (if needed)")

# App Instance
app = FastAPI(lifespan=lifespan)

# Register routers
app.include_router(predict_router, prefix="/api")
app.include_router(submit_router, prefix="/api")

@app.get("/info")
def info():
    return {"model_version": "v1.0.0", "author": "Jacob MacInnis", "framework": "TensorFlow"}

