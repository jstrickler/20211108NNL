
# create empty dictionary
counts = {}
# open passwd file
with open('DATA/passwd') as passwd_in:
# for each line in password file
    for raw_line in passwd_in:
        line = raw_line.rstrip()
#     split line into fields
        fields = line.split(':')
#     get last field (which is the shell)
        # 3 variations
        # 1. shell = fields[-1]
        # 2. shell = fields.pop()
        *_, shell = fields   # unpack
#     check for shell in dictionary and add with value 0 if not present
        if shell == '':
            shell = "NONE"
        if shell not in counts:
            counts[shell] = 0
#     increment value where key is shell
        counts[shell] += 1

print(counts)