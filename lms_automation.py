#!/usr/bin/env python3

import sys
import webbrowser
import time
import pyautogui
from datetime import datetime


# website link
LMS_WEBSITE_LINK = "https://script.google.com/a/coriolis.co.in/macros/s/AKfycbzp1aNPdUf9qlvrLh2FJvTJ0BUXvbKcrwrzret4v1paTt4tAuA/exec"

LMS_SCREEN_COORDINATES = {
    "lockedScreen": {"x": 2605, "y": 626},
    "input": {"x": 802, "y": 530},
    "submit": {"x": 670, "y": 604},
    "goToHome": {"x": 1181, "y": 275},
    "wfhNavlink": {"x": 284, "y": 133},
    "wfhApplyOption": {"x": 305, "y": 172},
    "wfhApplyDate": {"x": 679, "y": 294},
    "wfhApplyAgenda": {"x": 1106, "y": 364},
    "wfhApplySubmit": {"x": 663, "y": 438},
}


class LMSAutomation:
    def __init__(self):
        """
        Initialize variables and open browser
        """
        # Set present Date in format -> 'year/month/date'
        now = datetime.now()
        present_year = now.strftime("%Y")
        present_month = now.strftime("%m")
        present_day = now.strftime("%d")
        self.initialized = True

        # Check if today is Saturday (5) or Sunday (6)
        if now.weekday() in [5, 6]:  # 5 -> Saturday, 6 -> Sunday
            print("Today is a weekend. Exiting initialization.")
            self.initialized = False
            return

        self.current_date = f"{present_year}/{present_month}/{present_day}"
        self.status_message = "Working on it"
        self.wfh_message = "Working on feature"

        self.sleep_long = 20
        self.sleep_short = 10
        
        self.coordinates = LMS_SCREEN_COORDINATES

        # Open Locked Screen
        pyautogui.moveTo(self.coordinates["lockedScreen"]["x"], self.coordinates["lockedScreen"]["y"], duration=1)
        pyautogui.click()

        # Enter Password
        password = "Nezukochan@02"
        pyautogui.write(password, interval=0.1)

        # Unlock the screen
        pyautogui.press('enter')
        time.sleep(self.sleep_short)

        # Open the website in the default browser
        webbrowser.open(LMS_WEBSITE_LINK)

        # Wait a few seconds for the page to load
        time.sleep(self.sleep_long)


    def get_coordinates(self):
        """
        This function prints coordinates of position, wherever mouse is pointed
        """
        print(pyautogui.position())


    def lock_screen(self):
        """
        Locks the screen
        """
        pyautogui.hotkey('win', 'l')

    
    def wfh_apply(self):
        """
        This function applies for WFH
        """
        if not getattr(self, "initialized", False):  # Prevent execution if not initialized
            print("Cannot execute wfh_apply: Object not initialized properly.")
            return

        # Click on wfh navlink
        pyautogui.moveTo(self.coordinates["wfhNavlink"]["x"], self.coordinates["wfhNavlink"]["y"], duration=1)
        pyautogui.click()

        # Click on Apply option in expanded dropdown
        pyautogui.moveTo(self.coordinates["wfhApplyOption"]["x"], self.coordinates["wfhApplyOption"]["y"], duration=1)
        pyautogui.click()

        # Wait for page load
        time.sleep(self.sleep_long)

        # Click on date
        pyautogui.moveTo(self.coordinates["wfhApplyDate"]["x"], self.coordinates["wfhApplyDate"]["y"], duration=1)
        pyautogui.click()

        # Enter Current Date
        pyautogui.write(self.current_date, interval=0.1)

        # Click on wfh agenda textfield
        pyautogui.moveTo(self.coordinates["wfhApplyAgenda"]["x"], self.coordinates["wfhApplyAgenda"]["y"], duration=1)
        pyautogui.click()

        # Enter todays agenda for wfh
        pyautogui.write(self.wfh_message, interval=0.1)

        # Click on submit button
        pyautogui.moveTo(self.coordinates["wfhApplySubmit"]["x"], self.coordinates["wfhApplySubmit"]["y"], duration=1)
        pyautogui.click()

        # Wait for page load
        time.sleep(self.sleep_long)

        # Click on 'Go To Home' button
        pyautogui.moveTo(self.coordinates["goToHome"]["x"], self.coordinates["goToHome"]["y"], duration=1)
        pyautogui.click()

        # Lock the screen after automation completes
        self.lock_screen()


    def status_update(self):
        """
        This function updates LMS status
        """
        if not getattr(self, "initialized", False):  # Prevent execution if not initialized
            print("Cannot update status: Object not initialized properly.")
            return

        # Click on input box
        pyautogui.moveTo(self.coordinates["input"]["x"], self.coordinates["input"]["y"], duration=1)
        pyautogui.click()

        # Enter Status
        pyautogui.write(self.status_message, interval=0.1)

        # Click on Submit button
        pyautogui.moveTo(self.coordinates["submit"]["x"], self.coordinates["submit"]["y"], duration=1)
        pyautogui.click()

        # Wait for page load
        time.sleep(self.sleep_long)

        # Click on 'Go To Home' button
        pyautogui.moveTo(self.coordinates["goToHome"]["x"], self.coordinates["goToHome"]["y"], duration=1)
        pyautogui.click()

        # Lock the screen after automation completes
        self.lock_screen()


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python lms_automation.py [wfh_apply|status_update]")
        sys.exit(1)

    action = sys.argv[1]
    lms_automation = LMSAutomation()

    if action == 'wfh_apply':
        lms_automation.wfh_apply()
    elif action == 'status_update':
        lms_automation.status_update()
    else:
        print("Invalid action. Use 'wfh_apply' or 'status_update'.")
        sys.exit(1)
