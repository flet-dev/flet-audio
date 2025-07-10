from dataclasses import dataclass, field
from enum import Enum

import flet as ft

__all__ = [
    "AudioState",
    "AudioStateChangeEvent",
    "AudioPositionChangeEvent",
    "AudioDurationChangeEvent",
    "ReleaseMode",
]


class ReleaseMode(Enum):
    """The behavior of Audio player when an audio is finished or stopped."""

    RELEASE = "release"
    """
    Releases all resources, just like calling release method.

    Info:
        - In Android, the media player is quite resource-intensive, and this will
        let it go. Data will be buffered again when needed (if it's a remote file,
        it will be downloaded again).
        - In iOS and macOS, works just like [`Audio.stop()`][(p).Audio.stop] method.
    """

    LOOP = "loop"
    """
    Keeps buffered data and plays again after completion, creating a loop.
    Notice that calling stop method is not enough to release the resources
    when this mode is being used.
    """

    STOP = "stop"
    """
    Stops audio playback but keep all resources intact.
    Use this if you intend to play again later.
    """


class AudioState(Enum):
    """The state of the audio player."""
    STOPPED = "stopped"
    """The audio player is stopped."""

    PLAYING = "playing"
    """The audio player is currently playing audio."""

    PAUSED = "paused"
    """The audio player is paused and can be resumed."""

    COMPLETED = "completed"
    """The audio player has successfully reached the end of the audio."""

    DISPOSED = "disposed"
    """The audio player has been disposed of and should not be used anymore."""


@dataclass
class AudioStateChangeEvent(ft.Event[ft.EventControlType]):
    state: AudioState


@dataclass
class AudioPositionChangeEvent(ft.Event[ft.EventControlType]):
    position: int


@dataclass
class AudioDurationChangeEvent(ft.Event[ft.EventControlType]):
    duration: int
