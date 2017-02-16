from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse
from .models import Workflow, RepairTypes
from collections import defaultdict
from django.template import loader

def calculate_length_of_service_by_mechanic(mechanics, services, n_average_records):
        result = []
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
                        ratio_of_avgs = round(float(float(n_average_records[types]/avg)),1)
                        m = str(mechanic + ' - ' + types + ' - ' + str(avg) + ' - ' + str(ratio_of_avgs))
                        result.append(m)

        return result

def calculate_length_of_service_by_repair_type(types, services, n_average_records):
        result = []
        for repair_type in types:
                repair_type = repair_type.strip()
		mechanics = []
                sum_records = defaultdict(int)
                count_records = defaultdict(int)
                for service in services:
                        s = str(service).split(",")
                        repair = s[3].strip()
                        if repair == repair_type:
                                mechanic = s[2].strip()
				mechanics.append(mechanic)
                                sum_records[mechanic] += (abs(datetime.strptime(s[0], '%m/%d/%Y') - datetime.strptime(s[1], '%m/%d/%Y')).days + 1)
                                count_records[mechanic] += 1

                for mechanic in sum_records:
                        avg = sum_records[mechanic]/count_records[mechanic]
                        ratio_of_avgs = round(float(float(n_average_records[repair_type]/avg)),1)
                        m = str(mechanic + ' - ' + repair_type + ' - ' + str(avg) + ' - ' + str(ratio_of_avgs))
                        result.append(m)
        
	return result
