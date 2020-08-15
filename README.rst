
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
   All = GitNX('my/repo/path/that/has/a/.git')
   write_dot(All, "myrepo.dot")

   #Commits
   Commits = GitNX('my/repo/path/that/has/a/.git', "c")
   write_dot(Commits, "mycommits.dot")

   #which is equivalent to the subgraph obtained by (not in terms of ops)
   [n for n in All if isinstance(n, Commit)]

Suppose you had a log like the following:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

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

then

.. code-block:: python

   G=GitNX(".", "lch")

   print(list(G.neighbors(Commit("80798c310455976e08fedd9b367794692ebb54a6"))))
   # [Commit('8c7f9cea1f6323d793cd035e2178636d6ebf0a36')]

   print(list(G.predecessors(Commit("80798c310455976e08fedd9b367794692ebb54a6"))))
   # [Commit('9a99a4d85cb14005ca829e2cab8f626b4034b981')]

   print(list(G.predecessors(Commit('9a99a4d85cb14005ca829e2cab8f626b4034b981'))))
   # [LocalBranch('dev'), LocalBranch('master')]

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
   G=GitNX('../git_networkx_test/', "lch")
