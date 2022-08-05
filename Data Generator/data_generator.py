##### DATA GENERATOR #####
# AUTHOR: Leslie A. McFarlin, Principal UX Architect @ Wheels-Donlen
# CREATE DATE: 25 Feb 2022

# DESC: data_generator is a python program to generate random data sets for use in UX prototypes.
#       It automatically generates company, fleet, vehicle, and driver details.
#       Users need to include the following information: 
#       Number of companies, country/ies, number of fleets, number of records needed

### IMPORTS ###
# Generate data frame
import pandas as pd

# Random numbers as needed
import random

# Random names
import random_names as rn

# Assist with string functionality
import string as st

##### USER INPUTS #####
# User inputs will serve as global variables accessible to all within the program
# Number of records to create
records_count = int(input('How many vehicles do you need?:'))

# Number of fleets to create
fleet_count = input('Should there be multiple fleets? [Y/N]:').lower()

# Country/ies company/ies should be in
country = input('Which countries should the fleet(s) be in? [Canada, US, both]:').lower()

##### HOLD THE USER OUTPUTS #####
# Add the necessary values from user inputs to start
data = {'Country': country,
        'Fleet Size': records_count}


##### RETURN COMPANY DETAILS #####   
# Get the country of the company
def getName():
    # If the US
    if data['Country'] == 'us':
        name = "ABC Corp"
    # If Canada
    elif data['Country'] == 'canada':
        name = "Can Corp"
    # Return the company's country
    elif data['Country'] == 'both':
        name = "Client-Corp"
    else:
        # Invalid 
        print('Please specify the US, Canada, or both.')
    # Add company name to the dictionary
    data['Company']=name

    
##### RETURN ASPECTS OF THE FLEET #####
# Produce a fleet ID based on the country
def getFleetID():
    # Get the company name
    company_name = data.get('Company')
    # Get how many fleet IDs to generate dynamically
    fleet_id_counter = records_count//5
    # Cap the total number of fleets at 7 to reflect reality
    if fleet_id_counter > 7:
        fleet_id_counter = 7
    else:
        # Do nothing
        pass
    # Hold dynamically generated fleet ID letter strings
    id_strings = []
    # Actual Fleet IDs
    fleet_id = []
    ### Generate Fleet IDs ###
    # If floor value is 0 or 1
    if (fleet_id_counter <= 2):
        # US
        if company_name == 'ABC Corp':
            fleet_id.append('3ABC')
        # Canada
        elif company_name == 'Can Corp':
            fleet_id.append('7XYZ')
        # International
        elif company_name == 'Client-Corp':
            fleet_id.extend(['3AAA', '7AAA'])
        # Can't find company name
        else:
            print('No company name found.')
    # If floor value is greater than 1
    else:   
        # Generate 3-alpha strings
        f = 1
        while f <= fleet_id_counter:
            # Generate a random 3-alpha string
            id_strings.append("".join(random.choices(st.ascii_uppercase, k=3)))
            # Increment f
            f += 1
        # Country prefixes
        us_prefix = '3'
        can_prefix = '7'
        # US
        if country == 'us':
            fleet_id = [us_prefix+i for i in id_strings]
        # Canada
        elif country == 'canada':
            fleet_id = [can_prefix+i for i in id_strings]
        # International
        elif country == 'both':
            # Proportion is skewed toward US fleet membership because of current client composition
            us_fleet_count = int(round(fleet_id_counter*0.75, 0))
            # US Fleet IDs
            fleet_id = [us_prefix+i for i in id_strings[:us_fleet_count]]
            # Canadian Fleet IDs
            fleet_id.extend([can_prefix+i for i in id_strings[us_fleet_count:]])
        # Can't find country name
        else:
            print('No country specified.')
    # Add to the dictionary
    data['Fleet ID']=fleet_id
    
