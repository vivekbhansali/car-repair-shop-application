# car-repair-shop-application
Application for Car Repair Shop to calculate length of service for each mechanic

The application uses Django Framework with MySQL database.

## MySQL Database Settings:
You need to enter the name of database you want to use along with proper username and password.

All the settings can be changed in project/car_repair_shop/settings.py

## Seed File:
The seed file to populate data are <br />
1. workflow_data.txt <br />
2. repair_data.txt

### Command to populate the data into database
```
mysql db_name < workflow_data.txt -u username -p password
mysql db_name < repair_data.txt -u username -p password
```

## To run the application:
(You can change the ip-address and port number if you want)
```
python manage.py runserver 0.0.0.0:80
```
On your browser, you can go visit the entry point('Landing Page') for the application at,
```
0.0.0.0:80/length-of-service
```

To check the result, goto:
```
0.0.0.0:80/length-of-service/get-all-results
```
![](https://raw.githubusercontent.com/vivekbhansali/car-repair-shop-application/master/output.png =300X350)

## Test Cases
There are 3 test cases in length-of-service/tests.py file

To run a all test cases,
```
python manage.py test length_of_service.tests.CalculationTest
```

To run a particular test case,
```
python manage.py test length_of_service.tests.CalculationTest.test_calculations_01
```
OUTPUT:
```
Creating test database for alias 'default'...

 ---Test 01--- 

List of Workflow objects for this Test are
[<Workflow: 12/5/2016,12/7/2016,Bob,B
>, <Workflow: 12/5/2016,12/6/2016,Bob,B
>, <Workflow: 12/5/2016,12/8/2016,Peter,A
>] 

National Averages: 
[('A', 1.0), ('B', 2.0)] 

Expected Result:  ['Bob - B - 2 - 1.0', 'Peter - A - 4 - 0.3']
Actual Result from the function:  ['Bob - B - 2 - 1.0', 'Peter - A - 4 - 0.3'] 

.
----------------------------------------------------------------------
Ran 1 test in 0.015s

OK
Destroying test database for alias 'default'...
```
