from typing import List, Dict, Set

# TODO: we can do only one for on the sorted meetings based on time, and hold meetings form a certain time stamp
# and if we get a known person, we will update all the meetings in that time frame

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        #   sort meetings based on their time
        # meetings.append([0, first_person, 0])

        #   hold all the people that meet at time i in set, and i as the key
        chrono: Dict[int ,Set]= {}
        for p1, p2, t in meetings:
            try:
                chrono[t].update([p1, p2])
            except KeyError:
                chrono[t] = set([p1, p2])
                
        covid = [[k, chrono[k]] for k in chrono.keys()]
        covid.sort(key= lambda x: x[0])

        know_secret = set([0, first_person])
        for t, people in covid:
            if know_secret.intersection(people):
                know_secret = know_secret.union(people)
        
        return list(know_secret)
    
if __name__ == "__main__":
    s = Solution()
    n = 6
    meetings = [[1,2,5],[2,3,8],[1,5,10]]
    first_person = 1
    print(s.findAllPeople(n, meetings, first_person))