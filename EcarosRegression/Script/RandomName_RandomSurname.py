import random
import csv
import os     
        

def generate_random_name():
    first_names = ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'Grace', 'Henry', 'Isabella', 'Jack', 'Katherine', 'Liam', 'Mia', 'Noah', 'Olivia', 'Peter', 'Quinn', 'Rachel', 'Samuel', 'Taylor', 'Ursula', 'Victor', 'Wendy', 'Xander', 'Yasmine', 'Zane']
   
    random_first_name1 = random.choice(first_names)
    random_first_name2 = random.choice(first_names)

    random_firstName = f"{random_first_name1} {random_first_name2}"
    return random_firstName
    Log.Message(f"Random First name: {random_firstName}")


def generate_random_surname():
    last_names = ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Taylor', 'Anderson', 'Thomas', 'Jackson', 'White', 'Harris', 'Martin', 'Thompson', 'Garcia', 'Martinez', 'Robinson', 'Clark', 'Rodriguez', 'Lewis', 'Lee', 'Walker', 'Hall', 'Allen']

    random_last_name1 = random.choice(last_names)
    random_last_name2 = random.choice(last_names)

    random_lastName = f"{random_last_name1} {random_last_name2}"
    return random_lastName
    Log.Message(f"Random Last name: {random_lastName}")


    
def generate_random_chassis():
  file_name= "_SELECT_cbm_MANUFACTURERCODE_b_BRANDCODE_b_DESCRIPTION_FROM_CHAS_202407121251.csv"
  file_path = os.path.join(Project.Path,"Stores","Files" ,file_name)  #Stores files should not be needed....Still working on it
  corrected_path=file_path.replace('\\','/')
  with open(corrected_path) as csvfile: 
    reader=csv.reader(csvfile, delimiter=',',)
    selected= random.choice(list(reader))
    brand=selected[2]
    idcode=selected[0]
    print(idcode,brand)
    ran= str(random.randrange(10000000,99999999))
    chassis=selected[0]+ran
    return chassis,brand    
    
    
        
def random_license():
    license=str(random.randrange(100000,999999))
    return license    
    
    
def setProjectVariables():
    Project.Variables.random_FirstName = generate_random_name();
    Project.Variables.random_LastName = generate_random_surname();
    Project.Variables.random_ChassisNumber , Project.Variables.random_Brand  = generate_random_chassis();
    Project.Variables.random_License  = random_license();
    Log.Message("Random First Name: " + Project.Variables.random_FirstName)
    Log.Message("Random Last Name: " + Project.Variables.random_LastName)
    Log.Message("Random Chassis Number: " + Project.Variables.random_ChassisNumber)
    Log.Message("Random Brand: " + Project.Variables.random_Brand)
    Log.Message("Random License " + Project.Variables.random_License)

