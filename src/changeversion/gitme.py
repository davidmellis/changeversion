from git import Repo, Actor
from changeversion.versh import VersionHolder

class DoGit:
    def play(self):

        repo = Repo(".")

        file=open("VERSION","r")
        version_number = file.read()

        current_version = VersionHolder(version_number)
        print(current_version.rep())

        new_version = current_version.bump('micro')
        f = open("VERSION", "w")
        f.write(new_version.rep())
        f.close()

        version = new_version

#        repo.create_tag("v" + version,
#                        message="This is a tag-object pointing to %s" % "new_branch",
#        )
        index = repo.index
        author = Actor("An author", "author@example.com")
        committer = Actor("A committer", "committer@example.com")
        # commit by commit message and author and committer
        index.add('VERSION')
        index.commit("changeversion to v" + version.rep())

        print("COMMITTED NEW VERSION " + version.rep())

        origin = repo.remotes.origin
        print("PUSHING ...")
        origin.push()
        print("DONE PUSHING")

DoGit().play()

