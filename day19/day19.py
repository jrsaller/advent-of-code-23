import shared
import functools

def create_workflows(lines):
    flow_dict = {}
    for flow in lines:
        name = flow.split("{")[0]
        rulesList = flow.split("{")[1][:-1]
        rules = rulesList.split(",")
        flow_dict[name] = rules
    return flow_dict

def create_items(lines):
    end_items = []
    for item in lines:
        item = item[1:-1].split(",")
        final = {}
        for attr in item:
            ind = attr.index("=")
            k = attr[:ind]
            v = int(attr[ind+1:])
            final[k] = v
        end_items.append(final)
    return end_items

def check_item(item, flow_dict: dict):
    result = 'in'
    # print(item)
    while result != 'A' and result != 'R':
        # print(result)
        # print(flow_dict[result])
        for flow in flow_dict[result]:
            if ":" in flow:
                ind = flow.index(":")
                cond = flow[:ind]
                dest = flow[ind+1:]
                if (eval(cond,None,item)):
                    result = dest
                    break
            else:
                result = flow
                break
    if result == 'A':
        return True
    else:
        return False

lines = shared.read_file("source.txt")

flows = lines[:lines.index("")]
items = lines[lines.index("")+1:]
# print(flows)
flow_dict = create_workflows(flows)
items_dict = create_items(items)

# print(flow_dict)
# print(items_dict)

total = 0
for item in items_dict:
    if check_item(item, flow_dict):
        total += sum(item.values())

print('PART 1:',total)
print()
# PART 2
total2 = 0
Xs = []
Ms = []
As = []
Ss = []
final_rules = []

def getRules(flows, current_flow, existing_rules):
    first_rule = current_flow[0]
    # print("current flow:",current_flow)
    # print("existing rules: ", existing_rules)
    # print("final rules: ", final_rules)
    if ":" in first_rule:
        cond = first_rule[:first_rule.index(":")]
        dest = first_rule[first_rule.index(":")+1:]
        if dest == "A":
            final_rules.append(existing_rules + [cond])
            x = getRules(flows, current_flow[1:], existing_rules+["not " + cond])
            if x and x not in final_rules:
                final_rules.append(x)
            return existing_rules + [cond]
        elif dest == "R":
            getRules(flows, current_flow[1:], existing_rules + ["not " + cond])
        else:
            getRules(flows, flows[dest], existing_rules+[cond])
            getRules(flows, current_flow[1:], existing_rules + ["not " + cond])
            return existing_rules
    else:
        if first_rule == "A":
            if existing_rules not in final_rules:
                final_rules.append(existing_rules)
        elif first_rule == "R" or first_rule == "":
            return []
        else:
            getRules(flows, flows[first_rule], existing_rules)
        


# for flow in flow_dict:
#         print(flow)
#         print(flow_dict[flow])
#         for item in flow_dict[flow]:
#             if ":" in item:
#                 ind = item.index(":")
#                 cond = item[:ind]
#                 dest = item[ind+1:]
#                 print(get_all_rules(cond,dest))
#             print()



# print(flow_dict["in"])
getRules(flow_dict, flow_dict["in"],[])
# print(final_rules)
print()
for ruleset in final_rules:
    if ruleset:
        print(ruleset)
        x_rules = []
        m_rules = []
        a_rules = []
        s_rules = [] 
        for rule in ruleset:
            if "x" in rule:
                x_rules.append(rule)
            elif "m" in rule:
                m_rules.append(rule)
            elif "a" in rule:
                a_rules.append(rule)
            elif "s" in rule:
                s_rules.append(rule)
        x_wins = 0
        m_wins = 0
        a_wins = 0
        s_wins = 0
        for x in range(1,4001):
            if all(eval(rule,None,{"x":x}) for rule in x_rules):
                x_wins += 1
        for m in range(1,4001):
            if all(eval(rule,None,{"m":m}) for rule in m_rules):
                m_wins += 1
        for a in range(1,4001):
            if all(eval(rule,None,{"a":a}) for rule in a_rules):
                a_wins += 1
        for s in range(1,4001):
            if all(eval(rule,None,{"s":s}) for rule in s_rules):
                s_wins += 1
        print("x:",x_wins,"m:",m_wins,"a:",a_wins,"s:",s_wins)
        total2 += (x_wins*m_wins*a_wins*s_wins)
        print(total2)
        # print()


# for item in flow_dict["in"]:
#     if ":" in item:
#         ind = item.index(":")
#         cond = item[:ind]
#         dest = item[ind+1:]
#         print(get_all_rules(cond,dest))
#     else:
#         print(get_all_rules(item,item))
#     print()

print("PART 2:",total2)