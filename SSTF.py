def sstf(requests, head):
    requests = requests.copy()
    sequence = [head]
    total_seek_time = 0

    while requests:

        closest = min(requests, key=lambda x: abs(x - head))
        total_seek_time += abs(head - closest)
        head = closest
        sequence.append(head)
        requests.remove(closest)

    return sequence, total_seek_time

requests = [176, 79, 34, 60, 92, 11, 41]
head = 50

sequence, total_seek_time = sstf(requests, head)

print("Seek sequence:", sequence)
print("Total seek time:", total_seek_time)
print("Average seek time:", total_seek_time / (len(sequence) - 1))
