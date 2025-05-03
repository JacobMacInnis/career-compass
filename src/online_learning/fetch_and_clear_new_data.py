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

        new_df = pd.DataFrame(records)

        os.makedirs(os.path.dirname(SAVE_PATH), exist_ok=True)

        if os.path.exists(SAVE_PATH):
            # If the file exists, load it and append
            existing_df = pd.read_csv(SAVE_PATH)
            combined_df = pd.concat([existing_df, new_df], ignore_index=True)
            print(f"✅ Appending {len(new_df)} new records to existing {len(existing_df)} records")
        else:
            # If it doesn't exist, just use the new data
            combined_df = new_df
            print(f"✅ No existing file found, saving {len(new_df)} new records")

        combined_df.to_csv(SAVE_PATH, index=False)
        print(f"✅ Total saved records: {len(combined_df)}")

        # Delete all fetched records
        db.query(UserEntry).delete()
        db.commit()
        print(f"✅ Cleared {len(new_df)} records from UserEntry table")

    except Exception as e:
        print(f"❌ Error during fetch and clear: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    fetch_new_records_and_clear_db()
