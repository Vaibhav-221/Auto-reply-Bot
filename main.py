import pyautogui
import pyperclip
import time

# Give yourself 3 seconds
time.sleep(3)

# Coordinates
start_x, start_y = 612, 182
end_x, end_y = 1860, 945

# Move to start
pyautogui.moveTo(start_x, start_y, duration=0.5)

# Hold mouse
pyautogui.mouseDown(button='left')

# IMPORTANT for WhatsApp Desktop
time.sleep(0.2)

# Drag slowly
pyautogui.moveTo(end_x, end_y, duration=2)

# Release mouse
pyautogui.mouseUp(button='left')

# Wait
time.sleep(0.5)

# Copy
pyautogui.hotkey('ctrl', 'c')
pyautogui.click(1760, 845)

# Wait for clipboard
time.sleep(0.5)


# Read clipboard
copied_text = pyperclip.paste()

print("Copied Text:\n")
print(copied_text)