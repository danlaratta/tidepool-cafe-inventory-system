from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError


class PurchaseOrderItemCrud:
    def __init__(self, db_session: AsyncSession) -> None:
        self.db_session = db_session


    # Create PurchaseOrderItem 
    async def create_order_item(self) -> None:
        pass


    # Get PurchaseOrderItem 
    async def get_order_item(self) -> None:
        pass


    # Update PurchaseOrderItem 
    async def update_order_item(self) -> None:
        pass


    # Delete PurchaseOrderItem 
    async def delete_order_item(self) -> None:
        pass