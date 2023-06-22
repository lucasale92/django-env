from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from apps.Veterinaria.api.serializer.mascota_serializer import MascotaSerializer ,UpdateMascotaSerializer, MascotaListSerializer
from apps.Veterinaria.models import  Mascota

class MascotaViewSet(viewsets.GenericViewSet):
    model = Mascota
    serializer_class = MascotaSerializer
    list_serializer_class = MascotaListSerializer
    queryset = Mascota.objects.filter(estado=True)

    def get_object(self, pk):
        return get_object_or_404(self.model, pk=pk)

    def get_queryset(self):
        if self.queryset is None:
            self.queryset = self.model.objects.filter(estado=True).values('id', 'cliente','numero_chip','nombre_mascota')
        return self.queryset

    def list(self, request):
        """
        Informacion sobre la lista de Mascotas 
        """
        mascotas = self.get_queryset().values('id', 'cliente','numero_chip','nombre_mascota')
        mascotas_serializer = self.list_serializer_class(mascotas, many=True)
        return Response(mascotas_serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        """
        Aqui se crean las Mascotas
        """
        mascota_serializer = self.serializer_class(data=request.data)
        if mascota_serializer.is_valid():
            mascota_serializer.save()
            return Response({
                'message': 'Mascota registrada correctamente.'
            }, status=status.HTTP_201_CREATED)
        return Response({
            'message': 'Hay errores en el registro',
            'errors': mascota_serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)    
        
    def retrieve(self, request, pk=None):
        """
        Aqui se buscan por N° de ID
        """
        mascota = self.get_object(pk)
        mascota_serializer = self.serializer_class(mascota)
        return Response(mascota_serializer.data)

    def update(self, request, pk=None):
        """
        Aqui se actualiza la informacion
        """
        mascota = self.get_object(pk)
        mascota_serializer = UpdateMascotaSerializer(mascota, data=request.data)
        if mascota_serializer.is_valid():
            mascota_serializer.save()
            return Response({
                'message': 'Usuario actualizado correctamente'
            }, status=status.HTTP_200_OK)
        return Response({
            'message': 'Hay errores en la actualización',
            'errors': mascota_serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
        
    def destroy(self, request, pk=None):
        """
        Aqui se elimina la mascota 
        """
        mascota_destroy = self.model.objects.filter(id=pk).update(estado=False)
        if mascota_destroy == 1:
            return Response({
                'message': 'mascota eliminada correctamente'
            })
        return Response({
            'message': 'No existe la mascota que desea eliminar'
        }, status=status.HTTP_404_NOT_FOUND)