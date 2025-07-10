import asyncio
from typing import Optional

import flet as ft

from .types import (
    AudioDurationChangeEvent,
    AudioPositionChangeEvent,
    AudioStateChangeEvent,
    ReleaseMode,
)


@ft.control("Audio")
class Audio(ft.Service):
    """
    A control to simultaneously play multiple audio sources.

    Raises:
        AssertionError: If both [`src`][(c).] and [`src_base64`][(c).] are `None`.

    Note:
        This control is non-visual and should be added to [`Page.services`][flet.Page.services]
        list before it can be used.
    """

    src: Optional[str] = None
    """
    The audio source. Can be a URL or a local [asset file](https://flet.dev/docs/cookbook/assets).

    Note:
        - At least one of `src` or [`src_base64`][..] must be provided, 
            with `src_base64` having priority if both are provided.
        - [Here](https://github.com/bluefireteam/audioplayers/blob/main/troubleshooting.md#supported-formats--encodings) 
            is a list of supported audio formats.
    """

    src_base64: Optional[str] = None
    """
    Defines the contents of audio file encoded in base-64 format.
    
    Note:
        - At least one of [`src`][..] or `src_base64` must be provided, 
            with `src_base64` having priority if both are provided.
        - [Here](https://github.com/bluefireteam/audioplayers/blob/main/troubleshooting.md#supported-formats--encodings) 
            is a list of supported audio formats.
    """

    autoplay: bool = False
    """
    Starts playing audio as soon as audio control is added to a page.
    
    Note:
        Autoplay works in desktop, mobile apps and Safari browser, but doesn't work in Chrome/Edge.
    """

    volume: ft.Number = 1.0
    """
    Sets the volume (amplitude).
    It's value ranges between `0.0` (mute) and `1.0` (maximum volume). 
    Intermediate values are linearly interpolated.
    """

    balance: ft.Number = 0.0
    """
    Defines the stereo balance.


    * `-1` - The left channel is at full volume; the right channel is silent. 
    * `1` - The right channel is at full volume; the left channel is silent. 
    * `0` - Both channels are at the same volume.
    """

    playback_rate: ft.Number = 1.0
    """
    Defines the playback rate. 
    
    Should ideally be set when creating the constructor.
    
    Note: 
        - iOS and macOS have limits between `0.5x` and `2x`. 
        - Android SDK version should be 23 or higher.
    """

    release_mode: ReleaseMode = ReleaseMode.RELEASE
    """
    Defines the release mode.
    """

    on_loaded: Optional[ft.ControlEventHandler["Audio"]] = None
    """
    Fires when an audio is loaded/buffered.
    """

    on_duration_change: Optional[ft.EventHandler[AudioDurationChangeEvent["Audio"]]] = None
    """
    Fires as soon as audio duration is available (it might take a while to download or buffer it).
    """

    on_state_change: Optional[ft.EventHandler[AudioStateChangeEvent["Audio"]]] = None
    """
    Fires when audio player state changes.
    """

    on_position_change: Optional[ft.EventHandler[AudioPositionChangeEvent["Audio"]]] = None
    """
    Fires when audio position is changed. 
    Will continuously update the position of the playback every 1 second if the status is playing. 
    
    Can be used for a progress bar.
    """

    on_seek_complete: Optional[ft.ControlEventHandler["Audio"]] = None
    """
    Fires on seek completions. 
    An event is going to be sent as soon as the audio seek is finished.
    """

    def before_update(self):
        super().before_update()
        assert self.src or self.src_base64, "either src or src_base64 must be provided"

    async def play_async(self, position: ft.DurationValue = ft.Duration(), timeout: Optional[float] = 10):
        """
        Starts playing audio from the specified `position`.

        Args:
            position: The position to start playback from.
            timeout: The maximum amount of time (in seconds) to wait for a response.
        
        Raises:
            TimeoutError: If the request times out.
        """
        await self._invoke_method_async("play", {"position": position}, timeout=timeout)

    def play(self, position: ft.DurationValue = ft.Duration(), timeout: Optional[float] = 10):
        """
        Starts playing audio from the specified `position`.

        Args:
            position: The position to start playback from.
            timeout: The maximum amount of time (in seconds) to wait for a response.

        Raises:
            TimeoutError: If the request times out.
        """
        asyncio.create_task(self.play_async(position, timeout=timeout))

    async def pause_async(self, timeout: Optional[float] = 10):
        """
        Pauses the audio that is currently playing.

        If you call [`resume()`][(c).resume] or [`resume_async()`][(c).resume_async] later,
        the audio will resume from the point that it has been paused.
        """
        await self._invoke_method_async("pause", timeout=timeout)

    def pause(self, timeout: Optional[float] = 10):
        """
        Pauses the audio that is currently playing.

        If you call [`resume()`][(c).resume] or [`resume_async()`][(c).resume_async] later,
        the audio will resume from the point that it has been paused.

        Args:
            timeout: The maximum amount of time (in seconds) to wait for a response.

        Raises:
            TimeoutError: If the request times out.
        """
        asyncio.create_task(self.pause_async(timeout=timeout))

    async def resume_async(self, timeout: Optional[float] = 10):
        """
        Resumes the audio that has been paused or stopped.

        Args:
            timeout: The maximum amount of time (in seconds) to wait for a response.

        Raises:
            TimeoutError: If the request times out.
        """
        await self._invoke_method_async("resume", timeout=timeout)

    def resume(self, timeout: Optional[float] = 10):
        """
        Resumes the audio that has been paused or stopped.

        Args:
            timeout: The maximum amount of time (in seconds) to wait for a response.

        Raises:
            TimeoutError: If the request times out.
        """
        asyncio.create_task(self.resume_async(timeout=timeout))

    async def release_async(self, timeout: Optional[float] = 10):
        """
        Releases the resources associated with this media player.
        These are going to be fetched or buffered again as soon as
        you change the source or call [`resume()`][(c).resume] or [`resume_async()`][(c).resume_async].

        Args:
            timeout: The maximum amount of time (in seconds) to wait for a response.

        Raises:
            TimeoutError: If the request times out.
        """
        await self._invoke_method_async("release", timeout=timeout)

    def release(self, timeout: Optional[float] = 10):
        """
        Releases the resources associated with this media player.
        These are going to be fetched or buffered again as soon as
        you change the source or call [`resume()`][(c).resume] or [`resume_async()`][(c).resume_async].

        Args:
            timeout: The maximum amount of time (in seconds) to wait for a response.

        Raises:
            TimeoutError: If the request times out.
        """
        asyncio.create_task(self.release_async(timeout=timeout))

    async def seek_async(self, position: ft.DurationValue, timeout: Optional[float] = 10):
        """
        Moves the cursor to the desired position.

        Args:
            position: The position to seek/move to.
            timeout: The maximum amount of time (in seconds) to wait for a response.

        Raises:
            TimeoutError: If the request times out.
        """
        await self._invoke_method_async("seek", {"position": position}, timeout=timeout)

    def seek(self, position: ft.DurationValue, timeout: Optional[float] = 10):
        """
        Moves the cursor to the desired position.

        Args:
            position: The position to seek/move to.
            timeout: The maximum amount of time (in seconds) to wait for a response.

        Raises:
            TimeoutError: If the request times out.
        """
        asyncio.create_task(self.seek_async(position, timeout=timeout))

    async def get_duration_async(self, timeout: Optional[float] = 10) -> Optional[ft.Duration]:
        """
        Get audio duration of the audio playback.

        It will be available as soon as the audio duration is available
        (it might take a while to download or buffer it if file is not local).

        Args:
            timeout: The maximum amount of time (in seconds) to wait for a response.

        Returns:
            The duration of audio playback.

        Raises:
            TimeoutError: If the request times out.
        """
        return await self._invoke_method_async("get_duration", timeout=timeout)

    async def get_current_position_async(self, timeout: Optional[float] = 10) -> Optional[ft.Duration]:
        """
        Get the current position of the audio playback.

        Args:
            timeout: The maximum amount of time (in seconds) to wait for a response.
        Returns:
            The current position of the audio playback.
        """
        return await self._invoke_method_async("get_current_position", timeout=timeout)
