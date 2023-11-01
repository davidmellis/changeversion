from git import Repo

class DoGit:
    def play(self):

        repo = Repo(".")

        repo.create_tag("past",
                        message="This is a tag-object pointing to %s" % "new_branch",
)


DoGit().play()