# Get the size of each fleet
def fleetSize():
    # Total records to generate
    total_vehicles = data['Fleet Size']
    # Number of fleets
    fleet_count = len(data['Fleet ID'])
    # Floor division to capture the base count per fleet
    base_fleet_size = total_vehicles//fleet_count
    # Find the difference between total_vehicles and base_fleet_size
    extra_fleet_size = total_vehicles-(fleet_count*base_fleet_size)
    # Randomly pick a fleet ID to have count + extra_fleet_size
    rand_fleet_id = data['Fleet ID'][random.randint(0, fleet_count-1)]
    # Create a size variable per Fleet_ID
    for id in data['Fleet ID']:
        # Create a key in the dictionary for each fleet ID
        data[id] = {}
        # For the fleet IDs not absorbing extra vehicle count
        if id != rand_fleet_id:
            data[id].update({'Size': base_fleet_size})
        # For the randomly chosen fleet ID
        else:
            data[id].update({'Size': base_fleet_size + extra_fleet_size})     
        
        
##### RETURN ASPECTS OF DIVISION #####
# Generate components of a division id
def divComponents():
    # Uppercase letters
    letters = st.ascii_uppercase
    # Integers
    numbers = st.digits
    # Generate parts
    pt2 = ''.join(random.choice(letters) for x in range(2)) 
    pt3 = str(''.join(random.choice(numbers) for x in range(6))) 
    pt4 = str(''.join(random.choice(numbers) for x in range(4)))
    # Return component parts
    return pt2, pt3, pt4

