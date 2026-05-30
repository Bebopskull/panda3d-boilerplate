from direct.gui.OnscreenText import OnscreenText
from panda3d.core import TextNode

from scenes.base_scene import BaseScene


class MenuScene(BaseScene):
    def enter(self):
        self.title = OnscreenText(
            text="{{PROJECT_NAME}}",
            pos=(0, 0.2),
            scale=0.15,
            align=TextNode.ACenter,
            mayChange=False,
        )
        self.hint = OnscreenText(
            text="Press ESC to quit",
            pos=(0, -0.1),
            scale=0.06,
            align=TextNode.ACenter,
            mayChange=False,
        )

    def exit(self):
        self.title.destroy()
        self.hint.destroy()
        super().exit()
