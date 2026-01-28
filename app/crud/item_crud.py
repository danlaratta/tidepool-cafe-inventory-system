from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from app.models.item import Item
from app.exceptions.database_exception import DatabaseException


class ItemCrud:
    def __init__(self, db_session: AsyncSession) -> None:
        self.db_session = db_session


    # Create Item 
    async def create_item(self) -> None:
        pass


    # Get Item 
    async def get_item(self, item_id: int) -> Item:
        result = await self.db_session.execute(select(Item).where(Item.id == item_id))
        item: Item | None = result.scalar_one_or_none()

        if item is None:
            raise DatabaseException(f'No item found with id: {item_id}')
        return item


    # Update Item 
    async def update_item(self) -> None:
        pass


    # Delete Item 
    async def delete_item(self) -> None:
        pass