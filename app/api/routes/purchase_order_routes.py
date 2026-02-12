from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.crud.purchase_order_crud import PurchaseOrderCrud
from app.crud.supplier_crud import SupplierCrud
from app.database.database import get_db
from models.purchase_order import PurchaseOrder
from app.schemas.purchase_order_schema import PurchaseOrderCreate, PurchaseOrderUpdate, PurchaseOrderResponse
from app.services.purchase_order_services import PurchaseOrderService


# Create purchase_order router
router = APIRouter(prefix='/purchase-orders', tags=['Purchase Orders'])


# Dependency builder
def get_purchase_order_service(db: AsyncSession = Depends(get_db)) -> PurchaseOrderService:
    order_crud: PurchaseOrderCrud = PurchaseOrderCrud(db)
    supplier_crud: SupplierCrud = SupplierCrud(db)
    return PurchaseOrderService(order_crud, supplier_crud)


# Create Route
@router.post('/', response_model= PurchaseOrderResponse, status_code=status.HTTP_201_CREATED) 
async def create_purchase_order_route(order_create: PurchaseOrderCreate, service: PurchaseOrderService = Depends(get_purchase_order_service)) -> PurchaseOrder:
    purchase_order: PurchaseOrder = await service.create_purchase_order(
        order_status = order_create.status,
        updated_at = order_create.updated_at,
        delivery_date = order_create.delivery_date,
        supplier_id = order_create.supplier_id,
    )
    return purchase_order


# Get Route
@router.get('/{order_id}', response_model= PurchaseOrderResponse, status_code=status.HTTP_200_OK) 
async def get_purchase_order_route(order_id: int, service: PurchaseOrderService = Depends(get_purchase_order_service)) -> PurchaseOrder:
    purchase_order: PurchaseOrder = await service.get_purchase_order(order_id)
    return purchase_order

    
# Update Route
@router.put('/{order_id}', response_model= PurchaseOrderResponse, status_code=status.HTTP_200_OK) 
async def update_purchase_order_route(order_id: int, order_update: PurchaseOrderUpdate, service: PurchaseOrderService = Depends(get_purchase_order_service)) -> PurchaseOrder:
    update_purchase_order = await service.update_purchase_order(
        order_id = order_id,
        status = order_update.status,
        delivery_date = order_update.delivery_date,
    )
    return update_purchase_order


# Delete Route
@router.delete('/{order_id}', response_model= PurchaseOrderResponse, status_code=status.HTTP_204_NO_CONTENT) 
async def delete_purchase_order_route(order_id: int, service: PurchaseOrderService = Depends(get_purchase_order_service)) -> None:
    await service.delete_purchase_order(order_id)
