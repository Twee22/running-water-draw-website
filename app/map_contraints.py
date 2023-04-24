
# list of valid locations on the vendor map. 0 represents 'filler'
map_locations = [128, 0, 115, 116, 0, 119, 120, 0, 123, 124, 0, 0, 126, 0, 113, 114, 0, 117, 118, 0, 121, 122, 0, 0, 126, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 125, 0, 103, 104, 0, 107, 108, 0, 111, 112, 0, 0, 0, 0, 101, 102, 0, 105, 106, 0, 109, 110, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 88, 0, 91, 92, 0, 95, 96, 0, 99, 100, 0, 0, 0, 0, 89, 90, 0, 93, 94, 0, 97, 98, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 86, 0, 0, 0, 76, 0, 79, 80, 0, 83, 84, 0, 85, 0, 0, 0, 75, 0, 77, 78, 0, 81, 82, 0, 0, 46, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 45, 0, 65, 66, 0, 69, 70, 0, 73, 74, 0, 0, 44, 0, 63, 64, 0, 67, 68, 0, 71, 72, 0, 50, 43, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 49, 42, 0, 53, 54, 0, 57, 58, 0, 61, 62, 0, 48, 41, 0, 51, 52, 0, 55, 56, 0, 59, 60, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 31, 32, 0, 35, 36, 0, 39, 40, 0, 15, 10, 0, 29, 30, 0, 33, 34, 0, 37, 38, 0, 14, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13, 8, 0, 19, 20, 0, 23, 24, 0, 27, 28, 0, 12, 7, 0, 17, 18, 0, 21, 22, 0, 25, 26, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 5, 4, 3, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


def check_loc(user_booth1, user_booth2):
    # Check if both user inputs are in the list of map locations
    if user_booth1 not in map_locations or user_booth2 not in map_locations:
        return False

    # Get the indices of the user inputs in the list
    index1, index2 = map_locations.index(user_booth1), map_locations.index(user_booth2)

    # Check if the absolute difference between the indices is less than or equal to 1
    if abs(index1 - index2) <= 1:
        return True
    
    return False




