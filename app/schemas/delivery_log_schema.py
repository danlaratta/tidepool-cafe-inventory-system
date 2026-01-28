from pydantic import BaseModel, Field, model_validator
from datetime import datetime, timezone
from app.enums.log_type import DeliveryLogType


class DeliveryLogBase(BaseModel):
    quantity_change_amount: int
    log_type: DeliveryLogType
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime | None

    @model_validator(mode='after')
    def validate_dates(self):
        if self.updated_at:
            if self.updated_at < self.created_at:
                raise ValueError('updated_at cannot be before created_at')
        return self


class DeliveryLogCreate(DeliveryLogBase):
    delivery_id: int


class DeliveryLogUpdate(BaseModel):
    quantity_change_amount: int
    log_type: DeliveryLogType
    updated_at: datetime | None


class DeliveryLogResponse(DeliveryLogBase):
    id: int 
    delivery_id: int

    class Config:
        from_attributes = True