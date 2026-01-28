from sqlalchemy import Integer, Enum, TIMESTAMP, func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from app.enums.log_type import DeliveryLogType
from app.models.base import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.delivery import Delivery


class DeliveryLog(Base):
    __tablename__ = 'delivery_logs'

    # Columns
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    quantity_change_amount: Mapped[int] = mapped_column(Integer, nullable=False)
    log_type: Mapped[DeliveryLogType] = mapped_column(
        Enum(
            DeliveryLogType,
            name='logtype',
            native_enum=True,
            values_callable=lambda enum_cls: [e.value for e in enum_cls]
        ),
        nullable=False
    )
    created_at: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), nullable=False, server_default=func.now())
    updated_at: Mapped[datetime | None] = mapped_column(TIMESTAMP(timezone=True), nullable=True)
    
    # Foriegn Keys
    delivery_id: Mapped[int] = mapped_column(Integer, ForeignKey('deliveries.id'), nullable=False)

    # Relationships
    delivery: Mapped['Delivery'] = relationship(back_populates='delivery_logs')