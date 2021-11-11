import csv

file_path = 'DATA/mary.txt'
mary_in = open(file_path, 'r')
# work with file ...
mary_in.close()

with open(file_path) as mary_in:   # mary_in.__exit__() -> .close()
    for raw_line in mary_in:
        line = raw_line.rstrip()  # strip trailing whitespace
        print(line)
print("-" * 60)

with open(file_path) as mary_in:
    contents = mary_in.read()  # read entire file into string
    print("RAW:")
    print(repr(contents))
    print("NORMAL:")
    print(contents)
print("-" * 60)

with open(file_path) as mary_in:
    all_lines = mary_in.readlines()
    print(all_lines)
print("-" * 60)

with open(file_path) as mary_in:
    all_lines_without_nl = [line.rstrip() for line in mary_in]
    print(all_lines_without_nl)

state = "Massachusetts"
va_potus = []
with open('DATA/presidents.txt') as presidents_in:
    for raw_line in presidents_in:
        term, last_name, first_name, dob, dod, bplace, bstate, start, end, party = raw_line.split(':')
        if bstate == state:
            record = first_name, last_name, bplace
            va_potus.append(record)

print(va_potus[3])
print(va_potus)

with open("va_potus.txt", "w") as potus_out:
    for president in va_potus:
        potus_out.write('\t'.join(president) + '\n')
print()
with open('va_potus.csv', "w") as potus_out:
    wtr = csv.writer(potus_out, lineterminator="\n")
    for president in va_potus:
        wtr.writerow(president)

with open('va_potus.csv') as potus_in:
    rdr = csv.reader(potus_in)
    for president in rdr:
        print(president)

with open('DATA/mary.txt') as mary_in:
    with open('mary_upper.txt', 'w') as mary_out:
        for line in mary_in:
            mary_out.write(line.upper().replace('E', 'X'))
