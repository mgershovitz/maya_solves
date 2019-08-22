from operator import add, truediv, imul, isub


class OpStr(object):
    ADD = "+"
    SUB = "-"
    MUL = "*"
    DIV = "/"
    PAR_L = "("
    PAR_R = ")"

class BasicCalculator(object):
    def __init__(self):
        self.operator_to_action = {
            OpStr.ADD: add,
            OpStr.SUB: isub,
            OpStr.MUL: imul,
            OpStr.DIV: truediv
        }

    def __eval_expression(self, arg_1, operator, arg_2):
        action = self.operator_to_action[operator]
        return action(arg_1, arg_2)

    def __evaluate_next_val_and_get_length(self, exp_arr, index):
        sub_exp_length = 2
        val = exp_arr[index + 1]
        if val == OpStr.PAR_L:
            sub_exp_length, val = self.__solve_expression_wrap(exp_arr[index + 2:])
        return sub_exp_length, val

    def __solve_expression(self, exp_arr, current_operators):
        new_exp = [exp_arr[0]]
        i = 1
        while i < len(exp_arr):
            operator = exp_arr[i]
            if operator == OpStr.PAR_R:
                current_exp_length = i + 2
                return current_exp_length, new_exp

            sub_exp_length, val = self.__evaluate_next_val_and_get_length(exp_arr, i)

            if operator in current_operators:
                res = self.__eval_expression(new_exp.pop(), operator, val)
                new_exp.append(res)
            else:
                new_exp.append(operator)
                new_exp.append(val)

            i += sub_exp_length

        return len(exp_arr), new_exp

    def __solve_expression_wrap(self, exp_arr):
        sub_exp_length, exp_arr = self.__solve_expression(exp_arr, [OpStr.MUL, OpStr.DIV])
        _, exp_arr = self.__solve_expression(exp_arr, [OpStr.ADD, OpStr.SUB])
        return sub_exp_length + 1, exp_arr[0]

    def solve(self, exp_arr):
        sub_exp_length, res = self.__solve_expression_wrap(exp_arr)
        return res


def run_tests():
    calc = BasicCalculator()
    assert calc.solve([1, "+", 2]) == 3
    assert calc.solve([1, "-", 2]) == -1
    assert calc.solve([2, "*", "(", 1, "+", 3, ")"]) == 8
    assert calc.solve([2, "*", "(", 1, "+", 6, "/", 3, ")"]) == 6
    assert calc.solve([2, "*", "(", 1, "+", 6, "/", 3, ")", "-", "(", 5, "*", 2, ")"]) == -4
    assert calc.solve([2, "+", "(", 3, "*", "(", 8, "/", 2, ")", "-", 10, ")"]) == 4


if __name__ == '__main__':
    run_tests()
