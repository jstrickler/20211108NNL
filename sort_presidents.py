presidents = []

with open('DATA/presidents.txt') as pres_in:
    for raw_line in pres_in:
        line = raw_line.rstrip()
        (term, last_name, first_name, dob, dod,
            bplace, bstate, took_office, left_office, party) = line.split(':')
        record = first_name, last_name, bstate
        presidents.append(record)

for first_name, last_name, bstate in sorted(presidents, key=lambda p: (p[1], p[0])):
    print(f"{first_name:25s} {last_name:25s} {bstate}")