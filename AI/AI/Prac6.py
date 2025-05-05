def job_scheduling(jobs):
    # Sort jobs by descending profit (greedy choice)
    jobs.sort(key=lambda x: x[2], reverse=True)
    
    n = max(job[1] for job in jobs)  # Max deadline
    schedule = [None] * n            # Time slots
    total_profit = 0

    for job in jobs:
        id, deadline, profit = job
        for i in range(min(n, deadline)-1, -1, -1):
            if schedule[i] is None:
                schedule[i] = id
                total_profit += profit
                break

    return schedule, total_profit
# Format: (Job ID, Deadline, Profit)
jobs = [('J1', 2, 100), ('J2', 1, 19), ('J3', 2, 27), ('J4', 1, 25), ('J5', 3, 15)]
schedule, profit = job_scheduling(jobs)
print("Job Order:", schedule)
print("Total Profit:", profit)
