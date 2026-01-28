from sqlalchemy import Integer, String, Enum, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.enums.item_category import ItemCategory
from app.enums.quantity_unit import QuantityUnit
from app.models.base import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.delivery_log import DeliveryLog
    from app.models.delivery import Delivery
    from app.models.supplier import Supplier
    from app.models.purchase_order_item import PurchaseOrderItem

class Item(Base):
    __tablename__ = 'items'

    # Columns
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    category: Mapped[ItemCategory] = mapped_column(
        Enum(
            ItemCategory,
            name='itemcategory',
            native_enum=True,
            values_callable=lambda enum_cls: [e.value for e in enum_cls]
        ),
        nullable=False
    )
    reorder_threshold: Mapped[int] = mapped_column(Integer, nullable=False)
    reorder_amount: Mapped[int] = mapped_column(Integer, nullable=False)
    quantity_unit: Mapped[QuantityUnit] = mapped_column(
        Enum(
            QuantityUnit,
            name='quantityunit',
            native_enum=True,
            values_callable=lambda enum_cls: [e.value for e in enum_cls]
        ),
        nullable=False
    )
    perishable: Mapped[bool] = mapped_column(Boolean, nullable=False)


    # Foriegn Key
    supplier_id: Mapped[int] = mapped_column(Integer, ForeignKey('suppliers.id'), nullable=False)

    # Relationships
    supplier: Mapped['Supplier'] = relationship(back_populates='items')
    deliveries: Mapped[list['Delivery']] = relationship(back_populates='item', cascade='all, delete-orphan', lazy='selectin')
    purchase_order_items: Mapped[list['PurchaseOrderItem']] = relationship(back_populates='item', cascade='all, delete-orphan', lazy='selectin')
    inventory_logs: Mapped[list['DeliveryLog']] = relationship(back_populates='item', cascade='all, delete-orphan', lazy='selectin')
