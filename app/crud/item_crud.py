from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError


class ItemCrud:
    def __init__(self, db_session: AsyncSession) -> None:
        self.db_session = db_session


    # Create Item 
    async def create_item(self) -> None:
        pass


    # Get Item 
    async def get_item(self) -> None:
        pass


    # Update Item 
    async def update_item(self) -> None:
        pass


    # Delete Item 
    async def delete_item(self) -> None:
        pass