from rest_framework import generics
from .models import Company, Employee, Device, Asset
from .serializers import CompanySerializer, EmployeeSerializer, DeviceSerializer, AssetSerializer


class CompanyList(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class EmployeeList(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class DeviceList(generics.ListCreateAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer


class AssetList(generics.ListCreateAPIView):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer
