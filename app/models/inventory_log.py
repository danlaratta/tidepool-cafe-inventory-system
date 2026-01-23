from sqlalchemy import Integer, Enum, TIMESTAMP, func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from app.enums.log_type import InventoryLogType
from app.models.base import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.item import Item
    from app.models.inventory import Inventory


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
    item_id: Mapped[int] = mapped_column(Integer, ForeignKey('items.id'), nullable=False)
    inventory_id: Mapped[int] = mapped_column(Integer, ForeignKey('inventories.id'), nullable=False)

    # Relationships
    item: Mapped['Item'] = relationship(back_populates='inventory_logs')
    inventory: Mapped['Inventory'] = relationship(back_populates='inventory_logs')