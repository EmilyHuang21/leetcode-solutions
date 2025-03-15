class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gas = sum(gas)
        total_cost = sum(cost)
        
        if total_gas < total_cost:
            return -1  # Not enough gas to complete the circuit

        tank = 0  # Current gas in the tank
        start_index = 0  # Potential starting station

        for i in range(len(gas)):
            tank += gas[i] - cost[i]  # Update tank balance
            
            if tank < 0:  # If gas in tank is negative, reset starting station
                tank = 0
                start_index = i + 1  # Move start to next station

        return start_index
