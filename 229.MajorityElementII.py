class Solution:
    def majorityElement(self, array):
        stack = {}
        k_ = None
        c_ = 0
        L = len(array)
        result = []

        for i in range(L):

            if array[i] not in stack:
                if len(stack) < 3:
                    stack[array[i]] = 1

                elif 0 in stack.values():
                    for k in stack.keys():
                        if stack[k] == 0:
                            k_ = k
                    stack.pop(k_)
                    stack[array[i]] = 1

                else:
                    for k in stack.keys():
                        stack[k] -= 1
                    c_ += 1
            else:
                stack[array[i]] += 1

        # result
        k_ = int(L/3)
        for k in stack.keys():
            c_ = 0
            for i in range(L):
                if array[i] == k:
                    c_ += 1
                    if c_ > k_:
                        result.append(k)
                        break
        return result
