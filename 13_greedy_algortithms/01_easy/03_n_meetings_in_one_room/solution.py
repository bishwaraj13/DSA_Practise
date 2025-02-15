# https://www.geeksforgeeks.org/problems/n-meetings-in-one-room-1587115620/1
class Solution:
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,start,end):
        meetings = list(zip(start, end))
        meetings.sort(key=lambda x: x[1])
        
        prev_end_time = 0
        count_meetings = 0
        
        for meeting_start, meeting_end in meetings:
            if meeting_start >= prev_end_time:
                count_meetings += 1
                prev_end_time = meeting_end
                
        return count_meetings