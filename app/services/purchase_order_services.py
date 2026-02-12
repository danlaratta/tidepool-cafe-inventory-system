from datetime import datetime, timezone
from app.crud.purchase_order_crud import PurchaseOrderCrud
from app.crud.supplier_crud import SupplierCrud
from app.enums.purchase_order_status import PurchaseOrderStatus
from app.models.purchase_order import PurchaseOrder
from app.models.supplier import Supplier


class PurchaseOrderService:
    def __init__(self, order_crud: PurchaseOrderCrud, supplier_crud: SupplierCrud) -> None:
        self.order_crud = order_crud
        self.supplier_crud = supplier_crud


    # Create new purchase order
    async def create_purchase_order(self, order_status: PurchaseOrderStatus, updated_at: datetime | None, delivery_date: datetime | None, supplier_id: int) -> PurchaseOrder:
        # Get supplier
        supplier: Supplier = await self.supplier_crud.get_supplier(supplier_id)

        # Create purchase order
        order: PurchaseOrder = PurchaseOrder(
            status = order_status, 
            updated_at = updated_at,
            delivery_date = delivery_date,
            supplier_id = supplier.id,
        )
        
        return await self.order_crud.create_purchase_order(order)

    
    # Get purchase order
    async def get_purchase_order(self, order_id: int) -> PurchaseOrder:
        order: PurchaseOrder = await self.order_crud.get_purchase_order(order_id)
        return order


    # Update purchase order
    async def update_purchase_order(self, order_id: int, status: PurchaseOrderStatus, delivery_date: datetime | None) -> PurchaseOrder:
        # Get purchase order to update 
        order: PurchaseOrder = await self.order_crud.get_purchase_order(order_id)

        # Validate
        if status not in PurchaseOrderStatus:
            raise ValueError('Status provided is an invalid PurchaseOrderStatus')
        
        if delivery_date is not None and delivery_date < datetime.now():
            raise ValueError('Delivery date must be a current or future date, cannot be updated to a date in the past')
        
        # Update purchase order
        order.status = status
        order.updated_at = datetime.now(timezone.utc)
        order.delivery_date = delivery_date

        return await self.order_crud.update_purchase_order(order)


    # Delete purchase order
    async def delete_purchase_order(self, order_id: int) -> None:
        # Get purchase order to delete
        order: PurchaseOrder = await self.order_crud.get_purchase_order(order_id)
        await self.order_crud.delete_purchase_order(order)
        

