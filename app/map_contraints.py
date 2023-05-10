# Import the ValidationError class from wtforms.validators
from wtforms.validators import ValidationError
from app.models import Vendor
import re

# list of valid locations on the vendor map. 0 represents 'filler'
map_locations = [128, 0, 115, 116, 0, 119, 120, 0, 123, 124, 0, 0, 126, 0, 113, 114, 0, 117, 118, 0, 121, 122, 0, 0, 126, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 125, 0, 103, 104, 0, 107, 108, 0, 111, 112, 0, 0, 0, 0, 101, 102, 0, 105, 106, 0, 109, 110, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 88, 0, 91, 92, 0, 95, 96, 0, 99, 100, 0, 0, 0, 0, 89, 90, 0, 93, 94, 0, 97, 98, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 86, 0, 0, 0, 76, 0, 79, 80, 0, 83, 84, 0, 85, 0, 0, 0, 75, 0, 77, 78, 0, 81, 82, 0, 0, 46, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 45, 0, 65, 66, 0, 69, 70, 0, 73, 74, 0, 0, 44, 0, 63, 64, 0, 67, 68, 0, 71, 72, 0, 50, 43, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 49, 42, 0, 53, 54, 0, 57, 58, 0, 61, 62, 0, 48, 41, 0, 51, 52, 0, 55, 56, 0, 59, 60, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 31, 32, 0, 35, 36, 0, 39, 40, 0, 15, 10, 0, 29, 30, 0, 33, 34, 0, 37, 38, 0, 14, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13, 8, 0, 19, 20, 0, 23, 24, 0, 27, 28, 0, 12, 7, 0, 17, 18, 0, 21, 22, 0, 25, 26, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 5, 4, 3, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# list of tuples of valid vertically adject posistions on the vendor map
wall_booths = [(128, 126), (126, 125), (86, 85), (46, 45), (45, 44), (44, 43), (43, 42), (42, 41), (50, 49), (49, 48), (15, 14), (14, 13), (13, 12), (10, 9), (9, 8), (8, 7)]

# Define a function to remove all spaces of boothLoc
def get_clean_boothLoc(boothLoc):
        # Remove any whitespace
    boothLoc = boothLoc.strip()
    # Replace any instances of multiple commas with a single comma
    boothLoc = re.sub(r',+', ',', boothLoc)
    # Remove any commas at the beginning or end of the string
    boothLoc = boothLoc.strip(',')
    # Remove any commas that are not followed by a number
    boothLoc = re.sub(r',(?!\d)', '', boothLoc)
    return boothLoc

# Define a function that checks if entered booth locations are adjecent horizontally
def check_loc(user_booth1, user_booth2):
    # Check if both user inputs are in the list of map locations
    if user_booth1 == 0 or user_booth2 == 0 or not all(loc in map_locations for loc in (user_booth1, user_booth2)):
        return False

    # Get the indices of the user inputs in the list
    index1, index2 = map_locations.index(user_booth1), map_locations.index(user_booth2)

    # Check if the absolute difference between the indices is less than or equal to 1
    if abs(index1 - index2) <= 1:
        return True
    
    return False

# Define a function to validate booth locations
def validate_boothLoc(form, field):
    # Get a list of booth locations from the field data and remove any whitespace
    boothLoc = get_clean_boothLoc(field.data)
    validate_not_empty(boothLoc)
    if not all(char.isdigit() or char == ',' for char in boothLoc):
            raise ValidationError('Booth Location can only contain numbers and commas. No spaces. Please enter Booth Location in the form: #,#')

    #boothLoc = field.data
    booth_list = boothLoc.split(",")

    # Check if booth(s) entered are in map_locations
    booth_set = set()
    for loc in booth_list:
        if int(loc) not in map_locations:
            raise ValidationError(f"Booth Location {loc} is not a valid location.")
        if int(loc) in booth_set:
            raise ValidationError(f"Booth Location {loc} cannot be entered twice.")
        booth_set.add(int(loc))
    
    # If there's more than one booth in the list, check if each booth is next to the previous booth
    if len(booth_list) > 1:
        for i in range(len(booth_list)-1):
            # Check if the current booth and the next booth are vertically adjacent, regardless of order
            booth_pair = tuple(sorted(map(int, [booth_list[i], booth_list[i+1]])))
            if booth_pair in wall_booths or booth_pair[::-1] in wall_booths:                 
                return True
            # Use the check_loc function to see if two booths are next to each other
            if check_loc(int(booth_list[i]), int(booth_list[i+1])) == False:
                # If they're not next to each other, raise a validation error
                raise ValidationError('The booths need to be positioned either horizontally adjacent or vertically adjacent if they are aligned along the walls.')
            
def validate_boothLoc_admin(form, field):
    # Get a list of booth locations from the field data and remove any whitespace
    boothLoc = get_clean_boothLoc(field.data)
    validate_not_empty(boothLoc)
    if not all(char.isdigit() or char == ',' for char in boothLoc):
        raise ValidationError('Booth Location can only contain numbers and commas. No spaces. Please enter Booth Location in the form: #,#')


    booth_list = boothLoc.split(",")

    # Check if booth(s) entered are in map_locations
    for loc in booth_list:
        if int(loc) not in map_locations:
            raise ValidationError(f"Booth location {loc} is not a valid location.")
            
 # Define a function to validate booth locations
def validate_boothLoc_available(form, field):
    # Get a clean list of booth locations without any spaces
    boothLoc = get_clean_boothLoc(field.data)
    # Get a list of all vendors and their reserved booth locations
    vendors = Vendor.query.all()
    reserved_locs = []
    for v in vendors:
        for loc in v.boothLoc.split(','):
            reserved_locs.append(loc.replace(' ', ''))
    
    # Check if any of the booth locations in the user input are already reserved by other vendors
    for loc in boothLoc.split(','):
        if loc in reserved_locs:
            raise ValidationError(f"Booth location {loc} is already reserved.")

# Define a function to validate that the number of booth locations matches the number of booths
def validate_boothNum_loc_match(form, field):
    boothNum = field.data
    boothLoc = get_clean_boothLoc(form.boothLoc.data)
    
    # Check if the number of booth locations in the user input matches the number of booths
    if boothLoc.count(',') + 1 != boothNum:
        raise ValidationError('Number of booth locations must match the number of booths.')

# Define a function to validate that a name does not contain any digits
def validate_no_digits(form, field):
    # Check if the name contains any digits
    if any(char.isdigit() for char in field.data):
        raise ValidationError('cannot contain any digits.')
    
# Define a function to validate that only contains digits   
def validate_digits(form, field):
    try:
        value = float(field.data)
        if value < 0:
            raise ValueError
    except (TypeError, ValueError):
        raise ValidationError('Payment Amount must be a digit and a postive number')

# Define a function to validate that the Booth Location field is not empty string or None
def validate_not_empty(boothLoc):
    if not boothLoc:
        raise ValidationError('cannot have empty Booth Location.')
    
def validate_no_special_chars(form, field):
    #Custom validator that checks if the name field contains special characters.
    if any(not c.isalpha() and not c.isspace() for c in field.data):
        raise ValidationError("Name should only contain letters and spaces")

# Define a function to validate that a phone number has a valid length
def validate_phoneNum(form, field):
    phoneNum = field.data.replace('-', '') # remove dashes
    
    # Check if the phone number has a valid length
    if len(phoneNum) < 10 or len(phoneNum) > 11:
        raise ValidationError('Invalid phone number length.')
    
    # Check if the phone number contains only digits
    if not phoneNum.isdigit():
        raise ValidationError('Phone number can only contain digits.')
    