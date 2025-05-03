import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))


import pandas as pd
from sqlalchemy.orm import Session
from src.db.database import SessionLocal
from src.db.models import UserEntry

import os

SAVE_PATH = "data/raw/job_applicants_online_learning.csv"

def fetch_new_records_and_clear_db():
    db: Session = SessionLocal()

    try:
        applicants = db.query(UserEntry).all()

        if not applicants:
            print("⚠️ No new applicants to fetch.")
            return

        records = []
        for applicant in applicants:
            record = {column.name: getattr(applicant, column.name) for column in UserEntry.__table__.columns}
            records.append(record)

        df = pd.DataFrame(records)

        os.makedirs(os.path.dirname(SAVE_PATH), exist_ok=True)
        df.to_csv(SAVE_PATH, index=False)
        print(f"✅ Saved {len(df)} new applicants to {SAVE_PATH}")

        # Delete all fetched records
        db.query(UserEntry).delete()
        db.commit()
        print(f"✅ Cleared {len(df)} records from UserEntry table")

    except Exception as e:
        print(f"❌ Error during fetch and clear: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    fetch_new_records_and_clear_db()
