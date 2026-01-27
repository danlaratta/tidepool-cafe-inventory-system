from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError


class InventoryLogCrud:
    def __init__(self, db_session: AsyncSession) -> None:
        self.db_session = db_session


    # Create InventoryLog 
    async def create_inventory_log(self) -> None:
        pass


    # Get InventoryLog 
    async def get_inventory_log(self) -> None:
        pass


    # Update InventoryLog 
    async def update_inventory_log(self) -> None:
        pass


    # Delete InventoryLog 
    async def delete_inventory_log(self) -> None:
        pass

