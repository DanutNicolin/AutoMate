import pyautogui
import time
import os
import json


# time.sleep(1)
# print(pyautogui.position())

PIC_PATH = "/home/danut/leetcode/Pic/"
img_files = os.listdir(PIC_PATH)

def read_json():
    with open("coordonates.json", "r") as f:
        json_content = json.load(f)
    return json_content

def write_json(content:dict):
    with open("coordonates.json", "w") as f:
        json.dump(content, f, indent=4)


def update_coordonates(img_files):
    img_coordonates = read_json()

    for img in img_files:
        img_key = img.split(".")[0]

        if (img_key in img_coordonates) and (img_coordonates[img_key] != None):
            padding = " " * (10-len(img_key))
            print(f"{img_key} {padding} already has coordonates")
            continue

        coordonates = pyautogui.locateOnScreen(f"{PIC_PATH}/{img}")
        img_coordonates[img_key] = coordonates
        print(f"{img_key} coordonates have been added")

        write_json(img_coordonates)


update_coordonates(img_files)

# home_location = pyautogui.locateOnScreen(f"{PIC_PATH}/home.png")


# pyautogui.center(coordonates)

# pics = {
#     "home_folder": pyautogui.center(home_location)
# }