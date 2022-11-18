from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponseRedirect
from rest_framework.permissions import IsAuthenticated

#------------------------------------------------------------
#----------------------------Job Position--------------------
#------------------------------------------------------------

class JobPositionAPI(APIView):

    def get(self, request, pk=''):

        if 'name' in request.GET:
            currentlyName = request.GET['name']
            jobPosition = JobPosition.objects.filter(name__contains=currentlyName)
            serializer = JobPositionTable(jobPosition, many=True)
            return Response(serializer.data)
        
        elif pk == '':
            jobPosition = JobPosition.objects.all()
            serializer = JobPositionTable(jobPosition, many=True)
            return Response(serializer.data)

        else:
            jobPosition = JobPosition.objects.get(id_card=pk)
            serializer = JobPositionTable(jobPosition)
            return Response(serializer.data)
    
    def post(self, request):

        serializer = JobPositionTable(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()        
        return Response({"msg": "Inserido com sucesso"})

    
    def put(self, request, pk=''):

        jobPosition = JobPosition.objects.get(id=pk)
        serializer = JobPositionTable(jobPosition, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk=''):    

        jobPosition = JobPosition.objects.get(id=pk)       
        jobPosition.delete()
        return Response({"msg": "Apagado com sucesso"})



#------------------------------------------------------------
#----------------------------Associate-----------------------
#------------------------------------------------------------
class AssociateAPI(APIView):

    def get(self, request, pk=""):

        if 'name' in request.GET:
            currentlyName = request.GET['name']
            associate = Associate.objects.filter(name__contains=currentlyName)
            serializer = Associate(associate, many=True)
            return Response(serializer.data)

        elif 'user' in request.GET:
            currentlyUser = request.GET['user']
            associate = Associate.objects.filter(idUser=currentlyUser)
            serializer = AssociateTable(associate, many=True)
            return Response(serializer.data)

        elif pk == '':
            associate = Associate.objects.all()
            serializer = AssociateTable(associate, many=True)
            return Response(serializer.data)

        else:
            associate = Associate.objects.get(id_card=pk)
            serializer = AssociateTable(associate)
            return Response(serializer.data)

    def post(self, request):

        serializer = AssociateTable(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()        
        return Response({"msg": "Inserido com sucesso"})

    def put(self, request, pk=''):

        associate = Associate.objects.get(id=pk)
        serializer = AssociateTable(associate, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk=''):    

        associate = Associate.objects.get(id=pk)       
        associate.delete()
        return Response({"msg": "Apagado com sucesso"})

    def patch(self, request, pk):
        associate = Associate.objects.get(id=pk)
        serializer = AssociateTable(associate, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

#------------------------------------------------------------
#----------------------------Associate Job Name-----------------------
#------------------------------------------------------------
class GetAssociateAPI(APIView):
    def get(self, request, pk=""):
        if pk == '':
            associate = Associate.objects.all()
            serializer = GetAssociateTable(associate, many=True)
            return Response(serializer.data)

        else:
            associate = Associate.objects.get(id_card=pk)
            serializer = GetAssociateTable(associate)
            return Response(serializer.data)


#------------------------------------------------------------
#----------------------------Machine-------------------------
#------------------------------------------------------------
class MachineAPI(APIView):

    def get(self, request, pk=''):

        if pk == '':
            machineResult = Machine.objects.all()
            serializer = MachineTable(machineResult, many=True)
            return Response(serializer.data)

        else:
            machineResult = Machine.objects.get(id=pk)
            serializer = MachineTable(machineResult)
            return Response(serializer.data)

    def post(self, request):

        serializer = MachineTable(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()        
        return Response({"msg": "Inserido com sucesso"})
    
    def put(self, request, pk=''):

        machineResult = Machine.objects.get(id=pk)
        serializer = MachineTable(machineResult, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, pk=''):

        machineResult = Machine.objects.get(id=pk)       
        machineResult.delete()
        return Response({"msg": "Apagado com sucesso"})

    def patch(self, request, pk):
        machineResult = Machine.objects.get(id=pk)
        serializer = MachineTable(machineResult, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)



#------------------------------------------------------------
#----------------------- GET Machine-------------------------
#------------------------------------------------------------
class GetMachineAPI(APIView):

    def get(self, request, pk=''):

        if pk == '':
            machineResult = Machine.objects.all()
            serializer = GetMachineTable(machineResult, many=True)
            return Response(serializer.data)

        else:
            machineResult = Machine.objects.get(id=pk)
            serializer = GetMachineTable(machineResult)
            return Response(serializer.data)


#------------------------------------------------------------
#----------------------------Question------------------------
#------------------------------------------------------------
class QuestionAPI(APIView):

    def get(self, request, pk=''):

        if pk == '':
            questionResult = Question.objects.all()
            serializer = QuestionTable(questionResult, many=True)
            return Response(serializer.data)

        else:
            questionResult = Question.objects.get(id=pk)
            serializer = QuestionTable(questionResult)
            return Response(serializer.data)

    def post(self, request):

        serializer = QuestionTable(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()        
        return Response({"msg": "Inserido com sucesso"})
    
    def put(self, request, pk=''):

        questionResult = Question.objects.get(id=pk)
        serializer = QuestionTable(questionResult, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, pk=''):

        questionResult = Question.objects.get(id=pk)       
        questionResult.delete()
        return Response({"msg": "Apagado com sucesso"})

#------------------------------------------------------------
#----------------------------Green Book----------------------
#------------------------------------------------------------
class GreenBookAPI(APIView):

    def get(self, request, pk='', tq=''):

        if pk == '':
            greenBookResult = GreenBook.objects.all()
            serializer = GreenBookTable(greenBookResult, many=True)
            return Response(serializer.data)

        else:
            greenBookResult = GreenBook.objects.filter(idMachineFK=pk, typeQuestion=tq)
            serializer = GreenBookTable(greenBookResult, many=True)
            return Response(serializer.data)
            

    def post(self, request):

        serializer = GreenBookTable(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()        
        return Response({"msg": "Inserido com sucesso"})
    
    def put(self, request, pk=''):

        greenBookResult = GreenBook.objects.get(id=pk)
        serializer = GreenBookTable(greenBookResult, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, pk=''):

        greenBookResult = GreenBook.objects.get(id=pk)       
        greenBookResult.delete()
        return Response({"msg": "Apagado com sucesso"})

#------------------------------------------------------------
#----------------------------Areas---------------------------
#------------------------------------------------------------
class AreaAPI(APIView):

    def get(self, request, pk=''):

        if pk == '':
            AreaResult = Areas.objects.all()
            serializer = AreasTable(AreaResult, many=True)
            return Response(serializer.data)

        else:
            AreaResult = Areas.objects.get(id=pk)
            serializer = AreasTable(AreaResult)
            return Response(serializer.data)


    def post(self, request):

        serializer = AreasTable(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()        
        return Response({"msg": "Inserido com sucesso"})
    
    def put(self, request, pk=''):

        AreaResult = Areas.objects.get(id=pk)
        serializer = AreasTable(AreaResult, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, pk=''):

        AreaResult = Areas.objects.get(id=pk)       
        AreaResult.delete()
        return Response({"msg": "Apagado com sucesso"})

#------------------------------------------------------------
#--------------------------Maintenance-----------------------
#------------------------------------------------------------
class MaintenanceAPI(APIView):

    def get(self, request, pk=''):

        if pk == '':
            maintenanceResult = Maintenance.objects.all()
            serializer = MaintenanceTable(maintenanceResult, many=True)
            return Response(serializer.data)

        else:
            maintenanceResult = Maintenance.objects.get(id=pk)
            serializer = MaintenanceTable(maintenanceResult)
            return Response(serializer.data)

    def post(self, request):

        serializer = MaintenanceTable(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()        
        return Response({"msg": "Inserido com sucesso"})
    
    def put(self, request, pk=''):

        maintenanceResult = Maintenance.objects.get(id=pk)
        serializer = MaintenanceTable(maintenanceResult, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, pk=''):

        maintenanceResult = Maintenance.objects.get(id=pk)       
        maintenanceResult.delete()
        return Response({"msg": "Apagado com sucesso"})

#------------------------------------------------------------
#-----------------------ReleaseMachine-----------------------
#------------------------------------------------------------
class ReleaseMachineAPI(APIView):

    def get(self, request, pk=''):

        if pk == '':
            releaseMachineTableResult = ReleaseMachine.objects.all()
            serializer = ReleaseMachineTable(releaseMachineTableResult, many=True)
            return Response(serializer.data)

        else:
            releaseMachineTableResult = ReleaseMachine.objects.get(id=pk)
            serializer = ReleaseMachineTable(releaseMachineTableResult)
            return Response(serializer.data)
 
    def post(self, request):

        serializer = ReleaseMachineTable(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()        
        return Response(serializer.data)
    
    def put(self, request, pk=''):

        releaseMachineTableResult = ReleaseMachine.objects.get(id=pk)
        serializer = ReleaseMachineTable(releaseMachineTableResult, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, pk=''):

        releaseMachineTableResult = ReleaseMachine.objects.get(id=pk)       
        releaseMachineTableResult.delete()
        return Response({"msg": "Apagado com sucesso"})

    def patch(self, request, pk):
        releaseMachineTableResult = ReleaseMachine.objects.get(id=pk)
        serializer = ReleaseMachineTable(releaseMachineTableResult, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
class GetReleaseMachineAPI(APIView):

    def get(self, request, pk=''):

        if pk == '':
            releaseMachineTableResult = ReleaseMachine.objects.all()
            serializer = GetReleaseMachineTable(releaseMachineTableResult, many=True)
            return Response(serializer.data)

        else:
            releaseMachineTableResult = ReleaseMachine.objects.get(id=pk)
            serializer = GetReleaseMachineTable(releaseMachineTableResult)
            return Response(serializer.data)


#------------------------------------------------------------
#-----------------------Observation--------------------------
#------------------------------------------------------------
class GetObservationAPI(APIView):

    def get(self, request, pk=''):

        if pk == '':
            ObservationResult = Observation.objects.all()
            serializer = GetObservationTable(ObservationResult, many=True)
            return Response(serializer.data)

        else:
            ObservationResult = Observation.objects.get(id=pk)
            serializer = GetObservationTable(ObservationResult)
            return Response(serializer.data)



class ObservationAPI(APIView):

    def get(self, request, pk=''):

        if pk == '':
            ObservationResult = Observation.objects.all()
            serializer = ObservationTable(ObservationResult, many=True)
            return Response(serializer.data)

        else:
            ObservationResult = Observation.objects.get(id=pk)
            serializer = ObservationTable(ObservationResult)
            return Response(serializer.data)

    def post(self, request):

        serializer = ObservationTable(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()        
        return Response({"msg": "Inserido com sucesso"})
    
    def put(self, request, pk=''):

        ObservationResult = Observation.objects.get(id=pk)
        serializer = ObservationTable(ObservationResult, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, pk=''):

        ObservationResult = Observation.objects.get(id=pk)       
        ObservationResult.delete()
        return Response({"msg": "Apagado com sucesso"})

#------------------------------------------------------------
#-----------------------Login--------------------------------
#------------------------------------------------------------

class LoginAPI(APIView):

    def get(self, request, pk=''):

        if pk == '':
            RequestLoginResult = Login.objects.all()
            serializer = LoginTable(RequestLoginResult, many=True)
            return Response(serializer.data)

        else:
            RequestLoginResult = Login.objects.get(id=pk)
            serializer = LoginTable(RequestLoginResult)
            return Response(serializer.data)


    def post(self, request):

        serializer = LoginTable(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()        
        return Response({"msg": "Inserido com sucesso"})
    
    def put(self, request, pk=''):

        RequestLoginResult = Login.objects.get(id=pk)
        serializer = LoginTable(RequestLoginResult, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, pk=''):

        RequestLoginResult = LoginTable.objects.get(id=pk)       
        RequestLoginResult.delete()
        return Response({"msg": "Apagado com sucesso"})