import keyboard
import pyautogui
import os

def count_files(directory):
    file_count = 0
    for _, _, files in os.walk(directory):
        file_count += len(files)
    return file_count

def screenshot_item():
    try:
        # Look for item frame
        TL_x,TL_y,w,h = pyautogui.locateOnScreen("img\\item_frame_TL_rare.png",confidence = 0.8)
        BR_x,BR_y,w,h = pyautogui.locateOnScreen("img\\item_frame_BR_rare.png",confidence = 0.8)
        print("Item found...")

        # Calculate width and height
        w = BR_x + w - TL_x
        h = BR_y - TL_y

        # Take screenshot
        try:
            img = pyautogui.screenshot("screenshots\\item_" + str(count_files("screenshots")) + ".png",region = (TL_x,TL_y,w,h))
            print("screenshot saved")
            print("item_" + str(count_files("screenshots")) + ".png")
        except ValueError:
            print("Error: Bottom right frame corner is further left or higher than top left frame corner.\nThis usually happens when there is more than one item frame on screen.")
    except TypeError:
        print("Error: Item not found...")

def handle_screenshot(e):
    global snip_state
    if not snip_state and keyboard.is_pressed('ctrl') and e.name == 'x':
        screenshot_item()
        snip_state = True

def handle_key_release(e):
    global snip_state
    if snip_state and not keyboard.is_pressed('x') and e.name == 'x':
        snip_state = False

# Once per key stroke limit
snip_state = False

# Event hooks
keyboard.on_press_key('x', handle_screenshot)
keyboard.on_release_key('x', handle_key_release)

# Keep the event listener running
keyboard.wait()