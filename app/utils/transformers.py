import pandas as pd


def to_dataframe(entries):
    """Convert list of SQLAlchemy ORM objects to pandas DataFrame."""
    data = [entry.__dict__ for entry in entries]
    for d in data:
        d.pop("_sa_instance_state", None)

    df = pd.DataFrame(data)

    column_order = [
        "date", "year", "month", "day", "city", "state", "killed", "wounded", "names", "suspect_status",
        "suspect_keyword", "sources", "id",
    ]

    df = df.reindex(columns=column_order)

    return df
