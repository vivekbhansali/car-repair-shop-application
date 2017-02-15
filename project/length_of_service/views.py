from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse
from .models import Workflow, RepairTypes
from collections import defaultdict
from django.template import loader

def calculate_length_of_service(request):
	mechanics =  Workflow.objects.values_list('mechanic', flat=True).distinct()
	types = RepairTypes.objects.values_list('repair_type', flat=True)
	national_averages = RepairTypes.objects.values_list('national_averages', flat=True)
	result = []
	n_average_records = {}
	for rtype, avg in zip(types, national_averages):
		n_average_records[rtype] = avg
	services = Workflow.objects.all()
	for mechanic in mechanics:
		mechanic = mechanic.strip()
		sum_records = defaultdict(int)
		count_records = defaultdict(int)
		for service in services:
			s = str(service).split(",")
			name = s[2].strip()
			if name == mechanic:
				repairType = s[3].strip()
				sum_records[repairType] += (abs(datetime.strptime(s[0], '%m/%d/%Y') - datetime.strptime(s[1], '%m/%d/%Y')).days + 1)
				count_records[repairType] += 1
		
		for types in sum_records:
			avg = sum_records[types]/count_records[types]
			ratio_of_avgs = round(float(n_average_records[types]/avg),1)
			m = str(mechanic + ' - ' + types + ' - ' + str(avg) + ' - ' + str(ratio_of_avgs))
			result.append(m)

	template = loader.get_template('length_of_service/index.html')
	context = {'result_list': result,}
	return HttpResponse(template.render(context, request))

def index(request):
	return HttpResponse('Welcome to LOS Application!')
