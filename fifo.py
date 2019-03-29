from itertools import cycle
FRAME_SIZE = 3
with open('input', 'r') as file:
    pages = [*map(int, file.read().split())]
faults = 0
frame = ['_', '_', '_']
c = cycle([0, 1, 2])
for page in pages:
    if page in frame:
        continue
    frame[next(c)] = page
    faults += 1
print('Page Faults : ', faults)
