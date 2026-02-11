from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.exceptions.database_exception import DatabaseException
from app.models.purchase_order import PurchaseOrder


class PurchaseOrderCrud:
    def __init__(self, db_session: AsyncSession) -> None:
        self.db_session = db_session


    # Create PurchaseOrder 
    async def create_purchase_order(self, order: PurchaseOrder) -> PurchaseOrder:
        self.db_session.add(order)
        await self.db_session.flush()
        return order
        

    # Get PurchaseOrder 
    async def get_purchase_order(self, order_id: int) -> PurchaseOrder:
        result = await self.db_session.execute(select(PurchaseOrder).where(PurchaseOrder.id == order_id))
        order: PurchaseOrder | None = result.scalar_one_or_none()

        if order is None:
            raise DatabaseException(f'No purchase order found with id: {order_id}') 
        return order


    # Update PurchaseOrder 
    async def update_purchase_order(self, order: PurchaseOrder) -> PurchaseOrder:
        await self.db_session.flush()
        return order


    # Delete PurchaseOrder 
    async def delete_purchase_order(self, order: PurchaseOrder) -> None:
        await self.db_session.delete(order)