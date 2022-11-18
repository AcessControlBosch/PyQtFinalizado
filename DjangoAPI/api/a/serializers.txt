from rest_framework import serializers
from .models import *

# class JobPositionTableAll(serializers.ModelSerializer):
#
#     class Meta:
#         many = True
#         model = JobPosition
#         fields = '__all__'

class JobPositionTable(serializers.ModelSerializer):

    class Meta: 
        many = True
        model = JobPosition
        fields = ['typeJob']


class AssociateTable(serializers.ModelSerializer):

    class Meta: 
        many = True
        model = Associate
        fields = '__all__'

class GetAssociateTable(serializers.ModelSerializer):

    jobposition = JobPositionTable(read_only=True)

    class Meta: 
        many = True
        model = Associate
        fields = '__all__'

class GetAssociateTableName(serializers.ModelSerializer):

    class Meta:
        many = True
        model = Associate
        fields = ['name', 'EDV'] 

class AssociateTableID(serializers.ModelSerializer):

    class Meta:
        many = True
        model = Associate
        fields = ['id']

class JobPositionTable(serializers.ModelSerializer):

    class Meta:
        many = True
        model = JobPosition
        fields = '__all__'

class MachineTable(serializers.ModelSerializer):

    class Meta: 
        many = True
        model = Machine
        fields = '__all__'

class GetMachineTable(serializers.ModelSerializer):

    class Meta:
        many = True
        model = Machine
        fields = ['name']

class QuestionTable(serializers.ModelSerializer):

    class Meta: 
        many = True
        model = Question
        fields = '__all__'

class AreasTable(serializers.ModelSerializer):

    class Meta: 
        many = True
        model = Areas
        fields = '__all__'

class MaintenanceTable(serializers.ModelSerializer):

    class Meta: 
        many = True
        model = Maintenance
        fields = '__all__'

class ReleaseMachineTable(serializers.ModelSerializer):


    class Meta: 
        many = True
        model = ReleaseMachine
        fields = '__all__'

class GetReleaseMachineTable(serializers.ModelSerializer):

    idMachineFK = MachineTable(read_only=True)
    idAssociateFK = GetAssociateTable(read_only=True)

    class Meta: 
        many = True
        model = ReleaseMachine
        fields = '__all__'

class ObservationTable(serializers.ModelSerializer):

    class Meta: 
        many = True
        model = Observation
        fields = '__all__'

class GetObservationTable(serializers.ModelSerializer):

    idMachineFK = MachineTable(read_only=True)
    idAssociateFK = AssociateTable(read_only=True)

    class Meta: 
        many = True
        model = Observation
        fields = '__all__'

class GreenBookTable(serializers.ModelSerializer):

    # idMachineFK = MachineTable(read_only=True)
    # idAssociateFK = MachineTable(read_only=True)

    class Meta: 
        many = True
        model = GreenBook
        fields = '__all__'


class LoginTable(serializers.ModelSerializer):

    class Meta: 
        many = True
        model = Login
        fields = '__all__'