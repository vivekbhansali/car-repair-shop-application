from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Workflow, RepairTypes
import calc

def length_of_service(request):
	result = []
        n_average_records = {}

	mechanics =  Workflow.objects.values_list('mechanic', flat=True).distinct()
	types = RepairTypes.objects.values_list('repair_type', flat=True)
	national_averages = RepairTypes.objects.values_list('national_averages', flat=True)
	services = Workflow.objects.all()
	for rtype, avg in zip(types, national_averages):
		n_average_records[rtype] = avg

	result = calc.calculate_length_of_service(mechanics, services, n_average_records)
	
	template = loader.get_template('length_of_service/index.html')
	context = {'result_list': result,}
	return HttpResponse(template.render(context, request))

def index(request):
	return HttpResponse('Welcome to LOS Application!')
