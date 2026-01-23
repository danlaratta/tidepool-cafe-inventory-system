from sqlalchemy import Integer, Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import date
from app.models.base import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.item import Item
    from app.models.purchase_order_item import PurchaseOrderItem
    from app.models.inventory_log import InventoryLog


class Inventory(Base):
    __tablename__ = 'inventories'

    # Columns
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    quantity_in_stock: Mapped[int] = mapped_column(Integer, nullable=False)
    received_at: Mapped[date] = mapped_column(Date, nullable=False, default=date.today)
    expires_at: Mapped[date] = mapped_column(Date, nullable=False)


    # Foriegn Keys
    item_id: Mapped[int] = mapped_column(Integer, ForeignKey('items.id'), nullable=False)
    purchase_order_item_id: Mapped[int] = mapped_column(Integer, ForeignKey('purchase_order_items.id'), nullable=False)

    # Relationships
    item: Mapped['Item'] = relationship(back_populates='inventories')
    purchase_order_item: Mapped['PurchaseOrderItem'] = relationship(back_populates='inventories')
    inventory_logs: Mapped[list['InventoryLog']] = relationship(back_populates='item', cascade='all, delete-orphan', lazy='selectin')