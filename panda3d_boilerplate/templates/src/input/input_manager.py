from utils.logger import get_logger

log = get_logger(__name__)


class InputManager:
    def __init__(self, app):
        self.app = app
        self._bind_defaults()

    def _bind_defaults(self):
        self.app.accept("escape", self.app.userExit)
        log.debug("Default keybinds registered")

    def bind(self, key, callback, *args):
        self.app.accept(key, callback, list(args))
