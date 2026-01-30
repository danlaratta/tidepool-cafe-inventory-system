from datetime import date, timedelta
from app.crud.delivery_crud import DeliveryCrud
from app.crud.item_crud import ItemCrud
from app.enums.category_expiration import CategoryExpirationDays
from app.models.delivery import Delivery
from app.models.item import Item

class DeliveryService:
    def __init__(self, delivery_crud: DeliveryCrud, item_crud: ItemCrud) -> None:
        self.delivery_crud = delivery_crud
        self.item_crud = item_crud


    # Create new delivery
    async def create_new_delivery(self, quantity: int, received_at: date | None, item_id: int, purchase_order_item_id: int) -> Delivery:
        # Get the item in delivery
        item: Item = await self.item_crud.get_item(item_id)
    
        # Set received_at (defaults to today if no date provided)
        received_at = received_at or date.today()

        # Calculate the expiration date based on the item's category (None is for disposable items that don't expire)
        expiration_days = CategoryExpirationDays[item.category.name].value
        expires_at: date | None = None if expiration_days is None else received_at + timedelta(days=expiration_days)

        # Create delivery
        delivery: Delivery = Delivery(
            quantity_in_delivery = quantity, 
            received_at = received_at,
            expires_at = expires_at,
            item_id = item_id,
            purchase_order_item_id = purchase_order_item_id
        )
        
        return await self.delivery_crud.create_delivery(delivery)


    # Update delivery
    async def update_delivery(self, delivery_id: int, quantity: int) -> Delivery:
        # get delivery to update
        delivery: Delivery = await self.delivery_crud.get_delivery(delivery_id)

        # Validate 
        if quantity < 0:
            raise ValueError('Delivery quantity cannot be a negative number')
        
        # Update quantity
        delivery.quantity_in_delivery = quantity

        return delivery
    

    # Delete delivery
    async def delete_delivery(self, delivery_id: int):
        # get delivery to delete
        delivery: Delivery = await self.delivery_crud.get_delivery(delivery_id)
        await self.delivery_crud.delete_delivery(delivery)