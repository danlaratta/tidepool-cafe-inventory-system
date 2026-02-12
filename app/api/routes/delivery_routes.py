from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.crud.delivery_crud import DeliveryCrud
from app.crud.purchase_order_item_crud import PurchaseOrderItemCrud
from app.database.database import get_db
from app.models.delivery import Delivery
from app.schemas.delivery_schema import DeliveryCreate, DeliveryUpdate, DeliveryResponse
from app.services.delivery_services import DeliveryService


# Create purchase_order router
router = APIRouter(prefix='/purchase-orders', tags=['Purchase Orders'])


# Dependency builder
def get_delivery_service(db: AsyncSession = Depends(get_db)) -> DeliveryService:
    delivery_crud: DeliveryCrud = DeliveryCrud(db)
    order_item_crud: PurchaseOrderItemCrud = PurchaseOrderItemCrud(db)
    return DeliveryService(delivery_crud, order_item_crud)


# Create Route
@router.post('/', response_model=DeliveryResponse, status_code=status.HTTP_201_CREATED)
async def create_delivery(delivery_create: DeliveryCreate, service: DeliveryService = Depends(get_delivery_service)) -> Delivery:
    delivery: Delivery = await service.create_delivery(
        quantity = delivery_create.quantity_in_delivery,
        received_at = delivery_create.received_at,
        purchase_order_item_id = delivery_create.purchase_order_item_id,
    )

    return delivery


# Get Route
@router.get('/{delivery_id}', response_model=DeliveryResponse, status_code=status.HTTP_200_OK)
async def get_delivery(delivery_id: int, service: DeliveryService = Depends(get_delivery_service)) -> Delivery:
    delivery: Delivery = await service.get_delivery(delivery_id)
    return delivery


# Update Route
@router.put('/{delivery_id}', response_model=DeliveryResponse, status_code=status.HTTP_200_OK)
async def update_delivery(delivery_id: int, delivery_update: DeliveryUpdate, service: DeliveryService = Depends(get_delivery_service)) -> Delivery:
    update_delivery: Delivery = await service.update_delivery(
        delivery_id = delivery_id,
        quantity = delivery_update.quantity_in_stock,
    )
    return update_delivery


# Delete Route
@router.delete('/{delivery_id}', response_model=DeliveryResponse, status_code=status.HTTP_204_NO_CONTENT)
async def delete_delivery(delivery_id: int, service: DeliveryService = Depends(get_delivery_service)) -> None:
    await service.delete_delivery(delivery_id)

