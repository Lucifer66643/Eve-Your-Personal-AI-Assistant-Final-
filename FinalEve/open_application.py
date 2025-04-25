# import pywhatkit as kit
# from speak_command import takecommand, speak

# def open_application():
#     try:
#         # Prompt the user via voice
#         speak("Please say the name of the application you want to open, like Chrome or Notepad.")
        
#         # Get the application name via voice command
#         app_name = takecommand().strip()
        
#         if not app_name:
#             speak("I didn't catch that. Please try again.")
#             return
        
#         # Attempt to open the application or search for it
#         kit.search(app_name)  # This will try to open the application or search online if not found
#         speak(f"Attempting to open application: {app_name}")
#         print(f"Attempting to open application: {app_name}")
#     except Exception as e:
#         speak("An error occurred while trying to open the application.")
#         print(f"An error occurred: {e}")

# if __name__ == '__main__':
#     open_application()



# applications = {
#     # Built-in Applications
#     "chrome": "start chrome",
#     "notepad": "notepad",
#     "calculator": "calc",
#     "paint": "mspaint",
#     "command prompt": "cmd",
#     "file explorer": "explorer",
#     "wordpad": "write",
#     "task manager": "taskmgr",
#     "control panel": "control",

#     # Microsoft Office Suite
#     "microsoft word": "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE",
#     "microsoft excel": "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE",
#     "microsoft powerpoint": "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE",

#     # Browsers
#     "firefox": "C:\\Program Files\\Mozilla Firefox\\firefox.exe",
#     "edge": "start microsoft-edge:",
#     "brave": "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe",

#     # Multimedia Players
#     "vlc media player": "C:\\Program Files\\VideoLAN\\VLC\\vlc.exe",
#     "windows media player": "C:\\Program Files\\Windows Media Player\\wmplayer.exe",
#     "spotify": "C:\\Users\\YourUsername\\AppData\\Roaming\\Spotify\\Spotify.exe",

#     # Developer Tools
#     "visual studio code": "C:\\Users\\YourUsername\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe",
#     "pycharm": "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2023.1\\bin\\pycharm64.exe",
#     "eclipse": "C:\\Program Files\\Eclipse\\eclipse.exe",
#     "android studio": "C:\\Program Files\\Android\\Android Studio\\bin\\studio64.exe",

#     # Communication Tools
#     "skype": "C:\\Program Files (x86)\\Microsoft\\Skype for Desktop\\Skype.exe",
#     "zoom": "C:\\Users\\YourUsername\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe",
#     "discord": "C:\\Users\\YourUsername\\AppData\\Local\\Discord\\app-1.0.9004\\Discord.exe",
#     "teams": "C:\\Program Files\\Microsoft Teams\\current\\Teams.exe",

#     # File Compression
#     "winrar": "C:\\Program Files\\WinRAR\\WinRAR.exe",
#     "7zip": "C:\\Program Files\\7-Zip\\7zFM.exe",

#     # System Utilities
#     "device manager": "devmgmt.msc",
#     "disk management": "diskmgmt.msc",
#     "services": "services.msc",
#     "event viewer": "eventvwr.msc",

#     # Custom Applications
#     "photoshop": "C:\\Program Files\\Adobe\\Adobe Photoshop 2023\\Photoshop.exe",
#     "illustrator": "C:\\Program Files\\Adobe\\Adobe Illustrator 2023\\Illustrator.exe",
#     "premiere pro": "C:\\Program Files\\Adobe\\Adobe Premiere Pro 2023\\Adobe Premiere Pro.exe",
# }




import os
from speak_command import takecommand, speak

def open_application():
    try:
        # Prompt the user via voice
        speak("Please say the name of the application you want to open, like Chrome or Notepad.")
        
        # Get the application name via voice command
        app_name = takecommand().strip().lower()
        
        if not app_name:
            speak("I didn't catch that. Please try again.")
            return
        
        # Application paths or commands
        applications = {
            "chrome": "start chrome",
            "notepad": "notepad",
            "calculator": "calc",
            "paint": "mspaint",
            "command prompt": "cmd",
            "file explorer": "explorer",
        }
        
        if app_name in applications:
            os.system(applications[app_name])  # Open the specified application
            speak(f"Opening {app_name}.")
            print(f"Opening {app_name}.")
        else:
            speak(f"Sorry, I don't know how to open {app_name}. Please add it to my database.")
            print(f"Unknown application: {app_name}")
    except Exception as e:
        speak("An error occurred while trying to open the application.")
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    open_application()
