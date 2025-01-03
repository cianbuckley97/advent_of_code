rules = []
orders = []
with open("/home/cbuckley/projects/advent_of_code/Day5/input_data_Day5.txt", "r") as f:
    for line in f:
        if "|" in line:
            rule_s = (line.split("|"))
            rule_s = [int(rule) for rule in rule_s]
            rules.append(rule_s)
        elif "," in line:
            order_s = line.split(",")
            order_s = [int(order) for order in order_s]
            orders.append(order_s)

middle_tot = 0
for order in orders:
    good = True
    rel_rules = [rule for rule in rules if (rule[0] in order and rule[1] in order)]
    good = True if all([order.index(rule[0]) < order.index(rule[1]) for rule in rel_rules]) else False
    if good:
        middle_tot = middle_tot + order[int((len(order)+1)/2)-1]

print(middle_tot)