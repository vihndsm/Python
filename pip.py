# import pyautogui
# pyautogui.typewrite("Hello World")
# # распечатать "Hello World" мгновенно


# pyautogui.typewrite("bye bye",interval=0.5)
# """Распечатайте "Hello World" с задержкой 
# в полсекунды после каждого символа"""

# import wikipedia
# query = wikipedia.page("python")
# print(query.summary)

'''### audio playing ####'''

# from gtts import gTTS
# from playsound import playsound

# play = 'audio.mp3'
# # language = 'ru'

# audio = gTTS(text = 'Python — высокоуровневый язык программирования общего назначения, ориентированный на повышение производительности разработчика и читаемости кода. Синтаксис ядра Python минималистичен. В то же время стандартная библиотека включает большой набор полезных функций', lang = 'ru', slow = False)
# audio.save(play)
# playsound(play)