from git import Repo, Actor,RemoteProgress
from github import Github
import pygit2
from git import Repo
from changeversion.versh import VersionHolder, Vershion
from changeversion.progress import ProgressIndicator

class DoGit:


    def tag_version(self, version):
        repo = Repo(".")

        repo = Repo(".")
        repo.index.add("VERSION")
        repo.index.commit("commitMessage")
        repo.git.push()

        build_id = version.micro()
        print("build_id %s" % build_id)
        index = repo.index
        index.add("VERSION")
        commit = index.commit("changeversion to v" + version.rep())
        print("COMMITTED NEW VERSION " + version.rep())

        repo.create_tag("v" + version.rep(),
                        message="Change version to %s" % version.rep()
        )
        build_id = version.micro()

        repo.create_tag("b%s" % build_id,
                        message="Bump build_id to %s" % build_id
        )

        try:
#            origin = repo.remote(name='origin')
            origin = repo.remotes.origin
            print("PUSHING ...")
            origin.push()
            print("DONE PUSHING")
#        except git.GitCommandError:
#           print("PUSH FAIL " + str(error))
        except Exception as error:
            print("PUSH FAILED " + str(error))


        progress = ProgressIndicator()

        origin = repo.remotes.origin
        print("PUSHING ...")
        origin.push(progress=progress)
        print("DONE PUSHING") 
#        print(progress.allErrorLines())
#        print(progress.allDroppedLines())


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



class Progress(RemoteProgress):
    def __init__( self ):
        super().__init__()

        self.__all_dropped_lines = []

    def update( self, op_code, cur_count, max_count=None, message='' ):
        pass

    def line_dropped( self, line ):
        if line.startswith( 'POST git-upload-pack' ):
            return

        self.__all_dropped_lines.append( line )

    def allErrorLines( self ):
        return self.error_lines() + self.__all_dropped_lines

    def allDroppedLines( self ):
        return self.__all_dropped_lines
