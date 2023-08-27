import re

def neveikianciu_streak(input_string):
    max_streak_length = 0
    max_streak_start = -1
    current_streak_length = 0
    current_streak_start = -1

    for i, char in enumerate(input_string):
        if char == '0':
            if current_streak_length == 0:
                current_streak_start = i
            current_streak_length += 1
            if current_streak_length > max_streak_length:
                max_streak_length = current_streak_length
                max_streak_start = current_streak_start
        else:
            current_streak_length = 0
            current_streak_start = -1

    return max_streak_start, max_streak_length

def find_middle_index(start_index, streak_length):
    middle_index = start_index + streak_length // 2
    if streak_length % 2 == 0:
        middle_index -= 1
    return middle_index

road_length = min(int(input("Enter the length of the road (in meters, up to 2000000): ")), 2000000)
lamp_count = (road_length // 20) + 1  # A lamp every 20 meters, plus the starting lamp
working_lamp_status = ['1'] * lamp_count
non_working_lamps = input("Enter the indices of non-working lamps separated by spaces: ").split()

for index in non_working_lamps:
    if index.isnumeric():
        lamp_index = int(index)
        if 0 <= lamp_index < lamp_count:
            working_lamp_status[lamp_index] = '0'

lamp_status_string = ''.join(working_lamp_status)
start_index, streak_length = neveikianciu_streak(lamp_status_string)

if start_index != -1:
    middle_index = find_middle_index(start_index, streak_length)
    print(f"Lamp needs to be replaced at index: {middle_index}")
else:
    print("No non-working lamps found.")