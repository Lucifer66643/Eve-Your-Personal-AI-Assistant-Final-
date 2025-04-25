# import subprocess

# def minimize_active_window():
#     try:
#         # Get the active window ID
#         result = subprocess.run(['xdotool', 'getactivewindow'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#         if result.returncode != 0:
#             raise Exception(result.stderr.decode('utf-8'))

#         active_window_id = result.stdout.decode('utf-8').strip()

#         # Minimize the active window
#         subprocess.run(['xdotool', 'windowminimize', active_window_id], check=True)
#         print("Active window minimized successfully.")
#     except FileNotFoundError:
#         print("xdotool is not installed or not found in PATH.")
#     except Exception as e:
#         print(f"An error occurred: {e}")

# if __name__ == '__main__':
#     minimize_active_window()

import pygetwindow as gw

def minimize_active_window():
    try:
        active_window = gw.getActiveWindow()
        if active_window:
            active_window.minimize()
            print(f"Window '{active_window.title}' minimized successfully.")
        else:
            print("No active window found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    minimize_active_window()
