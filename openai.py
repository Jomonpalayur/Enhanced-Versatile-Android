import openai
import pyttsx3
import speech_recognition as sr

# Set your OpenAI API KEY
openai.api_key = "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"

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def transcribe_audio_to_text(filename):
    recognizer = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio = recognizer.record(source)
    try:
        return recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        print('Google Speech Recognition could not understand audio')
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")

def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=4000,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response["choices"][0]["text"]

def speak_text(text):
    engine.say(text)
    engine.runAndWait()

def greet_user():
    engine.say("Hello! I am EDITH. PURPOSE OF CREATION -----?")
    engine.runAndWait()

def main():
    greet_user()
    while True:
        print("Say something...")
        with sr.Microphone() as source:
            recognizer = sr.Recognizer()
            audio = recognizer.listen(source)
            try:
                transcription = recognizer.recognize_google(audio)
                print(f"You said: {transcription}")
                if "your name" in transcription.lower():
                    response_text = "My name is EDITH"
                else:
                    response_text = generate_response(transcription)
                print(f"GPT-3 SAYS: {response_text}")
                speak_text(response_text)
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")
            except Exception as e:
                print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
