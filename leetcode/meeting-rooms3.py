import heapq
from typing import List

# TODO: could store the actual meetings allocated to each room, but thats unrequited for
#   solving the actual problem

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        #   create a priority queue based on the start time
        #   this creates a min heap, always poping the smallest start time
        heapq.heapify(meetings)
        
        #   heap to store data of rooms under use
        rooms_in_use = []
        #   heap to store free rooms
        free_rooms = [i for i in range(n)]
        heapq.heapify(free_rooms)
        #   array to hold meetings held
        room_meeting_count = [0 for _ in range(n)]
        
        
        for _ in range(len(meetings)):
            meeting = heapq.heappop(meetings) 
            meeting_duration = (meeting[1] - meeting[0])
            
            #   if there is a free room
            if free_rooms:
                room_index = heapq.heappop(free_rooms)
                heapq.heappush(rooms_in_use, (meeting[1], room_index))
                room_meeting_count[room_index] += 1
            
            else:
                #   find the first room that gets free
                first_empty_room = heapq.heappop(rooms_in_use)
                ending_time = first_empty_room[0] + meeting_duration
                heapq.heappush(rooms_in_use, (ending_time, first_empty_room[1]))
                room_meeting_count[first_empty_room[1]] += 1    

        max_meetings = -1
        index = -1
        for x in range(len(room_meeting_count)):
            if room_meeting_count[x] > max_meetings:
                max_meetings = room_meeting_count[x]
                index = x
        return index
    
if __name__ == "__main__":
    s = Solution()
    n = 4
    meetings = [[18,19],[3,12],[17,19],[2,13],[7,10]]
    
    print(s.mostBooked(n, meetings))