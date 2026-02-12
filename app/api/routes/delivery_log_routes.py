from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.crud.delivery_log_crud import DeliveryLogCrud
from app.crud.delivery_crud import DeliveryCrud
from app.database.database import get_db
from app.models.delivery_log import DeliveryLog
from app.schemas.delivery_log_schema import DeliveryLogCreate, DeliveryLogUpdate, DeliveryLogResponse
from app.services.delivery_log_services import DeliveryLogService


# Create purchase_order router
router = APIRouter(prefix='/purchase-orders', tags=['Purchase Orders'])


# Dependency builder
def get_delivery_log_service(db: AsyncSession = Depends(get_db)) -> DeliveryLogService:
    log_crud: DeliveryLogCrud = DeliveryLogCrud(db)
    delivery_crud: DeliveryCrud = DeliveryCrud(db)
    return DeliveryLogService(log_crud, delivery_crud)

# Create Route
@router.post('/', response_model=DeliveryLogResponse, status_code=status.HTTP_201_CREATED)
async def create_delivery_log(log_create: DeliveryLogCreate, service: DeliveryLogService = Depends(get_delivery_log_service)) -> DeliveryLog:
    log: DeliveryLog = await service.create_log(
        change_amount = log_create.quantity_change_amount, 
        log_type = log_create.log_type, 
        delivery_id = log_create.delivery_id, 
    )
    return log


# Get Route
@router.get('/{log_id}', response_model=DeliveryLogResponse, status_code=status.HTTP_200_OK)
async def get_delivery_log(log_id: int, service: DeliveryLogService = Depends(get_delivery_log_service)) -> DeliveryLog:
    log: DeliveryLog = await service.get_delivery_log(log_id)
    return log


# Update Route
@router.put('/{log_id}', response_model=DeliveryLogResponse, status_code=status.HTTP_200_OK)
async def update_delivery_log(log_id: int, log_update: DeliveryLogUpdate, service: DeliveryLogService = Depends(get_delivery_log_service)) -> DeliveryLog:
    log: DeliveryLog = await service.update_log(
        log_id = log_id,
        change_amount = log_update.quantity_change_amount,
        delivery_log_type = log_update.log_type,
    )
    return log


# Delete Route
@router.delete('/{log_id}', response_model=DeliveryLogResponse, status_code=status.HTTP_204_NO_CONTENT)
async def delete_delivery_log(log_id: int, service: DeliveryLogService = Depends(get_delivery_log_service)) -> None:
    await service.delete_log(log_id)

