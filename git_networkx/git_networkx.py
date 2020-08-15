import datetime
import os
import networkx as nx
from .git_node import *
import git_graph.git_graph_class as gg
from copy import deepcopy

CURRENT_FOLDER = "."

ALL = "all"
COMMITS = "commits"
BRANCHES = "branches"

ALL_NODES = "dchatsglurb"
COMMIT_NODES = ALL_NODES.replace("b", "").replace("t", "")
BRANCH_NODES = COMMIT_NODES.replace("c", "")


def handle_specific_node_sets(nodes=ALL_NODES):
    if nodes == ALL:
        result = ALL_NODES
    elif nodes == COMMITS:
        result = COMMIT_NODES
    elif nodes == BRANCHES:
        result = BRANCH_NODES
    else:
        result = nodes
    return result


def filter_nodes(git_graph, nodes=ALL_NODES):
    node_set = set()
    if "b" in nodes:
        node_set.update(git_graph.blobs)
    if "t" in nodes:
        node_set.update(git_graph.trees)
    if "c" in nodes:
        node_set.update(git_graph.commits)
    if "l" in nodes:
        node_set.update(git_graph.local_branches)
    if "h" in nodes:
        node_set.update(git_graph.local_head[0])
    if "r" in nodes:
        node_set.update(git_graph.remote_branches)
    if "d" in nodes:
        node_set.update(git_graph.remote_heads)
    if "s" in nodes:
        node_set.update(git_graph.remote_servers)
    if "a" in nodes:
        node_set.update(git_graph.annotated_tags)
    if "g" in nodes:
        node_set.update(git_graph.tags)
    if "u" in nodes:
        pass
    return node_set


def resolve_child_type(node, parent, gg):
    if isinstance(parent, Tree):
        return Blob

    if isinstance(parent, Commit):
        if node in gg.commits:
            return Commit
        else:
            return Tree

    if isinstance(parent, Blob):
        return None

    if isinstance(parent, LocalBranch):
        return Commit

    if isinstance(parent, RemoteBranch):
        if node in gg.local_branches:
            return LocalBranch
        else:
            return Commit

    if isinstance(parent, RemoteServer):
        if node in gg.remote_heads:
            return RemoteHead
        else:
            return LocalBranch

    if isinstance(parent, Tag):
        if node in gg.commits:
            return Commit
        else:
            return AnnotatedTag

    if isinstance(parent, AnnotatedTag):
        return Commit

    if isinstance(parent, LocalHead):
        return LocalBranch

    if isinstance(parent, RemoteHead):
        return RemoteBranch

import pdb
class GitNX(nx.DiGraph):
    def __init__(self, git_path, nodes=ALL_NODES):
        super().__init__()
        self.git_path = git_path
        git_graph = gg.GitGraph(self.git_path).build_graph()
        self.git_graph=git_graph
        nodes = handle_specific_node_sets(nodes)
        node_set = filter_nodes(git_graph, nodes)
        if "b" in nodes:
            for _b in git_graph.blobs:
                self.add_node(Blob(_b))
        if "t" in nodes:
            for _t in git_graph.trees:
                t = Tree(_t)
                self.add_node(t)
                for e in git_graph.trees[_t]:
                    if e[0] in node_set:
                        self.add_edge(t, resolve_child_type(e, t, git_graph)(e[0]))
        if "c" in nodes:
            for _c in git_graph.commits:
                c = Commit(_c)
                self.add_node(c)
                for _e in git_graph.commits[_c]:
                    if _e in node_set:
                        self.add_edge(c, resolve_child_type(_e, c, git_graph)(_e))
        if "l" in nodes:
            for _l in git_graph.local_branches:
                l = LocalBranch(_l)
                self.add_node(l)
                e = git_graph.local_branches[_l]
                if e in node_set:
                    self.add_edge(l, resolve_child_type(e, l, git_graph)(e))
        if "h" in nodes:
            h = git_graph.local_head[0]
            h = LocalHead(h)
            self.add_node(h)
            e = git_graph.local_head[1]
            if e in node_set:
                self.add_edge(h, resolve_child_type(e, h, git_graph)(e))
        if "r" in nodes:
            for _r in git_graph.remote_branches:
                r = RemoteBranch(_r)
                self.add_node(r)
                e = git_graph.remote_branches[_r]
                if e in node_set:
                    self.add_edge(r, resolve_child_type(e, r, git_graph)(e))
        if "d" in nodes:
            for _d in git_graph.remote_heads:
                d = RemoteHead(_d)
                self.add_node(d)
                e = git_graph.remote_heads[_d]
                if e in node_set:
                    self.add_edge(d, resolve_child_type(e, d, git_graph)(e))
        if "s" in nodes:
            for _s in git_graph.remote_servers:
                s = RemoteServer(_s)
                self.add_node(s)
                for _e in git_graph.remote_servers[_s]:
                    if _e in node_set:
                        self.add_edge(s, resolve_child_type(_e, s, git_graph)(_e))
        if "a" in nodes:
            for _a in git_graph.annotated_tags:
                a = AnnotatedTag(_a)
                self.add_node(a)
                e = git_graph.annotated_tags[_a]
                if e in node_set:
                    self.add_edge(a, resolve_child_type(e, a, git_graph)(e))
        if "g" in nodes:
            for _g in git_graph.tags:
                g = Tag(_g)
                self.add_node(g)
                e = git_graph.tags[_g]
                if e in node_set:
                    self.add_edge(g, resolve_child_type(e, g, git_graph)(e))
        # if "u" in nodes:  # no color (only edges)
        #     for u in git_graph.upstreams:
        #         e = git_graph.upstreams[u]
        #         if e in node_set:
        #             self.add_edge(u, resolve_child_type(e, u, git_graph)(e))
