from typing import List, Dict, Set

# TODO: we can do only one for on the sorted meetings based on time, and hold meetings form a certain time stamp
# and if we get a known person, we will update all the meetings in that time frame

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        #   sort meetings based on their time
        # meetings.append([0, first_person, 0])

        #   hold all the people that meet at time i in set, and i as the key
        chronology: Dict[int ,List]= {}
        for p1, p2, t in meetings:
            try:
                chronology[t].append([p1, p2])
            except KeyError:
                chronology[t] = [[p1, p2]]
                
        meetings_at_t = [[k, chronology[k]] for k in chronology.keys()]
        meetings_at_t.sort(key= lambda x: x[0])

        know_secret = set([0, first_person])
        for t, meetings_t in meetings_at_t:
            check = True
            while check:
                update = []
                for i in range(len(meetings_t)):
                    if (meetings_t[i][0] in know_secret) or (meetings_t[i][1] in know_secret):
                        know_secret.update([meetings_t[i][0], meetings_t[i][1]])
                        update.append(i)
                if not update:
                    check = False
                else:
                    for i in sorted(update, reverse=True):
                        del meetings_t[i]
                    
                    
        
        return list(know_secret)
    
if __name__ == "__main__":
    s = Solution()
    n = 6
    meetings = [[1,2,5],[2,3,8],[1,5,10]]
    first_person = 1
    print(s.findAllPeople(n, meetings, first_person))