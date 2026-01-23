from sqlalchemy import Integer, Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import date
from app.models.base import Base


class Inventory(Base):
    __tablename__ = 'inventories'

    # Columns
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    quantity_in_stock: Mapped[int] = mapped_column(Integer, nullable=False)
    received_at: Mapped[date] = mapped_column(Date, nullable=False, default=date.today)
    expires_at: Mapped[date] = mapped_column(Date, nullable=False)


    # Foriegn Keys
    # product id
    # purchase order item id

    # Relationships
    # product 
    # purchase order item 
    # inventory log