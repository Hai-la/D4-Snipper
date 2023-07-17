import keyboard
import pyautogui
import os
import configparser

def count_files(directory):
    file_count = 0
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.isfile(file_path):
                file_count += 1
    return file_count

def screenshot_item():
    try:
        # Look for normal rare item frame
        TL_x,TL_y,_,_ = pyautogui.locateOnScreen("img\\item_frame_TL_rare.png",confidence = 0.8)
        BR_x,BR_y,w2,_ = pyautogui.locateOnScreen("img\\item_frame_BR_rare.png",confidence = 0.8)
        print("Item found...")

        # Calculate width and height
        w = BR_x + w2 - TL_x
        h = BR_y - TL_y

        # Take screenshot
        try:
            file_num = str(count_files("screenshots")+1)
            img = pyautogui.screenshot("screenshots\\item_" + file_num + ".png",region = (TL_x,TL_y,w,h))
            print("Screenshot saved: "+"item_" + file_num + ".png")
        except ValueError:
            print("Error: Bottom right frame corner is further left or higher than top left frame corner.\nThis usually happens when there is more than one item frame on screen.")
    except TypeError:
        try:
            # Look for scrollable rare item frame
            BR_x,BR_y,w2,h2 = pyautogui.locateOnScreen("img\\item_frame_BR_rare_scrollable.png",confidence = 0.8)
            print("Item found")

            # Calculate width and height
            w = BR_x + w2 - TL_x
            h = ((BR_y + h2) - 5) - TL_y

            # Take screenshot
            try:
                file_num = str(count_files("screenshots")+1)
                img = pyautogui.screenshot("screenshots\\item_" + file_num + ".png",region = (TL_x,TL_y,w,h))
                print("Screenshot saved: "+"item_" + file_num + ".png")
            except ValueError:
                print("Error: Bottom right frame corner is further left or higher than top left frame corner.\nThis usually happens when there is more than one item frame on screen.")
        except:
            print("Error: Item not found...")

def handle_screenshot(e):
    global snip_state
    if not snip_state and keyboard.is_pressed(modifier_key) and e.name == rare_snip_key:
        screenshot_item()
        snip_state = True

def handle_key_release(e):
    global snip_state
    if snip_state and not keyboard.is_pressed(rare_snip_key) and e.name == rare_snip_key:
        snip_state = False

# Once per key stroke limit
snip_state = False

# Read config
config = configparser.ConfigParser()
config.read("config.ini")
rare_snip_key = config.get('Keybindings', 'rare_snip_key')
modifier_key = config.get('Keybindings', 'modifier_key')

# Start-up dialog
print("--- Welcome to D4S ---\nTo snip a rare item, hover over it, hold " + modifier_key + ", and press " + rare_snip_key + "\nKeybindings can be changed in config.ini")

# Event hooks
keyboard.on_press_key(rare_snip_key, handle_screenshot)
keyboard.on_release_key(rare_snip_key, handle_key_release)

# Keep the event listener running
keyboard.wait()