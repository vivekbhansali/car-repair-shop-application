from __future__ import unicode_literals

from django.db import models

# Create your models here.
class RepairTypes(models.Model):
        repair_type = models.CharField(max_length=1)
        description = models.CharField(max_length=30)
        national_averages = models.DecimalField(max_digits=5, decimal_places=1)

        class Meta:
                db_table = "repair_types"

class Workflow(models.Model):
	dropoff = models.CharField(max_length=30)
	pickup = models.CharField(max_length=30)
	mechanic = models.CharField(max_length=30)
	repair_type = models.CharField(max_length=1)

	def __str__(self):
        	s = str(self.dropoff + ',' + self.pickup + ',' + self.mechanic + ',' + self.repair_type)
		return s + '\n'

	class Meta:
		db_table = "shop_workflow_fact"

