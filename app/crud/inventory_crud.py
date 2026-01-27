from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from app.exceptions.database_exception import DatabaseException
from app.models.inventory import Inventory


class InventoryCrud:
    def __init__(self, db_session: AsyncSession) -> None:
        self.db_session = db_session


    # Create Inventory 
    async def create_inventory(self) -> None:
        pass


    # Get Inventory 
    async def get_inventory(self, inventory_id: int) -> Inventory:
        result = await self.db_session.execute(select(Inventory).where(Inventory.id == inventory_id))
        inventory: Inventory | None = result.scalar_one_or_none()

        if inventory is None:
            raise DatabaseException(f'No inventory found with id: {inventory_id}')
        return inventory


    # Update Inventory 
    async def update_inventory(self) -> None:
        pass


    # Delete Inventory 
    async def delete_inventory(self) -> None:
        pass


