import datetime
import os
import pyautogui



def take_screenshot() -> None:
    # Get the current time
    time: datetime.datetime = datetime.datetime.now()

    # Format the current time
    formatted_time: str = datetime.datetime.strftime(self=time, format="%m.%d.%y.%I.%M.%S")

    # Locate the path to the current project
    project_path: str = os.path.dirname(p=__file__)

    # Create screenshot path
    screenshot: str = os.path.join(project_path, formatted_time)

    # Take the screenshot and save it to path
    pyautogui.screenshot(imageFilename=screenshot)
  
