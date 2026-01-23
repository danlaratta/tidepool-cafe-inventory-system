from sqlalchemy import Integer, Date, func, String, Enum, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.base import Base


class Supplier(Base):
    __tablename__ = 'suppliers'

    # Columns
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    email: Mapped[str] = mapped_column(String(255), nullable=False, unique=True) 
    phone: Mapped[str] = mapped_column(String(15), nullable=False)

    # Foriegn Key

    # Relationships