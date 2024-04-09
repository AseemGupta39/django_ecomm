from django.db.models import Models
from django.db.models import UUIDField
from django.db.models import DateTimeField
from uuid import uuid4

class BaseModel(Models):
    uid = UUIDField(primary_key = True,editable=False,default=uuid4)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_add = True)
    
    class Meta:
        abstract = True
         
