from gitme import DoGit
from versh import Vershion


version = Vershion.read()
new_version = version.bump("micro")

print("old version %s: v" + version.rep() + " new version %s: v" % new_version.rep())

Vershion.write(new_version)

git = DoGit()
git.tag_version(new_version)
git.git_push()

