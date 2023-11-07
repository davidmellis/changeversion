from packaging.version import Version, parse

class VersionParts:
    def __init__(self, major, minor, micro):
        self.parts = {}
        self.parts["major"] = major
        self.parts["minor"] = minor
        self.parts["micro"] = micro

    def bump(self, type):
        self.parts[type] += 1
        return self

    def set(self, type, val):
        self.parts[type] = val
        return self

    def major(self):
        return self.parts["major"]

    def minor(self):
        return self.parts["minor"]

    def micro(self):
        return self.parts["micro"]



    def to_string(self):
        return str(self.parts["major"]) + "." + str(self.parts["minor"]) + "." + str(self.parts["micro"])
class VersionHolder:
    def __init__(self, vstr):
        self.version = Version(vstr)
        self.parts = VersionParts(self.version.major, self.version.minor, self.version.micro)

    def rep(self) -> str:
        return str(self.version)

    def bump(self, value):
        v = self.parts.bump(value)
        return VersionHolder(self.parts.to_string())

    def set(self, part, vstr):
        return VersionHolder(self.parts.set(part, vstr).to_string())

    def micro(self):
        return self.parts.micro()

    def minor(self):
        return self.parts.minor()

    def major(self):
        return self.parts.major()


class Vershion:
    @classmethod
    def read(cls, file="VERSION"):
        file=open("VERSION","r")
        version_number = file.read()
        return VersionHolder(version_number)

    @classmethod
    def write(cls, version, file="VERSION"):
        f = open(file, "w")
        f.write(version.rep())
        f.close()

