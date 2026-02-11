from app.crud.supplier_crud import SupplierCrud
from app.models.supplier import Supplier

class SupplierService:
    def __init__(self, supplier_crud: SupplierCrud) -> None:
        self.supplier_crud = supplier_crud


    # Create new supplier
    async def create_new_supplier(self, name: str, email: str, phone: str) -> Supplier:
        # Create supplier
        supplier: Supplier = Supplier(
            name = name,
            email = email,
            phone = phone
        )

        return await self.supplier_crud.create_supplier(supplier)


    # Delete supplier
    async def delete_supplier(self, supplier_id: int) -> None:
        supplier: Supplier = await self.supplier_crud.get_supplier(supplier_id)
        await self.supplier_crud.delete_supplier(supplier)

