from app.ingestion.scraper import fetch_fca_updates
from app.llm.summarizer import summarize_regulation
from app.db.models import Regulation
from app.db.database import SessionLocal

def ingest_regulations():
    db = SessionLocal()

    updates = fetch_fca_updates()

    for update in updates:
        summary = summarize_regulation(update["content"])

        regulation = Regulation(
            title=update["title"],
            content=update["content"],
            summary=summary,
            risk_level="Medium"
        )

        db.add(regulation)

    db.commit()
    db.close()