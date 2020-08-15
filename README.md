# Git-NetworkX

### Port of https://github.com/hoduche/git-graph to NetworkX
___

```python
from networkx.drawing.nx_pydot import write_dot
import git_networkx.git_networkx as gnx
G = gnx.GitNX('..')
write_dot(G, "myrepo.dot")
```
