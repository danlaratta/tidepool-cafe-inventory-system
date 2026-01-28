from sqlalchemy import Integer, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.base import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.item import Item
    from app.models.purchase_order import PurchaseOrder
    from app.models.delivery import Delivery


class PurchaseOrderItem(Base):
    __tablename__ = 'purchase_order_items'

    # Columns
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    quantity: Mapped[int] = mapped_column(Integer, nullable=False)
    delivery_received: Mapped[bool] = mapped_column(Boolean, nullable=False)

    # Foreign Key
    item_id: Mapped[int] = mapped_column(Integer, ForeignKey('items.id'), nullable=False)
    purchase_order_id: Mapped[int] = mapped_column(Integer, ForeignKey('purchase_orders.id'), nullable=False)

    # Relationships
    item: Mapped['Item'] = relationship(back_populates='purchase_order_items')
    purchase_order: Mapped['PurchaseOrder'] = relationship(back_populates='purchase_order_items')
    delivery: Mapped['Delivery'] = relationship(back_populates='purchase_order_item', uselist=False)

