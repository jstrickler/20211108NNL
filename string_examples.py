s1 = "spam\n"
s2 = 'spam\n'
s3 = """spam\n"""  # triple-quoted, OR
s4 = '''spam\n'''  # triple-delimited
s5 = r"spam\n"  # raw string

print("It's a Python thing")
print('A "Python" thing')
print("""It's a "Python" thing""")
query = """
select *
from customers
where state = 'WI'
order by account_balance desc
"""
print(len(s1), len(s2), len(s5))

print("It is 64\u00B0 in Durham")

# print("foo\
# bar")

a = None  # null or placeholder
b = ''
c = 0
print(type(None))


