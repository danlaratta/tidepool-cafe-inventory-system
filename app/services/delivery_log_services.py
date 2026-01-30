from app.crud.delivery_log_crud import DeliveryLogCrud
from app.enums.log_type import DeliveryLogType
from app.models.delivery_log import DeliveryLog


class DeliveryLogService:
    def __init__(self, log_crud: DeliveryLogCrud) -> None:
        self.log_crud = log_crud

    #  Create Log
    async def create_log(self, change_amount: int, log_type: DeliveryLogType, delivery_id: int) -> None:
        # Get 
        pass


    #  Update Log
    async def update_log(self) -> None:
        pass


    #  Delete Log
    async def delete_log(self) -> None:
        pass


