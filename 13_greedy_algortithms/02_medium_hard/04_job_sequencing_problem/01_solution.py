# https://www.geeksforgeeks.org/problems/job-sequencing-problem-1587115620/1
class Solution:
    # Function used for sorting jobs according to their deadlines
    def JobSequencing(self, id, deadline, profit):
        jobs = list(zip(id, deadline, profit))
        jobs.sort(key=lambda x: x[2], reverse=True)
        
        max_deadline = max(deadline)
        schedule = [-1] * max_deadline
        count_jobs = 0
        count_profit = 0
        
        for job in jobs:
            job_id, job_deadline, job_profit = job
            
            for j in range(job_deadline - 1, -1, -1):
                if schedule[j] == -1:
                    schedule[j] = job_id
                    count_jobs += 1
                    count_profit += job_profit
                    break
                
        return [count_jobs, count_profit]
