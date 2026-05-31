from direct.showbase.ShowBase import ShowBase
from panda3d.core import loadPrcFile

from scenes.menu_scene import MenuScene
from input.input_manager import InputManager
from utils.logger import get_logger

loadPrcFile("config/config.prc")
log = get_logger(__name__)


class App(ShowBase):
    def __init__(self):
        super().__init__()
        log.info("Starting {{PROJECT_NAME}}")

        self.input_manager = InputManager(self)
        self.current_scene = None
        self.switch_scene(MenuScene(self))

    def switch_scene(self, scene):
        if self.current_scene is not None:
            self.current_scene.exit()
        self.current_scene = scene
        self.current_scene.enter()


if __name__ == "__main__":
    App().run()
