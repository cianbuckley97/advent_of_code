import requests

# i\nput_data = requests.get("https://adventofcode.com/2024/day/1/input")

arr_1 = []
arr_2 = []
with open("input_data_Day1.txt", "r") as f:
    for line in f:
        arr_1.append(int(line.strip().split()[0]))
        arr_2.append(int(line.strip().split()[1]))

arr_1.sort()
arr_2.sort()

total_distance = sum([abs(x-y) for x,y in zip(arr_1,arr_2)])
print(total_distance)