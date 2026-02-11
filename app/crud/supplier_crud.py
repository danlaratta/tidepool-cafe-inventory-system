from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.exceptions.database_exception import DatabaseException
from app.models.supplier import Supplier


class SupplierCrud:
    def __init__(self, db_session: AsyncSession) -> None:
        self.db_session = db_session

    # Create Supplier 
    async def create_supplier(self) -> None:
        pass


    # Get Supplier 
    async def get_supplier(self, supplier_id: int) -> Supplier:
        result = await self.db_session.execute(select(Supplier).where(Supplier.id == supplier_id))
        supplier: Supplier | None = result.scalar_one_or_none()

        if supplier is None:
            raise DatabaseException(f'No supplier found with id: {supplier_id}')
        return supplier


    # Update Supplier 
    async def update_supplier(self) -> None:
        pass


    # Delete Supplier 
    async def delete_supplier(self) -> None:
        pass