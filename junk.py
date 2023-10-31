from packaging.version import Version
from packaging.version import parse

v = Version("1.0.5")

vx = parse(str(v.major) + "." + str(v.minor+1) + "." + str(v.micro))
# vx = list(v)


#vx[1] = vx[1]+1

print(vx)
# = v[1]+1


