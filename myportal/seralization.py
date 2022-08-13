from rest_framework import serializers

from .models import RetailOutlets, DivOffice

class DivOfficeSerilizer(serializers.ModelSerializer):
    class Meta:
        model = DivOffice
        fields = '__all__'

class RetailOutletsSerilizer(serializers.ModelSerializer):
    FO_name = DivOfficeSerilizer(many=False)
    # FO_name = models.ForeignKey(DivOffice, on_delete=models.CASCADE, related_name='FieldO_Name')
    # FO_name = serializers.StringRelatedField(many=False)
    class Meta:
        model = RetailOutlets
        fields = list_display = ['code','name','area','sales','type','FO_name']





    # def validate(self, data):
    #     id = data.get('id')
    #     if id < 0 :
    #         raise serializers.ValidationError('ID cant be negative')
    #     else:
    #         return data

# class officeSerilizer(serializers.Serializer):
#     id = serializers.IntegerField()
#     employee_name = serializers.CharField(max_length=70)
#     employee_role = serializers.CharField(max_length=70)
#     employee_email = serializers.EmailField(max_length=70)
#     employee_city = serializers.CharField(max_length=70)

    # def create(self,validate_data):
    #     return office.objects.create(**validate_data)
    #
    # def update(self, instance, validated_data):
    #     print(instance.employee_name)
    #     instance.id = validated_data.get('id', instance.id)
    #     instance.employee_name = validated_data.get('employee_name', instance.employee_name)
    #     instance.employee_role = validated_data.get('employee_role', instance.employee_role)
    #     instance.employee_email = validated_data.get('employee_email', instance.employee_email)
    #     #instance.employee_city = validated_data.get('employee_city', instance.employee_city)
    #     print(instance.employee_name)
    #     instance.save()
    #     return instance

