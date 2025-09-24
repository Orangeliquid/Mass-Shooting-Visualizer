import pandas as pd

from app.database import SessionLocal
from app.models.db_entry import IncidentEntry


def create_incident_entries(df: pd.DataFrame):
    with SessionLocal() as db:
        entries = []
        for _, row in df.iterrows():
            entry = IncidentEntry(
                date=row["date"],
                killed=row["killed"],
                wounded=row["wounded"],
                city=row["city"],
                state=row["state"],
                names=row["names"],
                sources=row["sources"],
                suspect_status=row["suspect_status"],
                suspect_keyword=row["suspect_keyword"],
                year=row["year"],
                month=row["month"],
                day=row["day"],
            )

            db.add(entry)
            entries.append(entry)

        db.commit()
        for entry in entries:
            db.refresh(entry)

        return entries


def get_entries_by_year(year: int):
    with SessionLocal() as db:
        entries = (
            db.query(IncidentEntry)
            .filter(IncidentEntry.year == year)
            .all()
        )

        return entries


def get_entries_by_year_range(start_year: int, end_year: int):
    with SessionLocal() as db:
        entries = (
            db.query(IncidentEntry)
            .filter(IncidentEntry.year.between(start_year, end_year))
            .all()
        )

        return entries


def get_entries_by_column(column: str, value: int = None):
    if column not in IncidentEntry.__table__.column.keys():
        raise ValueError(f"Invalid column: {column}")

    with SessionLocal() as db:
        query = db.query(IncidentEntry)
        if value is not None:
            query = query.filter(getattr(IncidentEntry, column) == value)
        return query.all()

