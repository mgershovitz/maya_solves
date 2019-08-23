from basic_calc import BasicCalculator, OpStr


def is_number(val):
    return not isinstance(val, str)

class Config(object):
    CONF_1 = 1
    CONF_2 = 2

class MagicCalculator(BasicCalculator):
    def __init__(self):
        super(MagicCalculator, self).__init__()

    @staticmethod
    def __apply_writing_conv(exp_arr, config):
        new_exp = []
        i = 0
        parenthesis_counter = 0

        while i < len(exp_arr):
            next_val = exp_arr[i]
            new_exp.append(next_val)

            if is_number(next_val) and i < len(exp_arr) - 1 and exp_arr[i + 1] == OpStr.PAR_L:
                if config == Config.CONF_1:
                    new_exp.append(OpStr.MUL)
                elif config == Config.CONF_2:
                    parenthesis_counter += 1
                    number = new_exp.pop()
                    new_exp.extend([OpStr.PAR_L, number, OpStr.MUL])
            elif next_val == OpStr.PAR_R:
                parenthesis_counter -= 1
                if parenthesis_counter == 0:
                    new_exp.append(OpStr.PAR_R)
            i += 1
        return new_exp

    def solve(self, exp_arr, config=Config.CONF_1):
        exp_arr = self.__apply_writing_conv(exp_arr, config)
        return super(MagicCalculator, self).solve(exp_arr)

def run_tests():
    calc = MagicCalculator()
    assert calc.solve([1, "+", 2]) == 3
    assert calc.solve([1, "-", 2]) == -1
    assert calc.solve([2, "*", "(", 1, "+", 3, ")"]) == 8
    assert calc.solve([2, "*", "(", 1, "+", 6, "/", 3, ")"]) == 6
    assert calc.solve([2, "*", "(", 1, "+", 6, "/", 3, ")", "-", "(", 5, "*", 2, ")"]) == -4
    assert calc.solve([2, "+", "(", 3, "*", "(", 8, "/", 2, ")", "-", 10, ")"]) == 4

    assert calc.solve([8, "/", 2, "(", 2, "+", 2, ")"]) == 16
    assert calc.solve([8, "/", 2, "(", 2, "+", 2, ")"], Config.CONF_2) == 1

    assert calc.solve([1, "+", "(", 2, "/", 2, "(", 1, "+", 1, ")", "+", 3, ")"]) == 6
    assert calc.solve([1, "+", "(", 2, "/", 2, "(", 1, "+", 1, ")", "+", 3, ")"], Config.CONF_2) == 4.5


if __name__ == '__main__':
    run_tests()
