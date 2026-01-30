from sqlalchemy import Integer, TIMESTAMP, func, Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime, date
from app.models.base import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.purchase_order_item import PurchaseOrderItem
    from app.models.delivery_log import DeliveryLog


class Delivery(Base):
    __tablename__ = 'deliveries'

    # Columns
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    quantity_in_delivery: Mapped[int] = mapped_column(Integer, nullable=False)
    created_at: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), nullable=False, server_default=func.now())
    received_at: Mapped[date] = mapped_column(Date, nullable=False, default=date.today)
    expires_at: Mapped[date | None] = mapped_column(Date, nullable=True)


    # Foriegn Keys
    purchase_order_item_id: Mapped[int] = mapped_column(Integer, ForeignKey('purchase_order_items.id'), nullable=False, unique=True)

    # Relationships
    purchase_order_item: Mapped['PurchaseOrderItem'] = relationship(back_populates='delivery')
    delivery_logs: Mapped[list['DeliveryLog']] = relationship(back_populates='delivery', cascade='all, delete-orphan', lazy='selectin')