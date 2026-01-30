from datetime import date, timedelta
from app.crud.delivery_crud import DeliveryCrud
from app.crud.purchase_order_item_crud import PurchaseOrderItemCrud
from app.enums.category_expiration import CategoryExpirationDays
from app.models.delivery import Delivery
from app.models.purchase_order_item import PurchaseOrderItem


class DeliveryService:
    def __init__(self, delivery_crud: DeliveryCrud, order_item_crud: PurchaseOrderItemCrud) -> None:
        self.delivery_crud = delivery_crud
        self.order_item_crud = order_item_crud


    # Create new delivery
    async def create_new_delivery(self, quantity: int, received_at: date | None, purchase_order_item_id: int) -> Delivery:
        # Get the purchase order item in delivery
        order_item: PurchaseOrderItem = await self.order_item_crud.get_order_item(purchase_order_item_id)
    
        # Set received_at (defaults to today if no date provided)
        received_at = received_at or date.today()

        # Calculate the expiration date based on the item's category (None is for disposable items that don't expire)
        expiration_days = CategoryExpirationDays[order_item.item.category.name].value
        expires_at: date | None = None if expiration_days is None else received_at + timedelta(days=expiration_days)

        # Create delivery
        delivery: Delivery = Delivery(
            quantity_in_delivery = quantity, 
            received_at = received_at,
            expires_at = expires_at,
            purchase_order_item_id = order_item.id
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