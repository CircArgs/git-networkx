

class BaseNode:
    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return repr(self.data)

    def __str__(self):
        return str(self.data)

    def __eq__(self, other):
        if not isinstance(other, BaseNode):
            return False
        return self.data == other.data
    def __hash__(self):
        return self.data.__hash__()

class Blob(BaseNode):
    pass


class RemoteBranch(BaseNode):
    pass


class Tree(BaseNode):
    pass


class RemoteHead(BaseNode):
    pass


class Commit(BaseNode):
    pass


class RemoteServer(BaseNode):
    pass


class LocalBranch(BaseNode):
    pass


class AnnotatedTag(BaseNode):
    pass


class LocalHead(BaseNode):
    pass


class Tag(BaseNode):
    pass


# class Upstream(BaseNode):
#     pass
