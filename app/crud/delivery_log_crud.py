from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.exceptions.database_exception import DatabaseException
from app.models.delivery_log import DeliveryLog


class DeliveryLogCrud:
    def __init__(self, db_session: AsyncSession) -> None:
        self.db_session = db_session


    # Create DeliveryLog 
    async def create_delivery_log(self, log: DeliveryLog) -> DeliveryLog:
        self.db_session.add(log)
        await self.db_session.flush()
        return log


    # Get DeliveryLog 
    async def get_delivery_log(self, log_id: int) -> DeliveryLog:
        result = await self.db_session.execute(select(DeliveryLog).where(DeliveryLog.id == log_id))
        delivery_log: DeliveryLog | None = result.scalar_one_or_none()

        if delivery_log is None:
            raise DatabaseException(f'No delivery log found with id: {log_id}')
        return delivery_log


    # Update DeliveryLog 
    async def update_delivery_log(self, log: DeliveryLog) -> DeliveryLog:
        await self.db_session.flush()
        return log


    # Delete DeliveryLog 
    async def delete_delivery_log(self, log: DeliveryLog) -> None:
        await self.db_session.delete(log)

