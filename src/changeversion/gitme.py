from git import Repo, Actor,RemoteProgress, GitCommandError
from git import Repo
from changeversion.versh import VersionHolder, Vershion

class DoGit:


    def tag_version(self, version):

        print("TAGGING " + version.rep())

        repo = Repo(".")

        repo = Repo(".")
        repo.index.add("VERSION")
        #repo.git.push()

        build_id = version.micro()
        print("build_id %s" % build_id)
        index = repo.index
        index.add("VERSION")
        commit = index.commit("changeversion to v%s" % version.rep() + "  ***NO_CI***")
        print("COMMITTED NEW VERSION " + version.rep())

        repo.create_tag("v%s"  % version.rep(),
                        message="Change version to %s" % version.rep()
        )
        build_id = version.micro()

        repo.create_tag("b%s" % build_id,
                        message="Bump build_id to %s" % build_id
        )

        try:
            print("trying ...")
           #            origin = repo.remote(name='origin')
            #origin = repo.remotes.origin
            #print("PUSHING ...")
            #origin.push("main")
            #repo.git.push('origin', 'HEAD:main')
            # print("DONE PUSHING")
        except GitCommandError:
            print("PUSH FAIL " + str(error))
        except Exception as error:
            print("PUSH FAILED " + str(error))

        origin = repo.remotes.origin
        print("PUSHING ...")
#        origin.push(progress=progress)
        print("DONE PUSHING") 

       #try:
       #     for info in remote.push( progress=progress ):
            # call info_callback with the push commands info
       #     info_callback( info )

       # for line in progress.allDroppedLines():
       #     log.info( line )

       # except GitCommandError:
       #     for line in progress.allErrorLines():
       #     log.error( line )

       #     raise

    def git_push(self):
        repo = Repo(".")
        repo.git.add("VERSION")
        print("pushing to origin")

        origin = repo.remotes.origin
        origin.pull("main")
        print("PUSHING ...")
        origin.push("main")
        print("DONE PUSHING") 
