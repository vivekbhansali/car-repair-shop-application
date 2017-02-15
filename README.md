# car-repair-shop-application
Application for Car Repair Shop to calculate length of service for each mechanic

The application uses Django Framework with MySQL database.

## MySQL Database Settings:
You need to enter the name of database you want to use along with proper username and password.
All the settings can be changed in project/car_repair_shop/settings.py

## Seed File:
The seed file to populate data are
1) workflow_data.txt
2) repair_data.txt

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
