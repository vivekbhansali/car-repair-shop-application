# Car Repair Shop Application
Application to calculate length of service (LOS) for cars in a Car Repair Shop.

The application uses Python Django Framework with MySQL database.

## MySQL Database Settings:
You need to enter the name of database you want to use along with proper username and password.

All the settings can be changed in *project/car_repair_shop/settings.py*

## Seed File:
The seed file to populate data are,

1. workflow_data.sql
2. repair_data.sql

### Command to populate the data into database
```
mysql db_name < workflow_data.sql -u username -p
mysql db_name < repair_data.sql -u username -p
```

## To run the application:
(You can change the *ip-address* and *port* if you want)
```
python manage.py runserver 0.0.0.0:80
```
On your browser, you can visit the entry point('Landing Page') of the application at,
```
0.0.0.0:80/length-of-service
```
There are two types of Sorting provided,

1. Length of services sorted by Mechanics
   ```
   0.0.0.0:80/length-of-service/results-by-mechanics
   ```
   <img src="https://raw.githubusercontent.com/vivekbhansali/car-repair-shop-application/master/output1.png" width="450" height="500">

2. Length of service sorted by Repair Types
   ```
   0.0.0.0:80/length-of-service/results-by-repair-type
   ```

## Testing the Application:
There are Five test cases in *length-of-service/tests.py* file

1. Three test cases check Length of services calculations:
   ```
   python manage.py test length_of_service.tests.CalculationTest
   ```

2. Two test cases check connections on Views
   ```
   python manage.py test length_of_service.tests.ViewsTest
   ```

3. To run a all test cases
   ```
   python manage.py test
   ```

4. Running a Sample Test Case
   ```
   python manage.py test length_of_service.tests.CalculationTest.test_calculations_01
   ```
   **OUTPUT:**
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
