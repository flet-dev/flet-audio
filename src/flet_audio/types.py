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
        - On Android, the media player is quite resource-intensive, and this will
        let it go. Data will be buffered again when needed (if it's a remote file,
        it will be downloaded again).
        - On iOS and macOS, works just like [`Audio.release()`][(p).Audio.release] method.
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
    """
    Event triggered when the audio playback state changes.
    """

    state: AudioState
    """The current state of the audio player."""


@dataclass
class AudioPositionChangeEvent(ft.Event[ft.EventControlType]):
    """
    Event triggered when the audio playback position changes.
    """

    position: int
    """The current playback position in milliseconds."""


@dataclass
class AudioDurationChangeEvent(ft.Event[ft.EventControlType]):
    """
    Event triggered when the audio duration changes.
    """

    duration: ft.Duration
    """The duration of the audio."""
