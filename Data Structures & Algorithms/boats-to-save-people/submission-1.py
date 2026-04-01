class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left  = 0
        right = len(people) -1
        Boats = 0
        while (left <= right):
            if(left == right):
                Boats+=1
                break
            if(people[left]+people[right]<= limit):
                Boats+=1
                left+=1 
                right-=1
            else:
                right-=1
                Boats+=1
        return Boats
        