from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.crud.supplier_crud import SupplierCrud
from app.database.database import get_db
from models.supplier import Supplier
from app.schemas.supplier_schema import SupplierCreate, SupplierResponse
from app.services.supplier_services import SupplierService


# Create router
router = APIRouter(prefix='/suppliers', tags=['Suppliers'])


# Dependency builder
def get_supplier_service(db: AsyncSession = Depends(get_db)) -> SupplierService:
    supplier_crud: SupplierCrud = SupplierCrud(db)
    return SupplierService(supplier_crud)


# Create Route
@router.post('/', response_model= SupplierResponse, status_code=status.HTTP_201_CREATED) 
async def create_supplier_route(supplier_create: SupplierCreate, service: SupplierService = Depends(get_supplier_service)) -> Supplier:
    supplier: Supplier = await service.create_supplier(
        name = supplier_create.name,
        email = supplier_create.email,
        phone = supplier_create.phone,
    )
    return supplier


# Get Route
@router.get('/{supplier_id}', response_model= SupplierResponse, status_code=status.HTTP_200_OK) 
async def get_supplier_route(supplier_id: int, service: SupplierService = Depends(get_supplier_service)) -> Supplier:
    supplier: Supplier = await service.supplier_crud.get_supplier(supplier_id)
    return supplier

    
# Delete Route
@router.delete('/{supplier_id}', response_model= SupplierResponse, status_code=status.HTTP_204_NO_CONTENT) 
async def delete_supplier_route(supplier_id: int, service: SupplierService = Depends(get_supplier_service)) -> None:
    await service.delete_supplier(supplier_id)
    