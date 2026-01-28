from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError


class DeliveryLogCrud:
    def __init__(self, db_session: AsyncSession) -> None:
        self.db_session = db_session


    # Create DeliveryLog 
    async def create_delivery_log(self) -> None:
        pass


    # Get DeliveryLog 
    async def get_delivery_log(self) -> None:
        pass


    # Update DeliveryLog 
    async def update_delivery_log(self) -> None:
        pass


    # Delete DeliveryLog 
    async def delete_delivery_log(self) -> None:
        pass

