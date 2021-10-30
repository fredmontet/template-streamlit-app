class Component:

    def __init__(self, name, func=None):
        self.name = name
        self.func = func
        self.children = []

    def add_child(self, component):
        self.children.append(component)
        return self

    def run(self, **props):
        if self.func is not None:
            return self.func(**props)

        for child in self.children:
            child.run(**props)

    def __repr__(self):
        return repr(self.name)