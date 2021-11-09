import sys
# MAIN PART

raw_celsius = sys.argv[1]   # 2nd element of sys.argv

celsius = float(raw_celsius)

#-------------

# CALCULATION

fahrenheit = ((9 * celsius) / 5) + 32

print(f"{celsius}\u00B0 C is {fahrenheit}\u00B0 F")