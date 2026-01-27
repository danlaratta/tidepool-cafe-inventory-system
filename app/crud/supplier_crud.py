from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError


class SupplierCrud:
    def __init__(self, db_session: AsyncSession) -> None:
        self.db_session = db_session

    # Create Supplier 
    async def create_supplier(self) -> None:
        pass


    # Get Supplier 
    async def get_supplier(self) -> None:
        pass


    # Update Supplier 
    async def update_supplier(self) -> None:
        pass


    # Delete Supplier 
    async def delete_supplier(self) -> None:
        pass