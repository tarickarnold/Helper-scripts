import logging
import os
import psutil

def close_app(app_name) -> None:
    # Get running apps process
    running_apps = psutil.process_iter(['pid', 'name'])
    
    # Get names of running apps in a list
    for app in running_apps:
        sys_app=app.info.get('name').split('.')[0].lower()

        # Get process identifer that matches function parameter
        if sys_app in app_name.split() or app_name in sys_app:
            pid: any = app.info.get('pid')
        
            # Terminate matched process with process identifier and wait until closed
            app_pid = psutil.Process(pid)
            app_pid.terminate()
            app_pid.wait()
        else: 
            pass
