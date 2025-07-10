import logging

import flet as ft

import flet_audio as fta

logging.basicConfig(level=logging.INFO)

def main(page: ft.Page):

    url = "https://github.com/mdn/webaudio-examples/blob/main/audio-analyser/viper.mp3?raw=true"
    
    def volume_down(_):
        audio1.volume -= 0.1

    def volume_up(_):
        audio1.volume += 0.1

    def balance_left(_):
        audio1.balance -= 0.1

    def balance_right(_):
        audio1.balance += 0.1

    audio1 = fta.Audio(
        src=url,
        autoplay=False,
        volume=1,
        balance=0,
        on_loaded=lambda _: print("Loaded"),
        on_duration_change=lambda e: print("Duration changed:", e.duration),
        on_position_change=lambda e: print("Position changed:", e),
        on_state_change=lambda e: print("State changed:", e.state),
        on_seek_complete=lambda _: print("Seek complete"),
    )
    page.services.append(audio1)

    async def on_play(e):
        await audio1.play_async()

    async def on_get_duration(e):
        duration = await audio1.get_duration_async()
        print("Duration:", duration)

    async def on_get_current_position(e):
        position = await audio1.get_current_position_async()
        print("Current position:", position)

    page.add(
        ft.ElevatedButton("Play", on_click=on_play),
        ft.ElevatedButton("Pause", on_click=lambda _: audio1.pause()),
        ft.ElevatedButton("Resume", on_click=lambda _: audio1.resume()),
        ft.ElevatedButton("Release", on_click=lambda _: audio1.release()),
        ft.ElevatedButton("Seek 2s", on_click=lambda _: audio1.seek(2000)),
        ft.Row(
            [
                ft.ElevatedButton("Volume down", on_click=volume_down),
                ft.ElevatedButton("Volume up", on_click=volume_up),
            ]
        ),
        ft.Row(
            [
                ft.ElevatedButton("Balance left", on_click=balance_left),
                ft.ElevatedButton("Balance right", on_click=balance_right),
            ]
        ),
        ft.ElevatedButton("Get duration", on_click=on_get_duration),
        ft.ElevatedButton("Get current position", on_click=on_get_current_position),
    )


ft.run(main)
