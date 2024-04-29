from pynput import mouse

def on_click(x, y, button, pressed):
    if pressed:
        with open("mouse_positions.txt", "a") as file:
            file.write(f"Mouse clicked at position: {x}, {y}\n")

with mouse.Listener(on_click=on_click) as listener:
    listener.join()