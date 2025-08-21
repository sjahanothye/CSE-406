def scan(requests, head, direction, disk_size=200):
    requests = sorted(requests)
    sequence = []
    total_seek = 0

    left = [r for r in requests if r < head]
    right = [r for r in requests if r >= head]

    if direction == "left":
        left.reverse()
        for r in left:
            total_seek += abs(head - r)
            head = r
            sequence.append(head)
        total_seek += head
        head = 0
        sequence.append(head)
        for r in right:
            total_seek += abs(head - r)
            head = r
            sequence.append(head)

    elif direction == "right":
        for r in right:
            total_seek += abs(head - r)
            head = r
            sequence.append(head)
        total_seek += (disk_size - 1 - head)
        head = disk_size - 1
        sequence.append(head)
        left.reverse()
        for r in left:
            total_seek += abs(head - r)
            head = r
            sequence.append(head)

    return sequence, total_seek


requests = [11, 34, 41, 50, 52, 60, 70, 114]
head = 50
direction = "left"

sequence, total_seek = scan(requests, head, direction)

print("Seek sequence:", sequence)
print("Total seek time:", total_seek)
print("Average seek time:", total_seek / len(requests))
