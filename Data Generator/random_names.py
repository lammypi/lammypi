##### RANDOM NAMES #####
# AUTHOR: Leslie A. McFarlin, Principal UX Architect @ Wheels-Donlen
# CREATE DATE: 30 July 2022

# DESC: random_names randomly generates the following:
#       - first and last names
#       - US City and State combinations
#       - Canadian City and Province combinations
#       - Vehicle manufacturer and model combinations

# Imports
import os
import pandas as pd
import random
import string as st
from datetime import date


# Access .txt files - THESE MIGHT NEED TO BE UPDATED
first_names = pd.read_csv("first_name.txt", header=None)
last_names = pd.read_csv("last_name.txt", header=None)
can_provinces = pd.read_csv("can_provinces.txt", sep=",", header=None)
us_states = pd.read_csv("us_states.txt", sep=",", header=None)
street_names = pd.read_csv("street_names.txt", header=None)
vehicle_names = pd.read_csv("vehicles.txt", header=None)

##### RESOURCE PATH OF FILES #####

##### RETURN RANDOM NAMES #####

# First Name
def firstName():
    # Start value- adjust if needed
    start = 0
    # End value- dynamic to the number of names in the dataframe 
    # Don't adjust in case of file updates
    end = first_names.shape[0]-1
    # Get the random first name
    first_name_random = first_names[0][random.randint(start, end)]
    return first_name_random

# Last Name
def lastName():
    # Start value- adjust if needed
    start = 0
    # End value- dynamic to the number of names in the dataframe 
    # Don't adjust in case of file updates
    end = last_names.shape[0]-1
    # Get the random lasst name
    last_name_random = last_names[0][random.randint(start, end)]
    return last_name_random


##### RETURN RANDOM LOCATION NAMES #####

# US City and State
def cityState():
    # Start value- adjust if needed
    start = 0
    # End value- dynamic to the number of items in the dataframe 
    # Don't adjust in case of file updates
    end = us_states.shape[0]-1
    # Get the random integer
    idx = random.randint(start, end)
    # Get the random city + state combo
    state = us_states[0][idx]
    city = us_states[1][idx]
    zipcode = str(us_states[2][idx])
    # Return city, state, zip
    return state, city, zipcode

# Canadian City and Province
def cityProvince():
    # Start value- adjust if needed
    start = 0
    # End value- dynamic to the number of items in the dataframe 
    # Don't adjust in case of file updates
    end = can_provinces.shape[0]-1
    # Get the random integer
    idx = random.randint(start, end)
    # Get the random city + prov combo
    province = can_provinces[0][idx]
    city = can_provinces[1][idx]
    postal_code = can_provinces[2][idx]
    # Return city and province
    return province, city, postal_code

# Streets
def streetNames():
    # Types of thoroughfares
    thoroughfares = ['Rd.', 'St.', 'Ave.', 'Pkwy.', 'Hwy.', 'Ln.']
    # Start value- adjust if needed
    start = 0
    # End values- dynamic to the number of items in the dataframe 
    # Don't adjust in case of file updates
    end_tfares = len(thoroughfares)-1
    end_street = street_names.shape[0]-1
    # Pick a street type at random
    street_type = thoroughfares[random.randint(0, end_tfares)]
    # Pick a street name at random
    street_name = street_names[0][random.randint(start, end_street)]
    # Create the full name
    full_street = street_name  + " " + street_type
    # Return
    return full_street

# Vehicles
def makeModelYear():
    # Start value- adjust if needed
    start = 0
    # End value- dynamic to the number of items in the dataframe
    v_end = vehicle_names.shape[0]-1
    # Random index value
    v_idx = random.randint(start, v_end)
    # Get a vehicle
    vehicle = vehicle_names[0][v_idx]
    # Get a year
    current_year = int(date.today().year)
    # Previous years - up to 3 years back
    prev_year_boundary = current_year - 3
    # Year range
    year = random.randint(prev_year_boundary, current_year)
    # Return
    return vehicle, year
    
    