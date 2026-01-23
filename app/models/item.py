from sqlalchemy import Integer, String, Enum, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.enums.item_category import ItemCategory
from app.enums.quantity_unit import QuantityUnit
from app.models.base import Base


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
    # supplier id 

    # Relationships
    # supplier
    # inventory
    # purchase order item
    # inventory log
