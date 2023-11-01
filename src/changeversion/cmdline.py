import argparse
from changeversion.versh import VersionHolder

class MyAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):

        # Set optional arguments to True or False
        if option_string:
            attr = True if values else False
            setattr(namespace, self.dest, attr)

        # Modify value of "input" in the namespace
        if hasattr(namespace, 'input'):
            current_values = getattr(namespace, 'input')
            try:
                current_values.extend(values)
            except AttributeError:
                current_values = values
            finally:
                setattr(namespace, 'input', current_values)
        else:
            setattr(namespace, 'input', values)


def main():
    print("Running Change Version ####")

    file=open("VERSION","r")
    version_number = file.read()

    current_version = VersionHolder(version_number)
    print(current_version.rep())

    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument("--major") 
    parser.add_argument("--minor")
    parser.add_argument("--micro")
    parser.add_argument("--bump")
    args = parser.parse_args()

    if (args.major != None):
        new_version = current_version.set('major', args.major)
    if (args.minor != None):
        new_version = current_version.set('minor', args.minor)
    if (args.micro != None):
        new_version = current_version.set('micro', args.micro)
    if (args.bump != None):
        new_version = current_version.bump(args.bump)

    f = open("VERSION", "w")
    f.write(new_version.rep())
    f.close()

    print("CURRENT_VERSION " + current_version.rep())
    print("NEW_VERSION " + new_version.rep())
