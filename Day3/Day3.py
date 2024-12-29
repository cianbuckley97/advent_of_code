import re

pattern = r'mul\((-?\d*\.?\d+),\s*(-?\d*\.?\d+)\)'

sum_total = 0
with open("input_data_Day3.txt", "r") as f:
    for line in f:
        mul_instances = re.findall(pattern, line)
        for instance in mul_instances:
            sum_total = sum_total + int(instance[0])*int(instance[1])

print(sum_total)


# Part 2

do_pattern = r'do\(\)'  # Matches the do() function
dont_pattern = r"don't\(\)"  # Matches the don't() function
mul_pattern = r'mul\((-?\d*\.?\d+),\s*(-?\d*\.?\d+)\)'  # Matches mul(x, y) with numbers

sum_total = 0
with open("input_data_Day3.txt", "r") as f:
    do = True
    for line in f:
        # print(line)
        mul_instances = re.finditer(f"({do_pattern})|({dont_pattern})|({mul_pattern})", line)
        for instance in mul_instances:
            # print(instance)
            if instance.group(1):
                do = True
            elif instance.group(2):
                print("False")
                do = False
            elif instance.group(3):
                x, y = int(instance.group(4)), int(instance.group(5))
                if do:
                    sum_total = sum_total + x*y


print(sum_total)