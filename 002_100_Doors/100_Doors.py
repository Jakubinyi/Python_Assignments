doors = [0]*100

for a in range(0, 100):
    for b in range(a, 100, a + 1):
        if doors[b] == 0:
            doors[b] = 1
        else:
            doors[b] = 0
            
open_doors = []

for b in range(0, len(doors)):
    if doors[b] == 1:
        open_doors.append(b + 1)

print("The following doors are open: ", str(open_doors).strip("[]"))