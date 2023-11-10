import git
import pprint

class ProgressIndicator(git.RemoteProgress):
    def __init__( self ):
        super().__init__()

        self.__all_dropped_lines = []

    def update( self, op_code, cur_count, max_count=None, message='' ):


        elems = [
             str(op_code),
             str(cur_count),
             str(max_count),
             str(cur_count / (max_count or 100.0)),
             message or "NO MESSAGE"
        ]

        strg = ' '.join(elems)

        print(strg)

        return

    def line_dropped( self, line ):
        if line.startswith( 'POST git-upload-pack' ):
            return

        self.__all_dropped_lines.append( line )

    def allErrorLines( self ):
        return self.error_lines() + self.__all_dropped_lines

    def allDroppedLines( self ):
        return self.__all_dropped_lines
