"""Sprite sheet module"""

import pygame


class SpriteSheet:
    """Class to handle sprite sheets"""

    def __init__(
        self,
        img: pygame.Surface,
        horizontal_frames: int = 1,
        vertical_frames: int = 1,
        frame: tuple[int, int] = (0, 0),
    ) -> None:
        self._img = img

        # number of frames horizontally and vertically
        self._h_frames = max(1, min(abs(horizontal_frames), self._img.get_width()))
        self._v_frames = max(1, min(abs(vertical_frames), self._img.get_height()))

        # frame size
        self._frame_widht = self._img.get_width() // self._h_frames
        self._frame_height = self._img.get_height() // self._v_frames

        # number of total frames
        self._total_frames = (
            self._img.get_width()
            // self._frame_widht
            * self._img.get_height()
            // self._frame_height
        )
        # start frame
        self._frame_cord = (
            frame[0] % self._h_frames,
            frame[1] % self._v_frames,
        )

    @property
    def image(self):
        """Return sprite image"""
        return self._img

    @property
    def frame(self):
        """Return currente frame image"""
        return self._img.subsurface(
            self._frame_cord[0] * self._frame_widht,
            self._frame_cord[1] * self._frame_height,
            self._frame_widht,
            self._frame_height,
        )

    @property
    def frame_cord(self) -> tuple[int, int]:
        """Get currente frame cordinates"""
        return self._frame_cord

    def set_frame_cord(self, value: tuple[int, int]):
        """Sets new frame cordinates"""
        self._frame_cord = (value[0] % self._h_frames, value[1] % self._v_frames)

    @property
    def horizontal_cord(self) -> int:
        """Get current frame horizontal cordinate"""
        return self._frame_cord[0]

    @horizontal_cord.setter
    def horizontal_cord(self, value: int):
        """Sets new frame horizontal cordinate"""
        self._frame_cord = (value % self._h_frames, self._frame_cord[1])

    @property
    def vertical_cord(self) -> int:
        """Get current frame vertical cordinate"""
        return self._frame_cord[1]

    @vertical_cord.setter
    def vertical_cord(self, value: int):
        """Sets new frame vertical cordinate"""
        self._frame_cord = (self._frame_cord[0], value % self._v_frames)

    @property
    def total_frames(self) -> int:
        """Return number of total frames"""
        return self._total_frames

    @property
    def horizontal_len(self) -> int:
        """Return number of horizontal frames"""
        return self._h_frames

    @property
    def vertical_len(self) -> int:
        """Return number of vertical frames"""
        return self._v_frames
    
    def __len__(self) -> int:
        """Return number of total frames"""
        return self._total_frames

    def __getitem__(self, key: tuple[int, int]):
        """Return currente frame image"""
        return self._img.subsurface(
            (key[0] % self._h_frames) * self._frame_widht,
            (key[1] % self._v_frames) * self._frame_height,
            self._frame_widht,
            self._frame_height,
        )
