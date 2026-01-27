from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError


class PurchaseOrderCrud:
    def __init__(self, db_session: AsyncSession) -> None:
        self.db_session = db_session


    # Create PurchaseOrder 
    async def create_purchase_order(self) -> None:
        pass


    # Get PurchaseOrder 
    async def get_purchase_order(self) -> None:
        pass


    # Update PurchaseOrder 
    async def update_purchase_order(self) -> None:
        pass


    # Delete PurchaseOrder 
    async def delete_purchase_order(self) -> None:
        pass