from fastapi import FastAPI
from app.api.routes import router
from app.db.database import engine
from app.db.models import Base

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Regulatory Intelligence API"
)

app.include_router(router)