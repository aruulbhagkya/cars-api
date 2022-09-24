import requests
URL = "http://127.0.0.1:5000/cars"
username='jack'
password='qxf2'
my_session = requests.Session()

# Get a list of cars
response = requests.get(url='http://127.0.0.1:5000/cars',auth=(username,password))
print(response.text)

#Get the list of users
response = requests.get(url='http://127.0.0.1:5000/cars/filter/hatchback',auth=(username,password))
print(response.text)

# Get registered cars
response = requests.get(url='http://127.0.0.1:5000/register',auth=(username,password))
print(response.text)

#  Get cars by name
response = requests.get(url='http://127.0.0.1:5000/cars/Swift',auth=(username,password))
print(response.text)

#Cars present before you add a new car
response = my_session.get(url='http://127.0.0.1:5000/cars',auth=(username,password))
cars_before_add = response.json()
print(f'Cars present before adding a new car: {cars_before_add}')

#Make the POST to add a new car
response = my_session.post(url='http://127.0.0.1:5000/cars/add',json={'name':'figo','brand':'Ford','price_range':'2-3lacs','car_type':'hatchback'},auth=(username,password))
print(response.text)

#Cars present after you added a new car
response = my_session.get(url='http://127.0.0.1:5000/cars',auth=(username,password))
cars_after_add = response.json()
print(f'Cars present after adding a new car: {cars_after_add}')

# Register a car
response = requests.post(url='http://127.0.0.1:5000/register/car',params={'car_name':'figo','brand':'Ford'},json={'customer_name': 'Unai Emery','city': 'London'},auth=(username,password))
print(response.text)

#  Update a car
response = requests.post(url='http://127.0.0.1:5000/cars/add',json={'name':'figo','brand':'Ford','price_range':'2-3lacs','car_type':'hatchback'},auth=(username,password))
print(response.text)

# Delete a car
response = requests.delete(url='http://127.0.0.1:5000/register/cars/remove/City',auth=(username,password))
print(response.text)

#  Delete first entry in car registration list
response = requests.delete(url='http://127.0.0.1:5000/register/car/delete',auth=(username,password))
print(response.text)
                    
