from rest_framework import serializers
from apps.Veterinaria.models import  HistoriaClinica

       
class HistoriaClinicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoriaClinica
        fields = '__all__'
            
class UpdateHistoriaClinicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoriaClinica
        fields = ('mascota', ' tipo_mascota', 'fecha_consulta', 'observaciones', 'estado')

class HistoriaClinicaListSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoriaClinica
        
    def to_representation(self, instance):
        return {
            'mascota': instance["mascota"],
            'fecha_consulta': instance["fecha_consulta"],
            'observaciones': instance["observaciones"],
            'estado': instance["estado"],       
                   
    }
       

        