from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.crud.purchase_order_item_crud import PurchaseOrderItemCrud
from app.crud.purchase_order_crud import PurchaseOrderCrud
from app.crud.item_crud import ItemCrud
from app.database.database import get_db
from app.models.purchase_order_item import PurchaseOrderItem
from app.schemas.purchase_order_item_schema import PurchaseOrderItemCreate, PurchaseOrderItemResponse
from app.services.purchase_order_item_services import PurchaseOrderItemService


# Create router
router = APIRouter(prefix='/purchase-order-items', tags=['Purchase Order Items'])


# Dependency Builder
def get_order_item_service(db: AsyncSession = Depends(get_db)) -> PurchaseOrderItemService:
    order_item_crud: PurchaseOrderItemCrud = PurchaseOrderItemCrud(db)
    item_crud: ItemCrud = ItemCrud(db)
    order_crud: PurchaseOrderCrud = PurchaseOrderCrud(db)
    return PurchaseOrderItemService(order_item_crud, item_crud, order_crud)


# Create Route
@router.post('/', response_model=PurchaseOrderItemResponse, status_code=status.HTTP_201_CREATED)
async def create_order_item_route(order_item_create: PurchaseOrderItemCreate, service: PurchaseOrderItemService = Depends(get_order_item_service)) -> PurchaseOrderItem:
    order_item: PurchaseOrderItem = await service.create_purchase_order_item(
        quantity = order_item_create.quantity,
        delivery_received = order_item_create.delivery_received,
        item_id = order_item_create.item_id,
        purchase_order_id = order_item_create.purchase_order_id,
    )

    return order_item


# Get Route
@router.get('/{order_item_id}', response_model=PurchaseOrderItemResponse, status_code=status.HTTP_200_OK)
async def get_order_item_route(order_item_id: int, service: PurchaseOrderItemService = Depends(get_order_item_service)) -> PurchaseOrderItem:
    order_item: PurchaseOrderItem = await service.get_purchase_order_item(order_item_id)
    return order_item


# Delete Route
@router.delete('/{order_item_id}')
async def delete_order_item_route(order_item_id: int, service: PurchaseOrderItemService = Depends(get_order_item_service)) -> None:
    await service.delete_purchase_order_item(order_item_id)


