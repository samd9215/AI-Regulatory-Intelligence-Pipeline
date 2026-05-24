from fastapi import APIRouter
from app.db.database import SessionLocal
from app.db.models import Regulation
from app.services.regulatory_service import ingest_regulations

router = APIRouter()

@router.get("/")
def home():
    return {"message": "RegPass AI API running"}

@router.post("/ingest")
def ingest():
    ingest_regulations()
    return {"message": "Regulations ingested"}

@router.get("/regulations")
def get_regulations():
    db = SessionLocal()

    regulations = db.query(Regulation).all()

    results = []

    for reg in regulations:
        results.append({
            "id": reg.id,
            "title": reg.title,
            "summary": reg.summary,
            "risk_level": reg.risk_level
        })

    db.close()

    return results