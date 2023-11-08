from git import Repo, Actor
from changeversion.versh import VersionHolder, Vershion

class DoGit:

    def tag_version(self, version):
        repo = Repo(".")

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
            origin = repo.remote(name='origin')
#           origin = repo.remotes.origin
            print("PUSHING ...")
            origin.push()
            print("DONE PUSHING")
        except Exception as error:
            print("PUSH FAILED " + error)



    #   origin = repo.remotes.origin
     #  print("PUSHING ...")
       # origin.push(progress=progress)
      # print("DONE PUSHING")

       
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



