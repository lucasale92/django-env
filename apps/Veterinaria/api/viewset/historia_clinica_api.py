from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from apps.Veterinaria.api.serializer.historiaClinica_serializer import HistoriaClinicaSerializer ,UpdateHistoriaClinicaSerializer, HistoriaClinicaListSerializer
from apps.Veterinaria.models import  HistoriaClinica

class HistoriaClinicaViewSet(viewsets.GenericViewSet):
    model = HistoriaClinica
    serializer_class = HistoriaClinicaSerializer
    list_serializer_class = HistoriaClinicaListSerializer
    queryset = HistoriaClinica.objects.filter(estado=True)

    def get_object(self, pk):
        return get_object_or_404(self.model, pk=pk)

    def get_queryset(self):
        if self.queryset is None:
            self.queryset = self.model.objects.filter(estado=True).values('mascota' ,'fecha_consulta','observaciones','estado')
        return self.queryset

    def list(self, request):
        """
        Informacion sobre la lista de Historias Clinicas 
        """
        historias_clinicas = self.get_queryset().values('mascota','fecha_consulta','observaciones','estado')
        historias_clinicas_serializer = self.list_serializer_class(historias_clinicas, many=True)
        return Response(historias_clinicas_serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        """
        Aqui se crean las historias clinicas
        """
        historia_clinica_serializer = self.serializer_class(data=request.data)
        if historia_clinica_serializer.is_valid():
            historia_clinica_serializer.save()
            return Response({
                'message': ' Historia clinica registrada correctamente.'
            }, status=status.HTTP_201_CREATED)
        return Response({
            'message': 'Hay errores en el registro',
            'errors': historia_clinica_serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)    
        
    def retrieve(self, request, pk=None):
        """
        Aqui se buscan por N° de ID
        """
        historia_clinica = self.get_object(pk)
        historia_clinica_serializer = self.serializer_class(historia_clinica)
        return Response(historia_clinica_serializer.data)

    def update(self, request, pk=None):
        """
        Aqui se actualiza la informacion
        """
        historia_clinica = self.get_object(pk)
        historia_clinica_serializer = UpdateHistoriaClinicaSerializer(historia_clinica, data=request.data)
        if historia_clinica_serializer.is_valid():
            historia_clinica_serializer.save()
            return Response({
                'message': ' Historia clinica actualizada correctamente'
            }, status=status.HTTP_200_OK)
        return Response({
            'message': 'Hay errores en la actualización',
            'errors': historia_clinica_serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
        
    def destroy(self, request, pk=None):
        """
        Aqui se elimina la historia clinica
        """
        historia_clinica_destroy = self.model.objects.filter(id=pk).update(estado=False)
        if historia_clinica_destroy == 1:
            return Response({
                'message': 'Historia clinica eliminada correctamente'
            })
        return Response({
            'message': 'No existe historia clinica que desea eliminar'
        }, status=status.HTTP_404_NOT_FOUND)