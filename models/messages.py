from datetime import datetime, timezone
from sqlmodel import Field, SQLModel

__all__ = "Messages"


class Messages(SQLModel, table=True):
    id: int = Field(nullable=False, primary_key=True)
    date: datetime = Field(
        nullable=False,
        default=datetime.now(tz=timezone.utc)
    )
    author: str = Field(nullable=False)
    text: str = Field(nullable=False)
