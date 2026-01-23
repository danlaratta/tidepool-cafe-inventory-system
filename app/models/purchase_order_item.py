from sqlalchemy import Integer, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.base import Base

class PurchaseOrderItem(Base):
    __tablename__ = 'purchase_order_items'

    # Columns
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    quantity: Mapped[int] = mapped_column(Integer, nullable=False)
    delivery_received: Mapped[bool] = mapped_column(Boolean, nullable=False)

    # Foreign Key
    # purchase order id
    # product

    # Relationships
    # purchase order 
    # inventory log