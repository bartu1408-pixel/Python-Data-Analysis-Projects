ages = [18, 25, 15, 30, 12, 45, 17, 22, 50, 14, 29, 33, 61, 8, 19, 35, 78, 86, 21, 32]
participants = 0
kids_teens = 0
adults = 0
seniors = 0

for age in ages:
    participants += 1
    if age < 18:
        kids_teens += 1
    elif 18 <= age <= 60:
        adults += 1
    else:
        seniors += 1

average_kids = ( kids_teens / participants ) * 100
average_adults = ( adults / participants ) * 100
average_seniors = ( seniors / participants ) * 100

print(f"{participants} participants have attended. \nKids:{kids_teens} (%{average_kids}), adults:{adults} (%{average_adults}), seniors:{seniors} (%{average_seniors})")

