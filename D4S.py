import keyboard
import pyautogui

def screenshot_item():
    try:
        TL_x,TL_y,w,h = pyautogui.locateOnScreen("img\\item_frame_TL_rare.png",confidence = 0.8)
        BR_x,BR_y,w,h = pyautogui.locateOnScreen("img\\item_frame_BR_rare.png",confidence = 0.8)
        w = BR_x+w - TL_x
        h = BR_y - TL_y
        img = pyautogui.screenshot("screenshots\\item.png",region = (TL_x,TL_y,w,h))
    except TypeError:
        print("Item not found...")

# Initialize State
screenshotted = False

# Main Loop
while True:
    # Screenshot Item
    if keyboard.is_pressed('ctrl') and keyboard.is_pressed('x'):
        if screenshotted == False:
            screenshot_item()
            screenshotted = True
    if not keyboard.is_pressed('x') and screenshotted == True:
        screenshotted = False
