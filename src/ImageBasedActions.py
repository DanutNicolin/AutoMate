import pyautogui
import time 

from pathlib import Path

from src.error_handler import ErrorHandler




class ImageBasedActions(ErrorHandler):
    def __init__(self, pic_path, delay):
        self.pic_path = pic_path
        self.delay = delay
        self.debug = False

    def construct_path(self, pic_name:str):
        path = Path(self.pic_path).joinpath(pic_name)
        return path

    def get_coordonates(self, pic_name:str):
        path = str(self.construct_path(pic_name))
        coordonates = pyautogui.locateOnScreen(path)
        # print(coordonates)
        return coordonates

    def clickPic(self, pic_name:str, offset:tuple=None ,delay:int=None):
        """
        offset: tuple(left:int, top:int)
        """
        if delay is None:
            delay = self.delay
        time.sleep(delay)

        pic_coordonates = self.get_coordonates(pic_name)
        error_handling = self.error_handling(pic_coordonates)

        if offset != None:
            pyautogui.moveTo(pic_coordonates)
            pyautogui.moveRel(offset)
            pyautogui.click()
            return True

        pyautogui.click(pic_coordonates)
        return True

    def dclickPic(self, pic_name:str, delay:int=None):
        pic_coordonates = self.get_coordonates(pic_name)
        error_handling = self.error_handling(pic_coordonates)

        if delay is None:
            delay = self.delay
        time.sleep(delay)

        pyautogui.doubleClick(pic_coordonates)
        return True

    def mouseDown(self, pic_name:str, delay:int=None):
        pic_coordonates = self.get_coordonates(pic_name)
        error_handling = self.error_handling(pic_coordonates)

        if delay is None:
            delay = self.delay
        time.sleep(delay)

        pyautogui.mouseDown(pic_coordonates, button='left')
        return True

    def mouseUp(self, delay:int=None):
        if delay is None:
            delay = self.delay
        time.sleep(delay)

        pyautogui.mouseUp(button='left')
        return True

    def dragToPic(self, pic_name:str, delay:int=None):
        pic_coordonates = self.get_coordonates(pic_name)
        error_handling = self.error_handling(pic_coordonates)

        if delay is None:
            delay = self.delay
        time.sleep(delay)

        pyautogui.dragTo(pic_coordonates, duration=2)
        return True
