
Git-NetworkX
============

Port of https://github.com/hoduche/git-graph to NetworkX
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

----

Install
-------

PyPi
^^^^

``pip install git-networkx``

Git
^^^

``pip install git+https://github.com/CircArgs/git-networkx.git``

Demo
----

.. code-block:: python

   from networkx.drawing.nx_pydot import write_dot
   from git_networkx import GitNX, Commit
   #everything
   All = gnx.GitNX('my/repo/path/that/has/a/.git')
   write_dot(All, "myrepo.dot")

   #Commits
   Commits = gnx.GitNX('my/repo/path/that/has/a/.git', "c")
   write_dot(Commits, "mycommits.dot")

   #which is equivalent to the subgraph obtained by (not in terms of ops)
   [n for n in All if isinstance(n, Commit)]

Node Types
----------

.. list-table::
   :header-rows: 1

   * - Node Type
     - Letter
     - Node Type
     - Letter
   * - blob
     - b
     - remote branch
     - r
   * - tree
     - t
     - remote head
     - d
   * - commit
     - c
     - remote server
     - s
   * - local branch
     - l
     - annotated tag
     - a
   * - local head
     - h
     - tag
     - g
   * - upstream link
     - u


By default all nodes are added to the DiGraph.

.. code-block:: python

   # you can get your commits, branches and the head of your local repo simply with lch
   G=gnx.GitNX('../git_networkx_test/', "lch")
