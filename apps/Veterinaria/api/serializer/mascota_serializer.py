from rest_framework import serializers
from apps.Veterinaria.models import  Mascota

       
class MascotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mascota
        fields = '__all__'
            
class UpdateMascotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mascota
        fields = ('cliente', ' nombre_mascota', 'numero_chip')

class MascotaListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mascota
        
    def to_representation(self, instance):
        return {
            'id': instance["id"],
            'cliente': instance["cliente"],
            'nombre_mascota': instance["nombre_mascota"],
            'numero_chip': instance["numero_chip"],       
    }
       

        