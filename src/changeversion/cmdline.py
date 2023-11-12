import argparse
from changeversion.versh import VersionHolder, Vershion
from changeversion.gitme import DoGit

def main():
    print("Running Change Version ####")

    do_git = DoGit()    

    current_version = Vershion.read()

    print("WORKING OUT NEW VERSION")

    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument("--major") 
    parser.add_argument("--minor")
    parser.add_argument("--micro")
    parser.add_argument("--bump")
    parser.add_argument("--tag", action="store_true")
    args = parser.parse_args()

    new_version = current_version
    if (args.major != None):
        new_version = current_version.set('major', args.major)

    if (args.minor != None):
        new_version = current_version.set('minor', args.minor)
    if (args.micro != None):
        new_version = current_version.set('micro', args.micro)

    if (args.bump != None):
        new_version = current_version.bump(args.bump)

    print("CURRENT_VERSION " + current_version.rep())
    print("NEW_VERSION " + new_version.rep())

    print("WRITING NEW VERSION: " + new_version.rep())        
    Vershion.write(new_version)
    print("DONE WRITING: " + new_version.rep())

    if (args.tag == True):
        print("TAGGING " + new_version.rep())
        do_git.tag_version(new_version)
    else:
        print("I DONT WANT TO TAG")

