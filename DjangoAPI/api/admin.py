from django.contrib import admin
from .models import *

class detReleaseMachine(admin.ModelAdmin):
    list_display = ('id', 'date', 'InitialHour', 'FinishHour','description', 'idMachineFK','idAssociateFK', 'examA', 'examB', 'result')
    list_display_links = ('id',)
    search_fields = ('idMachineFK','idAssociateFK',)
    list_per_page = 10

admin.site.register(ReleaseMachine, detReleaseMachine)

class detAssociate(admin.ModelAdmin):
    list_display = ('id', 'name', 'EDV', 'id_card', 'skill', 'skill2', 'adminU', 'jobposition')
    list_display_links = ('id',)
    search_fields = ('EDV',)
    list_per_page = 10

admin.site.register(Associate, detAssociate)

class detMachine(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'status', 'ipaddress', 'statusMaint')
    list_display_links = ('id',)
    search_fields = ('name',)
    list_per_page = 10

admin.site.register(Machine, detMachine)

class detQuestion(admin.ModelAdmin):
    list_display = ('id', 'type')
    list_display_links = ('id',)
    search_fields = ('type',)
    list_per_page = 10

admin.site.register(Question, detQuestion)

class detGreenBook(admin.ModelAdmin):
    list_display = ('id', 'idMachineFK', 'typeQuestion','question')
    list_display_links = ('id',)
    search_fields = ('idMachineFK',)
    list_per_page = 10

admin.site.register(GreenBook, detGreenBook)

class detMaintenance(admin.ModelAdmin):
    list_display = ('id', 'date', 'Initialhour','Finishhour','idMachineFK', 'idAssociateFK', 'statusMaint')
    list_display_links = ('id',)
    search_fields = ('idMachineFK',)
    list_per_page = 10

admin.site.register(Maintenance, detMaintenance)

class detObservation(admin.ModelAdmin):
    list_display = ('id', 'date', 'hour','idMachineFK', 'idAssociateFK')
    list_display_links = ('id',)
    search_fields = ('idMachineFK',)
    list_per_page = 10

admin.site.register(Observation, detObservation)

class detAreas(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id',)
    search_fields = ('name',)
    list_per_page = 10

admin.site.register(Areas, detAreas)

class detLogin(admin.ModelAdmin):
    list_display = ('id', 'name', 'edv', 'idAreaFK')
    list_display_links = ('id',)
    search_fields = ('name',)
    list_per_page = 10

admin.site.register(Login, detLogin)

class detJobPosition(admin.ModelAdmin):
    list_display = ('id', 'typeJob',)
    list_display_links = ('id',)
    search_fields = ('typeJob',)
    list_per_page = 10

admin.site.register(JobPosition, detJobPosition)