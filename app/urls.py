from django.urls import path
from . import views

urlpatterns = [
    path('companies/', views.CompanyList.as_view(), name='company-list'),
    path('employees/', views.EmployeeList.as_view(), name='employee-list'),
    path('devices/', views.DeviceList.as_view(), name='device-list'),
    path('assets/', views.AssetList.as_view(), name='asset-list'),
    # Add more URL patterns as needed for other views
]