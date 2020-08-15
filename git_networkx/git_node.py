

class GitNode:
    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return self.__name__+"("+repr(self.data)+")"

    def __str__(self):
        return repr(self)

    def __eq__(self, other):
        if not isinstance(other, GitNode):
            return False
        return self.data == other.data
    def __hash__(self):
        return self.data.__hash__()

class Blob(GitNode):
    pass


class RemoteBranch(GitNode):
    pass


class Tree(GitNode):
    pass


class RemoteHead(GitNode):
    pass


class Commit(GitNode):
    pass


class RemoteServer(GitNode):
    pass


class LocalBranch(GitNode):
    pass


class AnnotatedTag(GitNode):
    pass


class LocalHead(GitNode):
    pass


class Tag(GitNode):
    pass


# class Upstream(GitNode):
#     pass
