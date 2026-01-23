from sqlalchemy import Integer, Enum, TIMESTAMP, func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from app.enums.purchase_order_status import PurchaseOrderStatus
from app.models.base import Base

class PurchaseOrder(Base):
    __tablename__ = 'purchaseorders'

    # Columns
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    status: Mapped[PurchaseOrderStatus] = mapped_column(
        Enum(
            PurchaseOrderStatus,
            name='purchaseorder',
            native_enum=True,
            values_callable=lambda enum_cls: [e.value for e in enum_cls]
        ),
        nullable=False
    )
    created_at: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), nullable=False, server_default=func.now())
    updated_at: Mapped[datetime | None] = mapped_column(TIMESTAMP(timezone=True), nullable=True)
    delivery_date: Mapped[datetime | None] = mapped_column(TIMESTAMP(timezone=True), nullable=True)

    # Foreign Key
    # supplier id

    # Relationships
    # supplier
    # purchase order items

