from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        gas_result = []
        for i in range(0, len(gas)):
            gas[i] = gas[i] - cost[i]
            if gas[i] >= 0:
                gas_result.append(i)
        if gas_result:
            for start in gas_result:
                can_travel = True
                total = 0
                for i in range(start, len(gas) + start):
                    index = i % len(gas)
                    total += gas[index]
                    if total < 0:
                        can_travel = False
                        break
                if can_travel:
                    return start
        return -1



s = Solution()
print(s.canCompleteCircuit(gas = [2], cost = [2]))


