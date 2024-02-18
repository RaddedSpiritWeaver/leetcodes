import heapq
from typing import List

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        #   create a priority queue based on the start time
        #   this creates a min heap, always poping the smallest start time
        heapq.heapify(meetings)
        
        #   array to hold time when room x gets empty, (time, room_index)
        #   need to use this as a priority queue as well
        room_free_time = [(0, i)for i in range(n)]
        #   array to hold meetings held
        room_meeting_count = [0 for _ in range(n)]
        # TODO: could store the actual meetings allocated to each room, but thats unrequited for
        #   solving the actual problem
        for _ in range(len(meetings)):
            meeting = heapq.heappop(meetings) 
            meeting_duration = (meeting[1] - meeting[0])
            
            first_empty_room = heapq.heappop(room_free_time)
            
            ending_time = 0
            if meeting[0] >= first_empty_room[0]:
                #   there is no delay, so the room is free when the meeting ends
                ending_time = meeting[1]
            else:
                #   the room is free, after the previous meeting is done, and the new meeting duration ends
                ending_time = first_empty_room[0] + meeting_duration
            
            new_room_time = (ending_time, first_empty_room[1])
            heapq.heappush(room_free_time, new_room_time)
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