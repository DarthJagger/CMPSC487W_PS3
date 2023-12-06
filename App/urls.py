from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("Manager/", views.Manager, name="Manager"),
    path("AddTenant/", views.AddTenants, name="Add Tenant"),
    path("Manager/Man_UpdateTen/<ID>/", views.UpdateTen, name="Update Tenant"),
    path("Manager/Man_DeleteTen/<ID>/", views.DeleteTen, name="Delete Tenant"),
    path("Tenant/<apartments>/", views.Tenant, name="Tenant"),
    path("Tenant/<apartments>/Addrequest/", views.Addrequests, name="Tenant"),
    path("Staff/", views.Staff, name="Staff"),
    path("request/<ID>/", views.request, name="Staff"),




]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)