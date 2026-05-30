class BaseScene:
    def __init__(self, app):
        self.app = app
        self.root = app.render.attachNewNode("scene_root")

    def enter(self):
        pass

    def exit(self):
        self.root.removeNode()
