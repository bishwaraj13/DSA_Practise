# https://leetcode.com/problems/alert-using-same-key-card-three-or-more-times-in-a-one-hour-period
from typing import *

class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        # Create a dictionary to group times by name
        worker_times = {}
        
        # Group times by worker name
        for name, time in zip(keyName, keyTime):
            if name not in worker_times:
                worker_times[name] = []
            worker_times[name].append(time)
        
        # List to store workers who triggered an alert
        alert_list = []
        
        # Process each worker's access times
        for name, times in worker_times.items():
            # Convert time strings to minutes for easier comparison
            minutes = []
            for time in times:
                hour, minute = map(int, time.split(':'))
                minutes.append(hour * 60 + minute)
            
            # Sort the times
            minutes.sort()
            
            # Check for 3+ accesses within a one-hour period
            for i in range(len(minutes) - 2):
                if minutes[i + 2] - minutes[i] <= 60:
                    alert_list.append(name)
                    break
        
        # Return sorted list of names
        return sorted(alert_list)