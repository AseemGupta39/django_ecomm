from django.urls import path
from accounts.views import *

urlpatterns = [
    path('login/', login_page,name = "login"),
    # path('admin/', admin.site.urls),
]