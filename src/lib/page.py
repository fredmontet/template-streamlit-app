from lib.component import Component


class Page:

    def __init__(self, component: Component, **props):
        self.component = component
        self.props = props

    def run(self):
        self.component.run(**self.props)
