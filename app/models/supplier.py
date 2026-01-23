from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.base import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.item import Item
    from app.models.purchase_order import PurchaseOrder


class Supplier(Base):
    __tablename__ = 'suppliers'

    # Columns
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    email: Mapped[str] = mapped_column(String(255), nullable=False, unique=True) 
    phone: Mapped[str] = mapped_column(String(15), nullable=False)


    # Relationships
    items: Mapped[list['Item']] = relationship(back_populates='supplier', cascade='all, delete-orphan', lazy='selectin')
    purchase_orders: Mapped[list['PurchaseOrder']] = relationship(back_populates='supplier', cascade='all, delete-orphan', lazy='selectin')