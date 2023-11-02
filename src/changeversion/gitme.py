from git import Repo, Actor
from changeversion.versh import VersionHolder

class DoGit:

    def tag_version(self, version):
        repo = Repo(".")

        build_id = version.micro()
        print("build_id %s" % build_id)
        index = repo.index
        index.commit("changeversion to v" + version.rep())

        repo.create_tag("v" + version.rep(),
                        message="Bump version to %s" % version.rep()
        )
        build_id = version.micro()

        repo.create_tag("b%s" % build_id,
                        message="Bump build_id to %s" % build_id
        )
 
        origin = repo.remotes.origin
        print("PUSHING ...")
        origin.push()
        print("DONE PUSHING")





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