# Produce a division id
def getDivisionID():
    # Create Division IDs for each Fleet ID
    for id in data['Fleet ID']:
        # Division ID list
        division_id=[]
        # Get the size of the fleet
        this_size = data[id]['Size']
        # If count per fleet is 10 or less, only one division id
        if (this_size//10 <= 1):
            # Generate the component parts
            div_id_pt2, div_id_pt3, div_id_pt4 = divComponents()
            division_id.append(id + ":" + div_id_pt2 + ":" + div_id_pt3 + ":" + div_id_pt4)
         # New division id for every 10 vehicles
        elif (this_size//10 > 1):
            extra_divisions = this_size//10
            for e in range(0, extra_divisions):
                # Generate the component parts
                div_id_pt2, div_id_pt3, div_id_pt4 = divComponents()
                division_id.append(id + ":" + div_id_pt2 + ":" + div_id_pt3 + ":" + div_id_pt4)
        # Do nothing
        else:
            pass
        # Add the division id
        data[id].update({'Division ID': division_id})

##### RETURN ASPECTS OF A VEHICLE #####
# Generate a vehicle ID
def getVehicleID():
    # Randomly generate a vehicle ID
    vehicle_id = [(''.join(random.choice(st.ascii_uppercase + str(st.digits)) for x in range(6))) for i in range(0, data['Fleet Size'])]
    data.update({'Vehicle ID': vehicle_id})

# Generate a VIN
def getVIN():
    # Randomly generate a VIN
    vin = [(''.join(random.choice(st.ascii_uppercase + str(st.digits)) for x in range(17))) for i in range(0, data['Fleet Size'])]
    data.update({'VIN': vin})
    
# Generate a license plate
def getPlates():
    plate_number = [(''.join(random.choice(st.ascii_uppercase + str(st.digits)) for x in range(6))) for i in range(0,data['Fleet Size'])]
    data.update({'License Plate': plate_number})
    
# Generate a vehicle description - FUTURE ADDITION
def getVehicleDesc():
    # Holding vehicles
    make_list = []
    model_list = []
    year_list = []
    # Create vehicle records according to record counts
    for i in range(0,data['Fleet Size']):
        # Return vehicle and year
        vehicle, year = rn.makeModelYear()
        # Split the vehicle to get make and model
        vehicle_string = vehicle.split(" ", 1)
        # Manufacturer
        make = vehicle_string[0]
        # Model
        model = vehicle_string[1]
        # Add to vehicle lists
        make_list.append(make)
        model_list.append(model)
        year_list.append(year)
    # Updata data
    data.update({'Make': make_list})   
    data.update({'Model': model_list})
    data.update({'Year': year_list})

##### RETURN ASPECTS OF A DRIVER #####

# Generate a name
def getDriverName():
    # Hold first names
    first_name_list=[]
    # Hold last names
    last_name_list=[]
    for i in range(0, data['Fleet Size']):
        # Randomly generate a first name
        first_name=rn.firstName()
        # Add first names
        first_name_list.append(first_name.strip())
        # Randomly generate a last name
        last_name=rn.lastName()
        # Add last names
        last_name_list.append(last_name.strip())
    # Add to data
    data.update({'First Name': first_name_list})
    data.update({'Last Name': last_name_list})
    
# Create emails for drivers
def getEmails():
    # Get first and last names
    first_name_list = data['First Name']
    last_name_list = data['Last Name']
    # Create - convert to lower case
    company_domain = "-".join(data['Company'].lower().split(" "))+".com"
    # Create the ID
    email_id = []
    for i,k in zip(first_name_list, last_name_list):
        email_id.append(i + "." + k)
    # Create the email addresses
    email_addr = [i+"@"+company_domain for i in email_id]
    # Add to data
    data.update({'Email Address': email_addr})
    
# Create phone numbers
def getPhoneNumbers():
    # List to hold phone numbers
    phone_number = []
    for i in range(0, data['Fleet Size']):
        # Area code
        area_code = str(random.randint(100,999))
        # Prefix
        prefix = str(random.randint(100,999))
        # Line number
        line_number = [(''.join(random.choice(str(st.digits)))) for i in range(0,4)]
        line_number_str = ''.join(map(str, line_number))
        # Create the number
        phone_number.append(area_code + "-" + prefix + "-" + line_number_str)
    # Add to data
    data.update({'Phone Number': phone_number})
    
# Generate a driver ID
def getDriverID():
    # Randomly generate a driver ID
    driver_id = [(''.join(random.choice(st.ascii_uppercase + str(st.digits)) for x in range(5))) for i in range(0, data['Fleet Size'])]
    data.update({'Driver ID': driver_id})

##### RETURN LOCATION INFORMATION #####

# City and State or Province information
def getCityInfo():
    # For US
    if data['Country'] == 'us':
        # City and state
        state, city, zipcode = rn.cityState()
        # Add to the dictionary
        data.update({'City': city})
        data.update({'State': state})
        data.update({'Zip': zipcode})
    # For Canada
    elif data['Country'] == 'canada':
        # Generate state and city pairing
        province, city, postal_code = rn.cityProvince()
         # Add to the dictionary
        data.update({'City': city})
        data.update({'Province': province})
        data.update({'Postal Code': postal_code})
    # For both
    elif data['Country'] == 'both':
        # City and state
        state, us_city, zipcode = rn.cityState()
        # Generate state and city pairing
        province, can_city, postal_code = rn.cityProvince()
        # Add to the dictionary
        data.update({'City': [us_city, can_city]})
        data.update({'State': state})
        data.update({'Province': province})
        data.update({'Zip': zipcode})
        data.update({'Postal Code': postal_code})
    # Else
    else:
        print('No country found. Restart the program and try again.')
        
# Generate a street address
def getAddress():
    # Address list
    addr_list = []
    # Generate one unique address per vehicle
    for i in range(0, data['Fleet Size']):
        start = 2
        end = 6
        addr_size = random.randint(start, end)
        # For rural addresses
        if addr_size == 6:
            num_pt1 = ''.join(random.choices(str(st.digits), k=2))
            dir = random.choice(['N', 'S', 'E', 'W', 'NW', 'NE', 'SW', 'SE'])
            num_pt2 = ''.join(random.choices(str(st.digits), k=3))
            this_addr = num_pt1+dir+num_pt2
        # For non-rural addresses
        else:
            this_addr = ''.join(random.choices(str(st.digits), k=addr_size))
        # Generate a street name
        street_name = rn.streetNames()
        full_address = this_addr + " " + street_name
        # Add to list
        addr_list.append(full_address)
    # Add to dictionary
    data.update({'Address': addr_list})
    
##### COMPILE A DATAFRAME #####
# Fleet IDs and Division IDs are repeated their specific number of times within a data set
# For international companies, city, state/province, and zip/postal code must match up with Fleet IDs and Division IDs

# Lists for dataframe
data_fleet_ids = [] # Fleet IDs
data_division_ids = [] # Division IDs per Vehicle ID
data_city = [] # City
data_SP = [] # State and/or Province
data_ZP = [] # Zip and/or Postal Code

# Add Fleet IDs
def fleetBuilder():
    # Individual fleets
    for id in data['Fleet ID']:
        # How many vehicles with this fleet ID
        id_size = data[id]['Size']
        for i in range(0,id_size):
            data_fleet_ids.append(id)
            

# Add Division IDs
def divisionBuilder():
    # Use the Vehicle IDs to govern iteration
    for id in data_fleet_ids:
        # For each Division ID
        for div in data[id]['Division ID']:
            # Match exists
            if id == div.split(':')[0]:
                # Add to Division ID list
                data_division_ids.append(div)
            # No match
            else:
                # Do nothing
                continue

# Add City, State/Province, and Zip/Postal Code
def locationBuilder():
    # Single cities
    if isinstance(data['City'], str):
        # Use the Vehicle IDs to govern iteration
        for id in data_fleet_ids:
            data_city.append(data['City'])
            if id.startswith('3'):
                data_SP.append(data['State'])
                data_ZP.append(data['Zip'])
            elif id.startswith('7'):
                data_SP.append(data['Province'])
                data_ZP.append(data['Postal Code'])
    # Multiple cities
    elif isinstance(data['City'], list):
        for id in data_fleet_ids:
            if id.startswith('3'):
                data_city.append(data['City'][0])
                data_SP.append(data['State'])
                data_ZP.append(data['Zip'])
            elif id.startswith('7'):
                data_city.append(data['City'][1])
                data_SP.append(data['Province'])
                data_ZP.append(data['Postal Code'])


##### MAIN FUNCTION #####
def main():
    # Company name
    getName()
    # Fleet IDs
    getFleetID()
    # Fleet sizes
    fleetSize()
    # Division IDs
    getDivisionID()
    # Vehicle IDs
    getVehicleID()
    # VIN
    getVIN()
    # License Plates
    getPlates()
    # Make, model, and year
    getVehicleDesc()
    # Driver Names
    getDriverName()
    # Emails
    getEmails()
    # Phone Numbers
    getPhoneNumbers()
    # Driver IDs
    getDriverID()
    # City and State/Province information
    getCityInfo()
    # Street address information
    getAddress()
    ### BUILD THE FINAL DATA SET ###
    # Build the Vehicle ID list
    fleetBuilder()
    # Build the Division ID list
    divisionBuilder()
    # Build the location set
    locationBuilder()
    
##### Execute main #####
main()

##### GENERATE AN EXCEL FILE #####
# Create a dictionary
results = {'Vehicle ID': data['Vehicle ID'],
           'Make': data['Make'],
           'Model': data['Model'],
           'Year': data['Year'],
           'VIN': data['VIN'],
           'License Plate': data['License Plate'],
           'Fleet ID': data_fleet_ids,
           'Division ID': data_division_ids,
           'First Name': data['First Name'],
           'Last Name': data['Last Name'],
           'Email Address': data['Email Address'],
           'Phone Number': data['Phone Number'],
           'Driver ID': data['Driver ID'],
           'Address': data['Address'],
           'City': data_city,
           'State/Prov': data_SP,
           'Zip/Postal': data_ZP}

# Create a dataframe
results_df = pd.DataFrame(data=results)

results_df.to_csv('prototype_fleet_data.csv', index=False)
