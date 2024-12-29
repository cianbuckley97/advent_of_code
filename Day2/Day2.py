def safe_report(values):
    strictly_increasing = all(int(x)<int(y) for x,y in zip(values, values[1:]))
    strictly_decreasing = all(int(x)>int(y) for x,y in zip(values, values[1:]))
    if strictly_increasing or strictly_decreasing:
        gradual_change = [abs(int(x)-int(y)) for x,y in zip(values, values[1:])]
        if max(gradual_change) < 4 and min(gradual_change)>0:
            return True
    return False

safe_reports = 0
with open("input_data_Day2.txt", "r") as f:
    for line in f:
        values = line.split()
        values = [int(value) for value in values]
        if safe_report(values):
            safe_reports = safe_reports + 1
        else:
            lists_with_one_element_dropped = [values[:i] + values[i+1:] for i in range(len(values))]
            for options in lists_with_one_element_dropped:
                if safe_report(options):
                    safe_reports = safe_reports + 1
                    print("here")
                    break

print(safe_reports)