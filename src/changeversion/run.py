from changeversion.progress import ProgressIndicator
from changeversion.gitme import DoGit
from changeversion.versh import VersionHolder, Vershion

gitme = DoGit()

v = VersionHolder("9.0.17")

gitme.tag_version(v)
