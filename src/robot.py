

from src.ImageBasedActions import ImageBasedActions
from src.BrowserActions import BrowserActions
from src.WebScrapingActions import WebScrapingActions



class BaseRobot(ImageBasedActions,
                BrowserActions,
                WebScrapingActions):

    def __init__(self, pic_path=None, driver="Chrome", delay=2):
        self.pic_path = pic_path
        self.driver = driver
        self.delay = delay
                
        # self.image_based_action = ImageBasedActions(self.pic_path)
        # self.browser_actions = BrowserActions(self.driver)










# >>> pyautogui.mouseDown(x=moveToX, y=moveToY, button='left')
# >>> pyautogui.mouseUp(x=moveToX, y=moveToY, button='left')
# pyautogui.moveRel(xOffset, yOffset, duration=num_seconds)




