# Git-NetworkX

### Port of https://github.com/hoduche/git-graph to NetworkX
___

```python
from networkx.drawing.nx_pydot import write_dot
import git_networkx.git_networkx as gnx
#everything
All = gnx.GitNX('my/repo/path/that/has/a/.git')
write_dot(All, "myrepo.dot")

#Commits
Commits = gnx.GitNX('my/repo/path/that/has/a/.git', "c")
write_dot(Commits, "mycommits.dot")

```
