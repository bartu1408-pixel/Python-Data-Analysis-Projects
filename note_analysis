notes = [45, 85, 20, 90, 100, 60, 72, 35, 23, 43, 27, 100, 98]

sum = 0
highest_note = 0
lowest_note = notes[0]
pass_count = 0

for note in notes:
    sum += note
    if note > highest_note:
        highest_note = note
    elif note < lowest_note:
        lowest_note = note

for note in notes:
    if note > 50:
        pass_count += 1

average = sum / len(notes)
pass_percent = int(( pass_count / len(notes) ) * 100)

print(f"Class average note is: {average}")
print(f"highest note is: {highest_note} \nlowest note is: {lowest_note}")
print(f"{pass_count} student passed.")
print(f"%{pass_percent} student passed.")
