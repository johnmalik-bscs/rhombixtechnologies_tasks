import speech_recognition as sr
import pyttsx3
import openai
import webbrowser
import os

# Initialize recognizer and TTS engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Text-to-speech function
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Speech-to-text function
def take_command():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            command = recognizer.recognize_google(audio)
            print(f"User said: {command}\n")
        except Exception as e:
            print("Could not understand audio, please repeat...")
            return "None"
    return command.lower()

def open_website(query):
    url = "https://www.google.com/search?q=" + query
    webbrowser.open(url)
    speak("Here is what I found on Google")

def open_application(app_name):
    if "notepad" in app_name:
        os.system("notepad")
    elif "calculator" in app_name:
        os.system("calc")
    else:
        speak("Application not available")

def openai_chatbot(prompt):
    openai.api_key = 'sk-your_openai_api_key'  # Replace with your OpenAI API key
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=50
    )
    return response.choices[0].text.strip()

# Play a favorite song
def play_favorite_song():
    song_path = "C:/path_to_your_song/favorite_song.mp3"  # Change this to your song file path
    if os.path.exists(song_path):
        os.startfile(song_path)
        speak("Playing your favorite song.")
    else:
        speak("The song file was not found.")

# Play a specific video (Nazar.mp4)
def play_nazar_video():
    video_path = "Nazar.mp4"  # Change this to your video file path
    if os.path.exists(video_path):
        os.startfile(video_path)
        speak("Playing Nazar video.")
    else:
        speak("The video file was not found.")

def run_voice_assistant():
    speak("How can I assist you today?")
    
    while True:
        query = take_command()
        
        if 'exit' in query or 'allah hafiz' in query or 'stop' in query:
            speak("Goodbye!")
            break

        elif 'how are you' in query or 'how r u' in query:
            speak("I'm fine, thank you. How can I assist you further?")
        
        elif 'thank you' in query:
            speak("You're welcome!")
        
        elif 'good night' in query:
            speak("Good Night Have a sweet dream!")
        
        elif 'qualification' in query:
            speak("My qualification is virtual assistance and artificial intelligence.")
            
        elif 'will you love me' in query:
            speak("OH My Friend, I am your virtual assistant. But I with you, Love is nothing")

        elif 'who made you' in query:
            speak("JUNAID MALIK is my creator. Thank you, JUNAID MALIK!")

        elif 'your name' in query:
            speak("My name is your virtual assistant.")

        elif 'feeling bad' in query:
            speak("OH My Dear Friend What happend.")
            
        elif 'your address' in query:
            speak("I'm a virtual assistant, so I don't have a physical address.")

        elif 'search' in query:
            speak("What would you like me to search?")
            search_query = take_command()
            open_website(search_query)
        
        elif 'open' in query:
            app_name = query.replace('open', '').strip()
            open_application(app_name)
        
        elif 'question' in query:
            speak("What would you like to know?")
            question = take_command()
            answer = openai_chatbot(question)
            speak(answer)

        elif 'play song' in query or 'favourite song' in query:
            play_favorite_song()

        elif 'play video' in query or 'nazar video' in query:
            play_nazar_video()

if __name__ == "__main__":
    run_voice_assistant()
