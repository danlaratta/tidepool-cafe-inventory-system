from datetime import date
from app.crud.delivery_crud import DeliveryCrud
from app.models.delivery import Delivery

class DeliveryService:
    def __init__(self, delivery_crud: DeliveryCrud) -> None:
        self.delivery_crud = delivery_crud

    # Create new delivery
    async def create_new_delivery(self, quantity_in_stock: int, received_at: date, expires_at: date, item_id: int, purchase_order_item_id: int) -> None:
        delivery: Delivery = Delivery(

        )
        

