.. role:: raw-html-m2r(raw)
   :format: html


Git-graph
=========

Learn (or teach) Git fast and well - *by visualizing the inner graph of your Git repositories*
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

----


.. image:: doc/sample_full.dot.svg
   :target: doc/sample_full.dot.svg
   :alt: full


..

   `Git is a fast, scalable, distributed revision control system with an unusually rich command set
   that provides both high-level operations and full access to internals. <https://git-scm.com/docs/git>`_


As wonderful as it may be, there is a downside coming with this "unusually rich command set", a kind of anxiety that affects beginners in particular and can be summed up in one question:

..

   "What the hell is going to happen to my repository if I launch this Git command ?"


A good way to overcome this difficulty is to experiment.
This is made easy thanks to Git lightness and the fact it is immediately up and running in any directory with ``git init``.

Git-graph is a Git plugin, written in Python, that displays your Git repository inner content as a `Directed Acyclic Graph <https://en.wikipedia.org/wiki/Directed_acyclic_graph>`_ (DAG).
This structured visual representation of Git internal data demystifies the impact of each Git command and considerably improves the learning curve.

Install
-------

From PyPI
~~~~~~~~~

To install Git-graph from PyPI:


#. You first need to install `Graphviz <https://www.graphviz.org/download/>`_ and check that the dot binary is correctly set in you system's path.  
#. Then run: 
   .. code-block::

       pip install git-graph

From GitHub
~~~~~~~~~~~

To install Git-graph from GitHub:


#. You first need to install `Graphviz <https://www.graphviz.org/download/>`_ and check that the dot binary is correctly set in you system's path.  
#. Then run:
   .. code-block::

       git clone https://github.com/hoduche/git-graph

#. Finally, inside the newly created git-graph folder, run (with Python 3 and setuptools):
   .. code-block::

       python setup.py install

Run
---

As a Git plugin
~~~~~~~~~~~~~~~

Git-graph is a Git plugin that is run from a Git repository with the command:

.. code-block::

   git graph

Running ``git graph`` from a Git repository will:


#. scan your ``.git`` folder
#. build and save a graph representation of the ``.git`` folder internals as text (\ ``.dot``\ ) and image (PDF by default) in a ``.gitGraph`` folder
#. popup a window that displays the image of your graph

A color code helps in distinguishing in the graph the different kinds of object Git is using in its implementation:

.. list-table::
   :header-rows: 1

   * - Object kind
     - Letter
     - Representation
     - Object kind
     - Letter
     - Representation
   * - blob
     - b
     - 
     .. image:: doc/sample_blob.dot.svg
        :target: doc/sample_blob.dot.svg
        :alt: blob
     
     - remote branch
     - r
     - 
     .. image:: doc/sample_remote_branch.dot.svg
        :target: doc/sample_remote_branch.dot.svg
        :alt: remote_branch
     
   * - tree
     - t
     - 
     .. image:: doc/sample_tree.dot.svg
        :target: doc/sample_tree.dot.svg
        :alt: tree
     
     - remote head
     - d
     - 
     .. image:: doc/sample_remote_head.dot.svg
        :target: doc/sample_remote_head.dot.svg
        :alt: remote_head
     
   * - commit
     - c
     - 
     .. image:: doc/sample_commit.dot.svg
        :target: doc/sample_commit.dot.svg
        :alt: commit
     
     - remote server
     - s
     - 
     .. image:: doc/sample_remote_server.dot.svg
        :target: doc/sample_remote_server.dot.svg
        :alt: remote_server
     
   * - local branch
     - l
     - 
     .. image:: doc/sample_local_branch.dot.svg
        :target: doc/sample_local_branch.dot.svg
        :alt: local_branch
     
     - annotated tag
     - a
     - 
     .. image:: doc/sample_annotated_tag.dot.svg
        :target: doc/sample_annotated_tag.dot.svg
        :alt: annotated_tag
     
   * - local head
     - h
     - 
     .. image:: doc/sample_local_head.dot.svg
        :target: doc/sample_local_head.dot.svg
        :alt: local_head
     
     - tag
     - g
     - 
     .. image:: doc/sample_tag.dot.svg
        :target: doc/sample_tag.dot.svg
        :alt: tag
     
   * - upstream link
     - u
     - 
     .. image:: doc/sample_upstream.dot.svg
        :target: doc/sample_upstream.dot.svg
        :alt: upstream
     


By default all nodes are displayed in the output graph when running ``git graph``.
It is possible to only display a user selection of object kinds using the ``-n`` or ``--nodes`` option and picking the letters corresponding to your choice.\ :raw-html-m2r:`<br>`
For instance to only display blobs, trees and commits:

.. code-block::

   git graph -n btc

By default Git-graph considers it is launched from a Git repository.
It is possible to indicate the path to another Git repository with the ``-p`` or ``--path`` option:

.. code-block::

   git graph -p examples/demo

The default output format is PDF.
Other output graphics formats (either vector or raster) can be set with the ``-f`` or ``--format`` option:\ :raw-html-m2r:`<br>`
(the full list of possible formats can be found on the `Graphviz documentation website <https://graphviz.gitlab.io/_pages/doc/info/output.html>`_\ )

.. code-block::

   git graph -f svg

Finally it is possible to prevent the graph image from poping up once constructed, with the ``-c`` or ``--conceal`` option:

.. code-block::

   git graph -c

As a Python program
~~~~~~~~~~~~~~~~~~~

.. code-block::

   python git_graph/cli.py -p examples/demo -n btc -f svg

or

.. code-block::

   ./git_graph/cli.py -p examples/demo -n btc -f svg

As a Python module
~~~~~~~~~~~~~~~~~~

.. code-block:: python

   import git_graph.dot_graph as dg
   dg.DotGraph('..').persist()
   dg.DotGraph('../examples/demo', nodes='btc').persist(form='svg', conceal=True)
