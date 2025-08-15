requests = [0, 16, 24, 43, 50, 82, 100, 140, 150, 170, 190, 199]

head = 50

seek_sequence = []
seek_time = 0

current_position = head

for track in requests:
    seek_sequence.append(track)
    distance = abs(current_position - track)
    seek_time += distance
    current_position = track

print("Initial Head Position:", head)
print("Request Sequence:", requests)
print("Seek Sequence:", [head] + seek_sequence)
print("Total Seek Time:", seek_time)
print("Average Seek Time:", seek_time / len(requests))
