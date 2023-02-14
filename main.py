
import time

from src.robot import BaseRobot
from src.keys import *

class DoStuff(BaseRobot):
    pic_path = "/home/danut/leetcode/Pic/"



    



if __name__ == "__main__":
    PIC_PATH = "/home/danut/leetcode/Pic/"
    # time.sleep(2)
    # main()
    robot = DoStuff(pic_path=PIC_PATH)


    # Selenium actions
    with robot.webdriver() as driver:
        robot.web_open_browser(driver)


        robot.web_access_url(driver, "https://youtube.com/")


        robot.web_click_element(driver, """//*[@id="content"]/div[2]/div[6]/div[1]/ytd-button-renderer[2]/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]""")

        robot.web_click_element(driver, """//*[@id="search"]""")

        robot.web_send_keys(driver, """//*[@id="search"]""", "dorian popa")
        robot.web_send_keys(driver, """//*[@id="search"]""", ENTER)

        robot.web_click_element(driver, """/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/div/div[1]/div/h3/a""")

        # time.sleep(6)
        # robot.clickPic(pic_name="hats.png") 
        time.sleep(150)