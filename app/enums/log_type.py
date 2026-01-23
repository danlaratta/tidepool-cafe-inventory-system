from enum import Enum 

class InventoryLogType(Enum):
    RECEIVED = 'Received'       
    USED = 'Used'               
    EXPIRED = 'Expired'         
