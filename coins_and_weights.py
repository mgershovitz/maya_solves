class Scale(object):
    def __init__(self):
        self.weigh_count = 0

    def weigh(self, coins_x, coins_y):
        self.weigh_count += 1
        if sum(coins_x) > sum(coins_y):
            return 1
        elif sum(coins_y) > sum(coins_x):
            return -1
        else:
            return 0

class CoinsAndWeights(object):
    def __init__(self):
        self.scale = Scale()

    @staticmethod
    def divide_group_to_three(group):
        groups_size = int(len(group)/3)
        groups = []
        for i in range(0, 3):
            groups.append(group[groups_size * i: groups_size * (i + 1)])
        return groups

    @staticmethod
    def add_regular_coins_to_odd_group(odd_group, control_group):
        if len(odd_group) % 3 == 1:
            odd_group.extend(control_group[0:2])
        elif len(odd_group) % 3 == 2:
            odd_group.extend(control_group[0:1])

    def find_odd_group(self, coins, odd_coin_weight):
        x, y, z = self.divide_group_to_three(coins)
        first_weigh = self.scale.weigh(x, y)
        if first_weigh == 0:
            return z
        else:
            if first_weigh == odd_coin_weight:
                return x
            else:
                return y

    def find_odd_group_and_odd_weight(self, coins):
        x, y, z = self.divide_group_to_three(coins)
        first_weigh = self.scale.weigh(x, y)
        second_weigh = self.scale.weigh(x, z)

        if first_weigh == 0 and second_weigh == 0:
            return None, None, None

        if first_weigh == 0:
            odd_group = z
            control_group = x
            odd_coin_weight = -1 * second_weigh
        elif second_weigh == 0:
            odd_group = y
            control_group = x
            odd_coin_weight = -1 * first_weigh
        else:
            odd_group = x
            control_group = y
            odd_coin_weight = first_weigh
        return odd_group, control_group, odd_coin_weight

    def find_odd_coin(self, coins):
        coins_remainder_group_size = len(coins) % 3
        main_groups_size = len(coins) - coins_remainder_group_size

        coins_remainder_group = coins[main_groups_size:]
        coins = coins[:main_groups_size]

        odd_group, control_group, odd_coin_weight = \
            self.find_odd_group_and_odd_weight(coins)

        if odd_group is None:
            # odd coin is in the remainder group
            self.add_regular_coins_to_odd_group(coins_remainder_group, coins)
            odd_group, _, _ = self.find_odd_group_and_odd_weight(coins_remainder_group)
            return odd_group[0]

        while len(odd_group) > 1:
            self.add_regular_coins_to_odd_group(odd_group, control_group)
            odd_group = self.find_odd_group(odd_group, odd_coin_weight)

        return odd_group[0]

def run_tests():
    caw = CoinsAndWeights()
    coins = [0, 0, 1]
    assert caw.find_odd_coin(coins) == 1
    assert caw.scale.weigh_count == 2

    caw = CoinsAndWeights()
    coins = [0, 1, 1]
    assert caw.find_odd_coin(coins) == 0
    assert caw.scale.weigh_count == 2

    caw = CoinsAndWeights()
    coins = [1] * 27
    coins[10] = 3
    assert caw.find_odd_coin(coins) == 3
    assert caw.scale.weigh_count == 4

    caw = CoinsAndWeights()
    coins = [1] * 28
    coins[27] = -1
    assert caw.find_odd_coin(coins) == -1
    assert caw.scale.weigh_count == 4

    caw = CoinsAndWeights()
    coins = [1] * 100000
    coins[9007] = 3
    assert caw.find_odd_coin(coins) == 3
    assert caw.scale.weigh_count == 12


if __name__ == '__main__':
    run_tests()