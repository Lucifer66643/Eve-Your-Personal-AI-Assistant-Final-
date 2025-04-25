from transformers import BertTokenizer, BertForSequenceClassification
import torch

model = BertForSequenceClassification.from_pretrained('./intent_model')
tokenizer = BertTokenizer.from_pretrained('./intent_model')

model.eval()

def predict_intent(text):
    inputs = tokenizer(text, return_tensors='pt', max_length=128)

    with torch.no_grad():
        outputs = model(**inputs)

    predicted_label = torch.argmax(outputs.logits, axis=1).item()

    int_to_label = {0: "time", 1: "date", 2: "search_wikipedia", 3: "youtube",
                    4: "google", 5: "open_application", 6: "screenshot", 7: "joke",
                    8: "get_weather", 9: "handle_system_status", 10: "shutdown",
                    11: "restart", 12: "control_led", 13: "minimize_active_window"}

    intent = int_to_label[predicted_label]
    return intent

import speak
import speech_recognition as sr

listener = sr.Recognizer()

def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            listener.adjust_for_ambient_noise(source)
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            intent = predict_intent(command)
            return intent
    except sr.RequestError:
        speak.speak("Sorry, I couldn't reach the Google API.")
    except sr.UnknownValueError:
        speak.speak("Sorry, I did not understand that.")
    except Exception as e:
        speak.speak(f"An error occurred: {str(e)}")
    return ""

# if __name__ == "__main__":

#     while (True):
#         text = input("please enter input : ")
#         predicted_intent = predict_intent(text)
#         print(f"Predicted Intent: {predicted_intent}")
