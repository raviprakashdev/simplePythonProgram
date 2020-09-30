import pyautogui, time
time.sleep(5)

str = "Hello World"
count = 20


for word in range(count):
    pyautogui.typewrite(str)
    pyautogui.press("enter")

print("Success")
    