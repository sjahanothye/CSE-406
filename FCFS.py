class FCFS:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.completion_time = 0
        self.turnaround_time = 0
        self.waiting_time = 0

fcfs = [
    FCFS(0, 0, 4),
    FCFS(1, 2, 3),
    FCFS(2, 3, 2),
    FCFS(3, 5, 1)
]

current_time = 0
total_tat = 0
total_wt = 0

print("PID\tAT\tBT\tCT\tTAT\tWT")

for f in fcfs:
    if current_time < f.arrival_time:
        current_time = f.arrival_time
    f.completion_time = current_time + f.burst_time
    f.turnaround_time = f.completion_time - f.arrival_time
    f.waiting_time = f.turnaround_time - f.burst_time
    current_time = f.completion_time

    total_tat += f.turnaround_time
    total_wt += f.waiting_time

    print(f"P{f.pid}\t{f.arrival_time}\t{f.burst_time}\t{f.completion_time}\t{f.turnaround_time}\t{f.waiting_time}")
n = len(fcfs)
avg_tat = total_tat / n
avg_wt = total_wt / n

print(f"Average Turnaround Time: {avg_tat}")
print(f"Average Waiting Time: {avg_wt}")
