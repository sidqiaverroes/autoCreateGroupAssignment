import pyautogui
import time
import keyboard

running = False


def start_program():
    global running
    running = True
    print("Program started")


def end_program():
    global running
    running = False
    print("Program ended")


def input_name(anggota_kelompok, x_coord, y_coord):
    # go to search bar
    pyautogui.press("tab")

    for i in range(len(anggota_kelompok)):
        # Type the text
        pyautogui.typewrite(anggota_kelompok[i])
        # Move the mouse to the specified coordinate
        pyautogui.moveTo(x_coord, y_coord)
        # Trigger a left mouse click at the current mouse position
        pyautogui.click()
        # Go to search bar
        pyautogui.hotkey("shift", "tab")
        pyautogui.hotkey("shift", "tab")

    # go to enter button submit group
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("enter")

    time.sleep(1.5)

    # create new group
    pyautogui.press("tab")
    pyautogui.hotkey("shift", "tab")
    pyautogui.press("enter")


# Register hotkeys
keyboard.add_hotkey("s", start_program)
keyboard.add_hotkey("q", end_program)


x_coord = 924
y_coord = 615
# daftar anggota
anggota_kelompok_1 = ["razza", "marsel", "rajen"]
anggota_kelompok_2 = ["ega.rizky", "antonius", "nafisa"]
anggota_kelompok_3 = ["franciscus", "daniyal"]
anggota_kelompok_4 = ["azka.adhi", "raffid", "yasmine"]
anggota_kelompok_5 = ["diestra", "valentinus", "zildiray"]
anggota_kelompok_6 = ["baihaqi", "rasyid"]
anggota_kelompok_7 = ["johanes", "haikal"]
anggota_kelompok_8 = ["aly", "thoriq", "daru"]
anggota_kelompok_9 = ["nathan.praja", "rizqi", "hasnan"]
anggota_kelompok_10 = ["ahmad.zaki", "giga", "bintang"]
anggota_kelompok_11 = ["rico", "nikolas", "athilla"]
anggota_kelompok_12 = ["uswa", "angelica", "diandra"]

while True:
    if running:
        print("Program started")
        # Delay before starting typing
        time.sleep(1)

        # only needed once
        pyautogui.press("tab")

        input_name(anggota_kelompok_1, x_coord, y_coord)

        input_name(anggota_kelompok_2, x_coord, y_coord)

        input_name(anggota_kelompok_3, x_coord, y_coord)

        input_name(anggota_kelompok_4, x_coord, y_coord)

        input_name(anggota_kelompok_5, x_coord, y_coord)

        input_name(anggota_kelompok_6, x_coord, y_coord)

        input_name(anggota_kelompok_7, x_coord, y_coord)

        input_name(anggota_kelompok_8, x_coord, y_coord)

        input_name(anggota_kelompok_9, x_coord, y_coord)

        input_name(anggota_kelompok_10, x_coord, y_coord)

        input_name(anggota_kelompok_11, x_coord, y_coord)

        input_name(anggota_kelompok_12, x_coord, y_coord)

        print("Done ya bang")
        running = False
