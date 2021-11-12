# from pkg.pkg import module as alias
from john.math import geo as g
# find geo.py in john/math  in one of the folders in sys.path
import lxml.etree as et

result = g.circle_area(15)
print(result)


root_tag = et.Element('presidents')
# root_tag = lxml.etree.Element('presidents')
