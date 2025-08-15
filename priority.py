processes = [
    ["P1", 0, 11, 2],
    ["P2", 5, 28, 0],
    ["P3", 12, 2, 3],
    ["P4", 2, 10, 1],
    ["P5", 9, 16, 4]
]
processes.sort(key=lambda x: x[1])

n = len(processes)
completed = []
time = 0
CT, TAT, WT = {}, {}, {}

while len(completed) < n:
    available = [p for p in processes if p[1] <= time and p[0] not in completed]

    if available:
        available.sort(key=lambda x: x[3])
        current = available[0]

        pid, at, bt, pr = current
        time += bt  
        CT[pid] = time
        TAT[pid] = CT[pid] - at
        WT[pid] = TAT[pid] - bt
        completed.append(pid)
    else:
        time += 1

print("PID\tAT\tBT\tPriority\tCT\tTAT\tWT")
for p in processes:
    pid = p[0]
    print(f"{pid}\t{p[1]}\t{p[2]}\t{p[3]}\t\t{CT[pid]}\t{TAT[pid]}\t{WT[pid]}")

avg_tat = sum(TAT.values()) / n
avg_wt = sum(WT.values()) / n
print(f"\nAverage TAT: {avg_tat}")
print(f"Average WT: {avg_wt}")
