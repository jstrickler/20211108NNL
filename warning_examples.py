import warnings

x = 40

if x > 25:
    warnings.warn("number is too high", DeprecationWarning)

print("Done.")