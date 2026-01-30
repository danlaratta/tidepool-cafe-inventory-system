from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.exceptions.database_exception import DatabaseException
from app.models.purchase_order_item import PurchaseOrderItem

class PurchaseOrderItemCrud:
    def __init__(self, db_session: AsyncSession) -> None:
        self.db_session = db_session


    # Create PurchaseOrderItem 
    async def create_order_item(self) -> None:
        pass


    # Get PurchaseOrderItem 
    async def get_order_item(self, order_item_id: int) -> PurchaseOrderItem:
        result = await self.db_session.execute(select(PurchaseOrderItem).where(PurchaseOrderItem.id == order_item_id))
        order_item: PurchaseOrderItem | None = result.scalar_one_or_none()

        if order_item is None:
            raise DatabaseException(f'No purchase order item found with id: {order_item_id}')
        return order_item


    # Update PurchaseOrderItem 
    async def update_order_item(self) -> None:
        pass


    # Delete PurchaseOrderItem 
    async def delete_order_item(self) -> None:
        pass