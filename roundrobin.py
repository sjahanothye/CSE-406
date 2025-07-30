processes = ['P1', 'P2', 'P3', 'P4', 'P5']
arrival_time = [0, 1, 2, 3, 4]
burst_time = [5, 3, 1, 2, 3]
time_quantum = 2

n = len(processes)
remaining_bt = burst_time[:]
completion_time = [0] * n
tat = [0] * n
wt = [0] * n

time = 0
done = False

while not done:
    done = True
    for i in range(n):
        if arrival_time[i] <= time and remaining_bt[i] > 0:
            done = False
            if remaining_bt[i] > time_quantum:
                time += time_quantum
                remaining_bt[i] -= time_quantum
            else:
                time += remaining_bt[i]
                completion_time[i] = time
                remaining_bt[i] = 0

for i in range(n):
    tat[i] = completion_time[i] - arrival_time[i]
    wt[i] = tat[i] - burst_time[i]

print("PID\tAT\tBT\tCT\tTAT\tWT")
for i in range(n):
    print(f"{processes[i]}\t{arrival_time[i]}\t{burst_time[i]}\t{completion_time[i]}\t{tat[i]}\t{wt[i]}")

print("Average TAT:", sum(tat)/n)
print("Average WT:", sum(wt)/n)
