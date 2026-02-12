from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.crud.item_crud import ItemCrud
from app.crud.supplier_crud import SupplierCrud
from app.database.database import get_db
from app.models.item import Item
from app.schemas.item_schema import ItemCreate, ItemUpdate, ItemResponse
from app.services.item_services import ItemService

# Create Router
router = APIRouter(prefix='/items', tags=['Items'])


# Dependency Builder
def get_item_service(db: AsyncSession = Depends(get_db)) -> ItemService:
    item_crud: ItemCrud = ItemCrud(db)
    supplier_crud: SupplierCrud = SupplierCrud(db)
    return ItemService(item_crud, supplier_crud)


# Create Route 
@router.post('/', response_model=ItemResponse, status_code=status.HTTP_201_CREATED)
async def create_item_route(item_create: ItemCreate, service: ItemService = Depends(get_item_service)) -> Item:
    item: Item = await service.create_item(
        name = item_create.name, 
        category = item_create.category, 
        threshold = item_create.reorder_threshold, 
        reorder_amount = item_create.reorder_amount, 
        unit = item_create.quantity_unit, 
        perishable = item_create.perishable, 
        supplier_id= item_create.supplier_id,
    )
    return item


# Get Route 
@router.get('/{item_id}', response_model=ItemResponse, status_code=status.HTTP_200_OK)
async def get_item_route(item_id: int, service: ItemService = Depends(get_item_service)) -> Item:
    item: Item = await service.get_item(item_id)
    return item


# Update Route 
@router.put('/{item_id}', response_model=ItemResponse, status_code=status.HTTP_200_OK)
async def update_item_route(item_id: int, item_update: ItemUpdate, service: ItemService = Depends(get_item_service)) -> Item:
    update_item: Item = await service.update_item(
        item_id = item_id,
        threshold = item_update.reorder_threshold,
        reorder_amount = item_update.reorder_amount,
    )
    return update_item


# Delete Route 
@router.delete('/{item_id}', response_model=ItemResponse, status_code=status.HTTP_204_NO_CONTENT)
async def delete_item_route(item_id: int, service: ItemService = Depends(get_item_service)) -> None:
    await service.delete_item(item_id)