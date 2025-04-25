import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser as wb
import os
import random
import pyautogui
import pyjokes
from weather import get_weather
from system_status import SystemHealthMonitor
from window import minimize_active_window
import requests
from news import NewsFromBBC
from speak_command import speak, takecommand
import pywhatkit as kit

# engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[1].id)
# engine.setProperty('rate', 150)
# engine.setProperty('volume', 1)

# def speak(audio) -> None:
#     engine.say(audio)
#     engine.runAndWait()


def time() -> None:
    current_time = datetime.datetime.now().strftime("%I:%M:%S %p")
    speak("The current time is")
    speak(current_time)
    print("The current time is", current_time)

def date() -> None:
    now = datetime.datetime.now()
    speak("The current date is")
    speak(f"{now.day} {now.strftime('%B')} {now.year}")
    print(f"The current date is {now.day}/{now.month}/{now.year}")

def wishme() -> None:
    speak("Welcome back, sir!")
    print("Welcome back, sir!")

    hour = datetime.datetime.now().hour
    if 4 <= hour < 12:
        speak("Good morning!")
        print("Good morning!")
    elif 12 <= hour < 16:
        speak("Good afternoon!")
        print("Good afternoon!")
    elif 16 <= hour < 24:
        speak("Good evening!")
        print("Good evening!")
    else:
        speak("Good night!")

    assistant_name = load_name()
    speak(f"{assistant_name} at your service. Please tell me how may I assist you.")
    print(f"{assistant_name} at your service. Please tell me how may I assist you.")

def screenshot() -> None:
    img = pyautogui.screenshot()
    img_path = os.path.expanduser("~\\Pictures\\Eve Screenshots\\screenshot.png")
    img.save(img_path)
    speak(f"Screenshot has been saved.")
    print(f"Screenshot saved as {img_path}.")

# def takecommand() -> str:
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening...")
#         r.pause_threshold = 1

#         try:
#             audio = r.listen(source, timeout=5)  # Listen with a timeout
#         except sr.WaitTimeoutError:
#             speak("Timeout occurred. Please try again.")
#             return None

#     try:
#         print("Recognizing...")
#         query = r.recognize_google(audio, language="en-in")
#         print(query)
#         return query.lower()
#     except sr.UnknownValueError:
#         speak("Sorry, I did not understand that.")
#         return None
#     except sr.RequestError:
#         speak("Speech recognition service is unavailable.")
#         return None
#     except Exception as e:
#         speak(f"An error occurred: {e}")
#         print(f"Error: {e}")
#         return None


def load_name() -> str:
    try:
        with open("assistant_name.txt", "r") as file:
            return file.read().strip()
    except FileNotFoundError:
        return "Eve"


def search_wikipedia(query):
    try:
        speak("Searching Wikipedia...")
        result = wikipedia.summary(query, sentences=2)
        speak(result)
        print(result)
    except wikipedia.exceptions.DisambiguationError:
        speak("Multiple results found. Please be more specific.")
    except Exception:
        speak("I couldn't find anything on Wikipedia.")

def control_led(location, state):
    """Send a request to the Flask API to control the LEDs."""
    base_url = "http://127.0.0.1:5000"  # Flask server URL
    endpoint = f"/led/{location}/{state}"
    try:
        response = requests.get(base_url + endpoint)
        if response.status_code == 200:
            speak(response.json()["status"])
        else:
            speak("Failed to control the LED. Please try again.")
    except requests.exceptions.RequestException as e:
        speak("I couldn't connect to the server. Please check if it's running.")

def handle_system_status():
    monitor = SystemHealthMonitor()
    speak("Sure!")
    print("Sure!")
    
    cpu_usage = monitor.get_cpu_usage()
    memory = monitor.get_memory_usage()
    disk = monitor.get_disk_usage()

    status = (
        f"System Status:\n"
        f"CPU usage: {cpu_usage} percent.\n"
        # f"Total memory: {memory['Total'] / (1024 ** 3):.2f} GB, "
        # f"Used: {memory['Used'] / (1024 ** 3):.2f} GB, "
        # f"Free: {memory['Free'] / (1024 ** 3):.2f} GB, "
        f"Memory usage: {memory['Percentage']} percent.\n"
        # f"Total disk space: {disk['Total'] / (1024 ** 3):.2f} GB, "
        # f"Used: {disk['Used'] / (1024 ** 3):.2f} GB, "
        # f"Free: {disk['Free'] / (1024 ** 3):.2f} GB, "
        f"Disk usage: {disk['Percentage']} percent."
    )

    speak(status)
    print(status)

def open_application():
    try:
        # Prompt the user via voice
        speak("Please say the name of the application you want to open, like Chrome or Notepad.")
        
        # Get the application name via voice command
        app_name = takecommand().strip()
        
        if not app_name:
            speak("I didn't catch that. Please try again.")
            return
        
        # Attempt to open the application or search for it
        kit.search(app_name)  # This will try to open the application or search online if not found
        speak(f"Attempting to open application: {app_name}")
        print(f"Attempting to open application: {app_name}")
    except Exception as e:
        speak("An error occurred while trying to open the application.")
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    wishme()
    
    while True:
        query = takecommand()

        if not query:
            continue
        if "time" in query or "check time" in query:
            time()

        elif "date" in query or "check date" in query:
            date()

        elif "wikipedia" in query or "search on wikipedia" in query:
            query = query.replace("wikipedia", "").strip()
            search_wikipedia(query)

        elif "open youtube" in query:
            wb.open("youtube.com")

        elif "open google" in query:
            wb.open("google.com")

        elif "open application" in query or "start application" in query or "open app" in query:
            open_application()

        elif "screenshot" in query:
            screenshot()

        elif "tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)
            print(joke)

        elif "weather" in query or "check weather" in query:
            speak("Let me check the weather for you.")
            get_weather()

        elif "system status" in query or "check system" in query or "cpu" in query:
            handle_system_status()

        elif "shutdown" in query or "shutdown the system" in query or "shutdown the pc" in query:
            speak("Shutting down the system, goodbye!")
            os.system("shutdown /s /f /t 1")
            break

        elif "restart" in query or "restart the system" in query or "restart the pc" in query:
            speak("Restarting the system, please wait!")
            os.system("shutdown /r /f /t 1")
            break

        elif "hall light of" in query or "light off"  in query or "hall light off" in query or "Turn off hall light" in query:
            control_led("hall", "off")

        elif "hall light" in query or "Turn on hall light" in query  or "hall light on" in query:
            control_led("hall", "on")

        elif "kitchen light on" in query or "switch on kitchen" in query or "kitchen lights on" in query or "turn on kitchen light" in query:
            control_led("kitchen", "on")
        
        elif "switch off kitchen" in query or "kitchen lights off" in query or "turn off kitchen lights" in query or "turn off kitchen light" in query:
            control_led("kitchen", "off")

        elif "minimize window" in query or "minimize" in query or "minimise" in query or "minimize the window" in query:
            speak('Minimizing window')
            minimize_active_window()
        
        elif "news" in query or "headlines" in query:
            speak("Okay! I'm fetching todays Headlines")
            NewsFromBBC()

        elif "offline" in query or "exit" in query:
            speak("Going offline. Have a good day!")
            break
