from src.app.core.db.database import Base
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column


class Test(Base):
    __tablename__ = "test"

    id: Mapped[int] = mapped_column(
        "id",
        autoincrement=True,
        nullable=False,
        unique=True,
        primary_key=True,
        init=False,
    )

    desc: Mapped[str] = mapped_column(String(255))
