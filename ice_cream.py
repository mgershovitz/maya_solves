# Related blog post - https://mayareads.blog/2019/07/18/ice-cream/

class IceCreamChooser(object):
    def __init__(self, ice_cream_costs):
        self.ice_cream_costs = ice_cream_costs

    def choose_ice_cream_once(self, money):
        raise NotImplementedError

    def choose_ice_cream(self, money_sums):
        results = []
        for money in money_sums:
            results.append(self.choose_ice_cream_once(money))
        return results


class IceCreamChooseLimitedVisits(IceCreamChooser):
    def choose_ice_cream_once(self, money):
        diff_to_cost = {}
        for i in range(0, len(self.ice_cream_costs)):
            cost = self.ice_cream_costs[i]
            if cost in diff_to_cost:
                return diff_to_cost[cost], i
            else:
                diff = money - cost
                diff_to_cost[diff] = i


class IceCreamChooseManyVisits(IceCreamChooser):
    def __init__(self, ice_cream_costs):
        super(IceCreamChooseManyVisits, self).__init__(ice_cream_costs)
        self.all_possible_costs_sums = self.preprocess_ice_cream_costs()

    def preprocess_ice_cream_costs(self):
        all_possible_costs_sums = {}
        for i in range(0, len(self.ice_cream_costs)):
            for j in range(i + 1, len(self.ice_cream_costs)):
                costs_sum = self.ice_cream_costs[i] + self.ice_cream_costs[j]
                all_possible_costs_sums[costs_sum] = (i, j)

        return all_possible_costs_sums

    def choose_ice_cream_once(self, money):
        return self.all_possible_costs_sums[money]


def choose_ice_cream_flavours(ice_cream_costs, money_sums):
    if len(money_sums) >= len(ice_cream_costs):
        return IceCreamChooseManyVisits(ice_cream_costs).choose_ice_cream(money_sums)
    else:
        return IceCreamChooseLimitedVisits(ice_cream_costs).choose_ice_cream(money_sums)


def run_tests():
    assert choose_ice_cream_flavours([2, 5, 3, 1], [3, 8]) == [(0, 3), (1, 2)]
    assert choose_ice_cream_flavours([2, 5, 3, 1], [3, 8, 7, 6, 5]) == [(0, 3), (1, 2), (0, 1), (1, 3), (0, 2)]
    assert choose_ice_cream_flavours([2, 5, 3.5, 4, 4.5, 1.5, 2.5, 0.5], [3, 8]) == [(6, 7), (2, 4)]
    assert choose_ice_cream_flavours([1, 2, 3], [3, 3, 3, 4, 5, 3, 4]) == [(0, 1), (0, 1), (0, 1), (0, 2), (1, 2),
                                                                           (0, 1), (0, 2)]
    assert choose_ice_cream_flavours([2, 5, 3.5, 4, 4.5, 1.5, 2.5, 0.5], [3.5]) == [(0,5)]



if __name__ == '__main__':
    run_tests()
