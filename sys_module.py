import sys

print(sys.version)
print(sys.version_info)
print(sys.version_info.major, sys.version_info.minor)
print(sys.prefix, sys.executable)
print(sys.platform)

# print(sys.modules.keys())
print(sys.modules['json'])

print("Your hair's on fire")
print("Your hair's on fire", file=sys.stderr)



