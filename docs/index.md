# flet-audio

[![pypi](https://img.shields.io/pypi/v/flet-audio.svg)](https://pypi.python.org/pypi/flet-audio)
[![downloads](https://static.pepy.tech/badge/flet-audio/month)](https://pepy.tech/project/flet-audio)
[![license](https://img.shields.io/github/license/flet-dev/flet-audio.svg)](https://github.com/flet-dev/flet-audio/blob/main/LICENSE)

A [Flet](https://flet.dev) extension package for displaying audio animations.

It is based on the [audioplayers](https://pub.dev/packages/audioplayers) Flutter package.

## Platform Support

This package supports the following platforms:

| Platform | Supported |
|----------|:---------:|
| Windows  |     ✅     |
| macOS    |     ✅     |
| Linux    |     ✅     |
| iOS      |     ✅     |
| Android  |     ✅     |
| Web      |     ✅     |

## Usage

### Installation

To install the `flet-audio` package and add it to your project dependencies:

=== "uv"
    ```bash
    uv add flet-audio
    ```

=== "pip"
    ```bash
    pip install flet-audio  # (1)!
    ```

    1. After this, you will have to manually add this package to your `requirements.txt` or `pyproject.toml`.

=== "poetry"
    ```bash
    poetry add flet-audio
    ```

??? note "Windows Subsystem for Linux (WSL)"
    On WSL, you need to install [`GStreamer`](https://github.com/GStreamer/gstreamer) library.
    
    If you receive `error while loading shared libraries: libgstapp-1.0.so.0`, 
    it means `GStreamer` is not installed in your WSL environment.
    
    To install it, run the following command:
    
    ```bash
    apt install -y libgstreamer1.0-0 gstreamer1.0-plugins-base gstreamer1.0-plugins-good gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly gstreamer1.0-libav gstreamer1.0-tools
    ```

## Example

```python title="main.py"
--8<-- "examples/audio_example/src/main.py"
``` 
