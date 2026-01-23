from enum import Enum 

class PurchaseOrderStatus(Enum):
    SUBMITTED = 'Submitted'
    ORDERED = 'Ordered'
    RECEIVED = 'Received'