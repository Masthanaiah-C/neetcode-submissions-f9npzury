class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        cars = sorted(zip(position, speed), reverse=True)  # closest to target first
        fleets = 0
        cur_fleet_time = 0.0

        for pos, spd in cars:
            t = (target - pos) / spd
            if t > cur_fleet_time:
                fleets += 1
                cur_fleet_time = t
        return fleets

