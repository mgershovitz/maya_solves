# Related blog post - https://mayareads.blog/2019/11/23/senate-evacuation/

import string

def remove_senators(senators_counter, senators_to_evict):
    for senator in senators_to_evict:
        senators_counter[senator] -= 1
        if senators_counter[senator] == 0:
            senators_counter.pop(senator)

def format_results(eviction_plan_list):
    eviction_plan_list = ["".join(senators) for senators in eviction_plan_list]
    return " ".join(eviction_plan_list)


def choose_next_to_evict(senators_counter):
    if len(senators_counter) == 2:
        return list(senators_counter.keys())
    else:
        return [max(senators_counter, key=senators_counter.get)]


def evict_the_senate_iter(senators_counter):
    eviction_plan = []
    while len(senators_counter) > 0:
        senators_to_evict = choose_next_to_evict(senators_counter)
        remove_senators(senators_counter, senators_to_evict)
        eviction_plan.append(senators_to_evict)
    return format_results(eviction_plan)


if __name__ == '__main__':
    num_test_cases = int(input())
    for i in range(1, num_test_cases + 1):
        num_parties = int(input())
        parties = [c for c in string.ascii_uppercase[:num_parties]]
        senators_count_per_party = [int(s) for s in input().split(" ")]
        counter = dict(zip(parties, senators_count_per_party))

        print("Case #{}: {}".format(i, evict_the_senate_iter(counter)))
