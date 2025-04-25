import serial
import time

BLUETOOTH_PORT = 'COM3'
BAUD_RATE = 9600
TIMEOUT = 1

try:
    bluetoothSerial = serial.Serial(BLUETOOTH_PORT, BAUD_RATE, timeout=TIMEOUT)
    print(f"Successfully connected to {BLUETOOTH_PORT} at {BAUD_RATE} baud.")

    while True:
        command = input("Enter command (A to turn LED1 ON, B to turn LED1 OFF, C to turn LED2 ON, D to turn LED2 OFF, or Q to quit): ").upper()

        if command == 'Q':
            break
        elif command in ['A', 'B', 'C', 'D']:
            print(f"Sending command: {command}")
            bluetoothSerial.write(command.encode())
            time.sleep(0.1)

            if bluetoothSerial.in_waiting > 0:
                response = bluetoothSerial.readline().decode('utf-8').strip()
                print(f"Arduino response: {response}")
        else:
            print("Invalid command. Please enter A, B, C, D, or Q.")

except serial.SerialException as e:
    print(f"Error connecting to Bluetooth port {BLUETOOTH_PORT}: {e}")
except KeyboardInterrupt:
    print("\nExiting.")
finally:
    if 'bluetoothSerial' in locals() and bluetoothSerial.is_open:
        bluetoothSerial.close()
        print("Bluetooth connection closed.")







# from speak import speak
# import requests
# from take_command import take_command

# def control_led(action):
#     base_url = "http://127.0.0.1:5000"  # Replace with the actual host if different
#     if action == "on":
#         url = f"{base_url}/led/on"
#     elif action == "off":
#         url = f"{base_url}/led/off"
#     else:
#         speak("Invalid action. Please say turn on or turn off.")
#         return

#     try:
#         response = requests.get(url)
#         if response.status_code == 200:
#             message = response.json().get("status", "No response received.")
#             speak(message)
#             print(message)
#         else:
#             speak("Failed to communicate with the LED controller.")
#             print(f"Error: {response.status_code}")
#     except requests.exceptions.RequestException as e:
#         speak("An error occurred while communicating with the LED controller.")
#         print(f"Error: {e}")

# def main():
#     while True:
#         speak("How can I assist you?")
#         command = take_command()
        
#         if "turn on" in command or "bedroom light on" in command or "light on" in command:
#             control_led("on")
#         elif "turn off" in command or "bedroom light off" in command or "light off" in command:
#             control_led("off")
#         elif "exit" in command or "stop" in command:
#             speak("Goodbye!")
#             print("Exiting...")
#             break
#         else:
#             speak("I didn't understand that. Please say turn on or turn off the light.")

# # Run the assistant
# if __name__ == "__main__":
#     main()