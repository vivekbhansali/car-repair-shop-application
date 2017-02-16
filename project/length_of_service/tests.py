from django.test import TestCase
from .models import Workflow, RepairTypes
import calc

class CalculationTest(TestCase):

	def test_calculations_01(self):
                print '\n ---Test 01--- \n'
		mechanics = ['Bob', 'Peter']
                services = [ Workflow.objects.create(dropoff='12/5/2016', pickup='12/7/2016', mechanic='Bob', repair_type='B'),
                                Workflow.objects.create(dropoff='12/5/2016', pickup='12/6/2016', mechanic='Bob', repair_type='B'),
                                Workflow.objects.create(dropoff='12/5/2016', pickup='12/8/2016', mechanic='Peter', repair_type='A') ]
                national_averages = {'A': 1.0, 'B': 2.0}
                expected_result = ['Bob - B - 2 - 1.0', 'Peter - A - 4 - 0.3']
                actual_result = calc.calculate_length_of_service(mechanics, services, national_averages)

                print 'List of Workflow objects for this Test are'
                print services, '\n'

                print 'National Averages: '
                print sorted(national_averages.items()), '\n'

                print 'Expected Result: ', expected_result
                print 'Actual Result from the function: ', actual_result, '\n'

                self.assertIs( ( sorted(expected_result) == sorted(actual_result) ), True )

	def test_calculations_02(self):
		print '\n ---Test 02--- \n'
		mechanics = ['Larry', 'Bob', 'Peter']
		services = [ Workflow.objects.create(dropoff='12/5/2016', pickup='12/7/2016', mechanic='Bob', repair_type='B'),
				Workflow.objects.create(dropoff='12/5/2016', pickup='12/6/2016', mechanic='Bob', repair_type='B'),
				Workflow.objects.create(dropoff='12/5/2016', pickup='12/7/2016', mechanic='Peter', repair_type='C'),
				Workflow.objects.create(dropoff='12/5/2016', pickup='12/5/2016', mechanic='Larry', repair_type='A'),
				Workflow.objects.create(dropoff='12/5/2016', pickup='12/8/2016', mechanic='Peter', repair_type='A') ]
		national_averages = {'A': 1.0, 'B': 2.0, 'C': 1.0}
		expected_result = ['Bob - B - 2 - 1.0', 'Peter - A - 4 - 0.3', 'Peter - C - 3 - 0.3', 'Larry - A - 1 - 1.0']
		actual_result = calc.calculate_length_of_service(mechanics, services, national_averages)
		
		print 'List of Workflow objects for this Test are'
		print services, '\n'

		print 'National Averages: '
		print sorted(national_averages.items()), '\n'

		print 'Expected Result: ', expected_result	
		print 'Actual Result from the function: ', actual_result, '\n'

		self.assertIs( ( sorted(expected_result) == sorted(actual_result) ), True )

	def test_calculations_03(self):
		print '\n ---Test 03--- \n'
                mechanics = ['Bob', 'Peter', 'Larry', 'Simone']
                services = [ Workflow.objects.create(dropoff='12/5/2016', pickup='12/6/2016', mechanic='Bob', repair_type='B'),
                                Workflow.objects.create(dropoff='12/5/2016', pickup='12/8/2016', mechanic='Larry', repair_type='A'),
                                Workflow.objects.create(dropoff='12/5/2016', pickup='12/8/2016', mechanic='Peter', repair_type='C'),
                                Workflow.objects.create(dropoff='12/6/2016', pickup='12/7/2016', mechanic='Larry', repair_type='A'),
                                Workflow.objects.create(dropoff='12/6/2016', pickup='12/9/2016', mechanic='Simone', repair_type='B'),
				Workflow.objects.create(dropoff='12/7/2016', pickup='12/8/2016', mechanic='Peter', repair_type='C'),
                                Workflow.objects.create(dropoff='12/7/2016', pickup='12/7/2016', mechanic='Simone', repair_type='C'),
                                Workflow.objects.create(dropoff='12/7/2016', pickup='12/9/2016', mechanic='Peter', repair_type='A'),
				Workflow.objects.create(dropoff='12/8/2016', pickup='12/8/2016', mechanic='Simone', repair_type='C'),
                                Workflow.objects.create(dropoff='12/8/2016', pickup='12/9/2016', mechanic='Peter', repair_type='A')  ]
                national_averages = {'A': 1.0, 'B': 2.0, 'C': 1.0}
                expected_result = ['Bob - B - 2 - 1.0', 'Peter - A - 2 - 0.5', 'Peter - C - 3 - 0.3', 'Larry - A - 3 - 0.3', 'Simone - C - 1 - 1.0', 'Simone - B - 4 - 0.5']
		actual_result = calc.calculate_length_of_service(mechanics, services, national_averages)
                
		print 'List of Workflow objects for this Test are'
                print services, '\n'

                print 'National Averages: '
                print sorted(national_averages.items()), '\n'

                print 'Expected Result: ', expected_result
		print 'Actual Result: ', actual_result, '\n'
		
		self.assertIs( ( sorted(expected_result) == sorted(actual_result) ), True )	
