import pyautogui
import pyperclip
import time
from google import genai

# =====================================
# GEMINI CLIENT
# =====================================

client = genai.Client(
    api_key="AIzaSyCOGjsxDQyqNAjAcVI-_rkpBDSsU27Rf88"
)

# =====================================
# MEMORY
# =====================================

last_processed_message = ""
last_ai_reply = ""

# =====================================
# LOOP
# =====================================

while True:

    try:

        print("\nChecking messages...\n")

        # =====================================
        # SELECT CHAT AREA
        # =====================================

        start_x, start_y = 556, 121
        end_x, end_y = 915, 1008

        pyautogui.moveTo(start_x, start_y, duration=0.1)

        pyautogui.mouseDown(button='left')

        pyautogui.moveTo(end_x, end_y, duration=0.3)

        pyautogui.mouseUp(button='left')

        time.sleep(0.2)

        # =====================================
        # COPY CHAT
        # =====================================

        pyautogui.hotkey('ctrl', 'c')

        time.sleep(0.5)

        copied_text = pyperclip.paste()

        # Deselect
        pyautogui.click(968, 910)

        # =====================================
        # CLEAN TEXT
        # =====================================

        lines = copied_text.split("\n")

        # Remove empty garbage lines
        lines = [line.strip() for line in lines if line.strip()]

        if len(lines) == 0:
            print("No text found")
            time.sleep(5)
            continue

        # =====================================
        # FIND LAST VALID MESSAGE
        # =====================================

        latest_message = ""

        for line in reversed(lines):

            # Ignore Instagram UI garbage
            ignored_words = [
                "Seen",
                "Active now",
                "Typing...",
                "You sent",
                "Send message"
            ]

            if any(word.lower() in line.lower() for word in ignored_words):
                continue

            # Ignore your own previous AI reply
            if line == last_ai_reply:
                continue

            latest_message = line
            break

        if latest_message == "":
            print("No valid message")
            time.sleep(5)
            continue

        print("Latest Message:", latest_message)

        # =====================================
        # DUPLICATE CHECK
        # =====================================

        if latest_message == last_processed_message:
            print("Already processed")
            time.sleep(5)
            continue

        # Save immediately
        last_processed_message = latest_message

        # =====================================
        # GEMINI PROMPT
        # =====================================

        prompt = f"""
Reply naturally to this Instagram DM.

Rules:
- Casual Hinglish
- Human-like
- Short
- Funny if suitable
- No explanationccc
- No quotation marks
- Output only reply text

Message:
{latest_message}
"""

        # =====================================
        # GENERATE RESPONSE
        # =====================================

        response = client.models.generate_content(
            model="gemini-3.1-flash-lite",
            contents=prompt
        )

        reply = response.text.strip()

        # Clean formatting
        reply = reply.replace('"', '')
        reply = reply.replace("*", '')

        print("AI Reply:", reply)

        # Save AI reply
        last_ai_reply = reply

        # =====================================
        # SEND MESSAGE
        # =====================================

        pyperclip.copy(reply)

        # Click message input box
        pyautogui.click(930, 982)

        time.sleep(0.2)

        pyautogui.hotkey('ctrl', 'v')

        time.sleep(0.2)

        pyautogui.press('enter')

        print("Reply Sent")

        # Cooldown after sending
        time.sleep(8)

    except Exception as e:

        print("Error:", e)

        time.sleep(5)