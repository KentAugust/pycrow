"""Config
module for setting different type of configuration needed for other classes"""

from dataclasses import dataclass
from typing import Any, NamedTuple, Protocol

import pygame

from .consts import ScaleFuntions


@dataclass
class WindowConfig: # pylint: disable=R0902
    """Window configuration class"""

    window_size: tuple[int, int]
    scale_factor: float = 1.0
    scale_funtion: ScaleFuntions = ScaleFuntions.NEAREST
    avalible_window_sizes: list[tuple[int, int]] | None = None
    depth: int = 0
    vsync: int = 0
    can_fullscreen: bool = True
    can_resize: bool = True


@dataclass
class GameConfig:
    """Game configuration class"""

    title: str = "Pygame Window"
    target_fps: int = 0
    start_fullscreen: bool = False
    clean_color: tuple[int, int, int] = (0, 0, 0)


class Window(Protocol):
    """Window Protocol"""

    display: pygame.Surface
    config: WindowConfig

    def __init__(self, config: WindowConfig) -> None:
        ...

    def update_display(self):
        """Render to the screen"""

    def update_win_size(self, size_option: int):
        """Update window size with if the option is avalible in disktop sizes"""

    def toggle_fullscreen(self):
        """Turn on/off fullscreen"""

    def clean(self, bg_color: pygame.Color):
        """fills the screen/display with the given color"""


class Game(Protocol):
    """General class that represent the game"""

    config: GameConfig
    window: Window
    clock: pygame.Clock

    def __init__(self, config: GameConfig, window: Window) -> None:
        ...

    def run(self):
        """Run the main game loop"""

    def set_title(self, title="Pygame Window", icontitle: str | None = None):
        """Set window title"""

    def quit(self):
        """Quit pygame and exit"""


class CallableScene(NamedTuple):
    """Class to store a scene class and its arguments"""

    scene_class: "Scene2D"
    kwargs: dict[str, Any]


class SceneManager(Protocol):
    """Class for hanglind scenes"""

    actual_scene: "Scene2D"
    actual_scene_name: str

    def __init__(
        self, game: Game, initial_scene: CallableScene, initial_scene_name: str
    ) -> None:
        ...

    def update(self, dt: float):
        """Update current scene"""

    def reder(self, display: pygame.Surface):
        """Render current scene"""

    def add_scene(self, name: str, scene: CallableScene):
        """Adds new scene to scenes"""

    def remove_scene(self, name: str):
        """Removes scene from scenes"""

    def change_scene(self, name: str):
        """Method to change scenes if name is avalible in scenes"""

    def scenes_names(self) -> set:
        "Get all scenes names"


class Scene2D(Protocol):
    """Abstract Class representing a single game scene"""

    game: Game

    def __init__(self, game: Game) -> None:
        ...

    def on_enter_update(self, dt) -> bool:
        """Ativate when enter the scene and return True when finish"""

    def on_exit_update(self, dt) -> bool:
        """Ativate when exit the scene and return True when finish"""

    def on_enter_render(self, display: pygame.Surface):
        """Render when enter the scene"""

    def on_exit_render(self, display: pygame.Surface):
        """Render when exit the scene"""

    def set_scene_manager(self, scene_manager: SceneManager):
        """Set scene manager"""

    def update(self, dt: float):
        """For updating stuff"""

    def render(self, display: pygame.Surface):
        """For rendering stuff"""
