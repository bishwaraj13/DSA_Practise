# https://www.geeksforgeeks.org/problems/job-sequencing-problem-1587115620/1
 # built on top of 01_solution.. this solution had TLE
class Solution:
    def JobSequencing(self, id, deadline, profit):
        n = len(id)
        # Create jobs list and sort by profit in descending order
        jobs = list(zip(id, deadline, profit))
        jobs.sort(key=lambda x: x[2], reverse=True)
        
        # Find maximum deadline
        max_deadline = max(deadline)
        
        # Use a set to keep track of available slots
        # This is more efficient than checking array positions
        available_slots = set(range(max_deadline))
        count_jobs = 0
        count_profit = 0
        
        for job_id, job_deadline, job_profit in jobs:
            # Find the latest available slot before deadline
            possible_slots = [x for x in available_slots if x < job_deadline]
            if possible_slots:
                slot = max(possible_slots)
                available_slots.remove(slot)
                count_jobs += 1
                count_profit += job_profit
                
        return [count_jobs, count_profit]