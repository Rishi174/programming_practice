class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res_array = []

        for token in tokens:
            if token not in ["+", "-", "*", "/"]:
                res_array.append(int(token))
            else:
                num_0 = int(res_array.pop())
                num_1 = int(res_array.pop())
                if token == '+':
                    res_array.append(num_0 + num_1)
                elif token == '-':
                    res_array.append(num_1 - num_0)
                elif token == '*':
                    res_array.append(num_0 * num_1)
                else:
                    res_array.append(int(num_1 / num_0))
        return res_array[0]
