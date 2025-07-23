class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.completion_time = 0
        self.turnaround_time = 0
        self.waiting_time = 0

def sjf_non_preemptive(processes):
    n = len(processes)
    time = 0
    completed = 0
    visited = [False] * n
    result = []

    while completed < n:
        available = [i for i in range(n) if processes[i].arrival_time <= time and not visited[i]]

        if not available:
            time += 1
            continue

        shortest = min(available, key=lambda i: processes[i].burst_time)
        p = processes[shortest]

        time += p.burst_time
        p.completion_time = time
        p.turnaround_time = p.completion_time - p.arrival_time
        p.waiting_time = p.turnaround_time - p.burst_time

        visited[shortest] = True
        completed += 1
        result.append(p)

    print("PID\tAT\tBT\tCT\tTAT\tWT")
    for p in result:
        print(f"{p.pid}\t{p.arrival_time}\t{p.burst_time}\t{p.completion_time}\t{p.turnaround_time}\t{p.waiting_time}")

    avg_tat = sum(p.turnaround_time for p in result) / n
    avg_wt = sum(p.waiting_time for p in result) / n
    print(f"Average Turnaround Time: {avg_tat}")
    print(f"Average Waiting Time: {avg_wt}")

processes = [
    Process('P1', 0, 12),
    Process('P2', 2, 4),
    Process('P3', 3, 6),
    Process('P4', 8, 5)
]
sjf_non_preemptive(processes)
