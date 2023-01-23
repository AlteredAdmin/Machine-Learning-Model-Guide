import pyautogui
import time

for i in range(1000):
    # Take a screenshot
    img = pyautogui.screenshot()
    img.save(f'screenshots/screenshot{i}.png')

    # # Get the coordinates of the mouse cursor
    # x, y = pyautogui.position()

    # # Save the coordinates to a file
    # with open(f'screenshots/coordinates{i}.txt', 'w') as f:
    #     f.write(f'{x}, {y}')

    time.sleep(0.5)
