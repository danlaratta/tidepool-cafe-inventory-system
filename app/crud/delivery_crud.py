from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from app.exceptions.database_exception import DatabaseException
from app.models.delivery import Delivery


class DeliveryCrud:
    def __init__(self, db_session: AsyncSession) -> None:
        self.db_session = db_session


    # Create Delivery 
    async def create_delivery(self) -> None:
        pass


    # Get Delivery 
    async def get_delivery(self, delivery_id: int) -> Delivery:
        result = await self.db_session.execute(select(Delivery).where(Delivery.id == delivery_id))
        delivery: Delivery | None = result.scalar_one_or_none()

        if delivery is None:
            raise DatabaseException(f'No delivery found with id: {delivery_id}')
        return delivery
    

    # Check delivery exists
    async def check_delivery_exists(self, delivery_id: int) -> bool:
        result = await self.db_session.execute(select(Delivery).where(Delivery.id == delivery_id))
        delivery: Delivery | None = result.scalar_one_or_none()

        if delivery is None:
            return False
        return True


    # Update Delivery 
    async def update_delivery(self) -> None:
        pass


    # Delete Delivery 
    async def delete_delivery(self) -> None:
        pass


