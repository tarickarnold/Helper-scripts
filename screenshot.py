import datetime
import logging
import os
import pyautogui

screenshot_logger = logging.getLogger(__name__)

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
    screenshot_logger.info(f"{screenshot} taken for error reporting")

def main() -> None:
    config: any = config('config.toml')
    botname: any = config['bot']['name']
    take_screenshot()

if __name__ == "__main__":
    main()