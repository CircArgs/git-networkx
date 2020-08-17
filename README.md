# Git-NetworkX

### Port of https://github.com/hoduche/git-graph to NetworkX

---

## Install

### PyPi

`pip install git-networkx`

### Git

`pip install git+https://github.com/CircArgs/git-networkx.git`

## Demo

```python
from networkx.drawing.nx_pydot import write_dot
from git_networkx import GitNX, Commit
#everything
All = GitNX('my/repo/path/that/has/a/.git')
#networkx Digraph representing all nodes of the git repo

#Commits
Commits = GitNX('my/repo/path/that/has/a/.git', "c")
write_dot(Commits, "mycommits.dot")
#networkx Digraph representing only commits of the git repo

#which is equivalent to the subgraph obtained by (not in terms of ops)
[n for n in All if isinstance(n, Commit)]

```

#### Suppose you had a log like the following:

```
commit 9a99a4d85cb14005ca829e2cab8f626b4034b981 (HEAD -> master, dev)
Author: CircArgs <quebecname@gmail.com>
Date:   Fri Aug 14 22:05:30 2020 -0400

    I like dogs

commit 80798c310455976e08fedd9b367794692ebb54a6
Author: CircArgs <quebecname@gmail.com>
Date:   Fri Aug 14 22:04:58 2020 -0400

    add file2 with text

commit 8c7f9cea1f6323d793cd035e2178636d6ebf0a36
Author: CircArgs <quebecname@gmail.com>
Date:   Fri Aug 14 22:04:28 2020 -0400

    add file 1

```

then

```python
G=GitNX(".", "lch")

print(list(G.neighbors(Commit("80798c310455976e08fedd9b367794692ebb54a6"))))
# [Commit('8c7f9cea1f6323d793cd035e2178636d6ebf0a36')]

print(list(G.predecessors(Commit("80798c310455976e08fedd9b367794692ebb54a6"))))
# [Commit('9a99a4d85cb14005ca829e2cab8f626b4034b981')]

print(list(G.predecessors(Commit('9a99a4d85cb14005ca829e2cab8f626b4034b981'))))
# [LocalBranch('dev'), LocalBranch('master')]
```

## Nodes

This table shows what nodes can be in a graph. The `Letter`s denote the filters for creation of the graph as the second positional argument to `git_networkx.GitNX` i.e. the `nodes` argument.

As shown in above examples, the `DiGraph` from `GitNX` can be filtered by checking `isinstance` against the Node Classes below or by filtering by a an instance of one of the classes.

Overall Node Class: `GitNode`

| Node kind    | Letter | Node Class  | Node kind     | Letter | Node Class   |
| ------------ | :----: | ----------- | ------------- | :----: | ------------ |
| blob         |   b    | Blob        | remote branch |   r    | RemoteBranch |
| tree         |   t    | Tree        | remote head   |   d    | RemoteHead   |
| commit       |   c    | Commit      | remote server |   s    | RemoteServer |
| local branch |   l    | LocalBranch | annotated tag |   a    | AnnotatedTag |
| local head   |   h    | LocalHead   | tag           |   g    | Tag          |

By default all nodes are added to the DiGraph.

```python
# you can get your commits, branches and the head of your local repo simply with lch
G=GitNX('../git_networkx_test/', "lch")

```
