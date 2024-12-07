import random

with open('input.txt', 'r') as f:
	data = f.read()


test_data =  """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""

def parse_input(data):
    rules, updates = data.split('\n\n')
    # print(rules)
    rules = rules.split('\n')
    updates = updates.split('\n')
    rules = list(map(lambda x: x.split('|'), rules))
    updates = list(map(lambda x: x.split(','), updates))

    return rules, updates

def get_middle_element(l):
    mid_index = int((len(l) - 1)/2)
    return l[mid_index]



def generate_rule_dicts(rules):
    after_dict = {}
    before_dict = {}
    for rule in rules:
        if rule[0] not in after_dict.keys():
            after_dict[rule[0]] = set(rule[1])
        else:
            after_dict[rule[0]].add(rule[1])

        if rule[1] not in before_dict.keys():
            before_dict[rule[1]] = set(rule[0])
        else:
            before_dict[rule[1]].add(rule[0])

    return after_dict, before_dict

def check_update(update, after_dict, before_dict):
    already_seen = set()

    update_c = update.copy()
    
    while update_c:
        current_page = update_c.pop(0)
        elements_after = after_dict.get(current_page)
        elements_before = before_dict.get(current_page)
        if elements_after is not None:
            if already_seen.intersection(elements_after):
                return False
            
        if elements_before is not None:
            if elements_before.intersection(update_c):
                return False

        already_seen.add(current_page)
    
    return True



def part1(data):
    rules, updates = parse_input(data)

    updates = list(filter(lambda x: x != [''], updates))

    after_dict, before_dict = generate_rule_dicts(rules)
 
    
    valid_updates = list(filter(lambda x: check_update(x, after_dict, before_dict), updates))
    return sum(map(int, map(get_middle_element, valid_updates)))

def generate_correct_order(rules, all_pages):
    ordered_pages = list(all_pages.copy())
    updates = True
    while updates:
        updates = False
        for rule in rules:
            if rule[0] in ordered_pages and rule[1] in ordered_pages:
                before_index = ordered_pages.index(rule[0])
                after_index = ordered_pages.index(rule[1])
                if before_index > after_index:
                    temp = ordered_pages.pop(after_index)
                    ordered_pages.insert(before_index+1, temp)
                    
                    updates = True

    return ordered_pages



def part2(data):
    rules, updates = parse_input(data)

    all_pages = []
    for update in updates:
        all_pages += update
    all_pages = sorted(list(set(all_pages)))

    updates = list(filter(lambda x: x != [''], updates))

    after_dict, before_dict = generate_rule_dicts(rules)

    
    invalid_updates = list(filter(lambda x: not check_update(x, after_dict, before_dict), updates))

    sorted_updates = []

    for update in invalid_updates:
        sorted_update = generate_correct_order(rules, update)
        print(check_update(sorted_update, after_dict, before_dict))
        sorted_updates.append(sorted_update)

    return sum(map(int, map(get_middle_element, sorted_updates)))



print(part1(data))
print(part2(data))