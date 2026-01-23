from sqlalchemy import Integer, Enum, TIMESTAMP, func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from app.enums.log_type import InventoryLogType
from app.models.base import Base


class InventoryLog(Base):
    __tablename__ = 'inventory_logs'

    # Columns
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    quantity_change_amount: Mapped[int] = mapped_column(Integer, nullable=False)
    log_type: Mapped[InventoryLogType] = mapped_column(
        Enum(
            InventoryLogType,
            name='logtype',
            native_enum=True,
            values_callable=lambda enum_cls: [e.value for e in enum_cls]
        ),
        nullable=False
    )
    created_at: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), nullable=False, server_default=func.now())
    updated_at: Mapped[datetime | None] = mapped_column(TIMESTAMP(timezone=True), nullable=True)
    
    # Foriegn Keys
    # product id
    # inventory id

    # Relationships
    # product 
    # purchase order item 
    # inventory