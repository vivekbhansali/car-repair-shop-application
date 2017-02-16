from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse
from .models import Workflow, RepairTypes
from collections import defaultdict
from django.template import loader

def calculate_length_of_service(mechanics, services, n_average_records):
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
