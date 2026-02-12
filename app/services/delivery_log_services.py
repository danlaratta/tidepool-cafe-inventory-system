from app.crud.delivery_crud import DeliveryCrud
from app.crud.delivery_log_crud import DeliveryLogCrud
from app.enums.log_type import DeliveryLogType
from app.models.delivery_log import DeliveryLog
from app.models.delivery import Delivery



class DeliveryLogService:
    def __init__(self, log_crud: DeliveryLogCrud, delivery_crud: DeliveryCrud) -> None:
        self.log_crud = log_crud
        self.delivery_crud = delivery_crud


    #  Create delivery log
    async def create_log(self, change_amount: int, log_type: DeliveryLogType, delivery_id: int) -> DeliveryLog:
        # Get delivery
        delivery: Delivery = await self.delivery_crud.get_delivery(delivery_id)

        # Create delivery log
        log: DeliveryLog = DeliveryLog(
            quantity_change_amount = change_amount,
            log_type = log_type,
            delivery_id = delivery.id
        )
        return await self.log_crud.create_delivery_log(log)


    # Get delivery log
    async def get_delivery_log(self, log_id: int) -> DeliveryLog:
        log: DeliveryLog = await self.log_crud.get_delivery_log(log_id)
        return log
    

    #  Update delivery log
    async def update_log(self, log_id: int, change_amount: int, delivery_log_type: DeliveryLogType) -> DeliveryLog:
        # Get delivery log to update
        log: DeliveryLog = await self.log_crud.get_delivery_log(log_id)

        # Validating change_amount
        if change_amount == 0:
            raise ValueError('Change amount cannot be a zero')
        
        if change_amount > 0 and delivery_log_type != DeliveryLogType.RECEIVED:
            raise ValueError('Wrong log type, log type should be RECEIVED if change amount is a positive number')
        
        if change_amount < 0 and delivery_log_type not in [DeliveryLogType.EXPIRED, DeliveryLogType.USED]:
            raise ValueError('Wrong log type, log type should be EXPIRED or USED if change amount is a negative number')
        
        # Update
        log.quantity_change_amount = change_amount
        log.log_type = delivery_log_type

        return await self.log_crud.update_delivery_log(log)
        

    #  Delete delivery log
    async def delete_log(self, log_id: int) -> None:
        # Get delivery log to update
        log: DeliveryLog = await self.log_crud.get_delivery_log(log_id)
        await self.log_crud.delete_delivery_log(log)
