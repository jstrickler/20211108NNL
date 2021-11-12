from john.math import geo
from john import trig
import math

print(geo.circle_area(10))
print(geo.rectangle_area(18, 27))
print(geo.square_area(57))
print(type(geo), type(math))

# where Python finds modules:
# 1. current folder
# 2. PYTHONPATH
# 3. Installed folders
import sys
for path in sys.path:
    print(path)


