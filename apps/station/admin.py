import xadmin
from xadmin import views
from .models import Station

xadmin.site.register(Station)
