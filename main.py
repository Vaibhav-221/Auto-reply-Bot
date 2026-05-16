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



from google import genai
# =========================
# STEP 2: GEMINI AI
# =========================

client = genai.Client(
    api_key="AIzaSyCOGjsxDQyqNAjAcVI-_rkpBDSsU27Rf88"
)

prompt = f"""
You are Vaibhav, an engineering student.

Analyze the following WhatsApp chat carefully.

Understand:
- context
- emotions
- conversation flow
- relationship tone

Then generate a natural human-like reply.

Chat History:
{copied_text}
"""

try:
    response = client.models.generate_content(
        model="gemini-3.1-flash-lite",
        contents=prompt
    )

    print(response.text)

except Exception as e:
    print("Error:", e)

# print("\nAI Reply:\n")
# print(response.text)