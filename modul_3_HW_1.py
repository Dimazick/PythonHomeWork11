# #задание 1 класс Animal
# import pyaudio
# import wave
# import sys
# class Animal:
#     def __init__(self, name: str, kind: str, age: int) -> None:
#         self.name = name
#         self.kind = kind
#         self.age = age
#
#     def get_voice(self) -> str:
#         self.get_audio_voice()
#         match self.kind:
#             case "cat": return f"{self.kind} say - МЯУ!"
#             case "dog": return f"{self.kind} say - ГАВ!"
#             case "horse": return f"{self.kind} say - ИГО-ГО!"
#             case _: return "Sorry, I don't know how this animal say"
#         pass
#
#
#
#     def get_audio_voice(self):
#         CHUNK = 1
#         match self.kind:
#             case "cat": wf = wave.open("мяу.wav", 'rb')
#             case "dog": wf = wave.open("гав.wav", 'rb')
#             case "horse": wf = wave.open("игого.wav", 'rb')
#             case _: wf = wave.open("прочее.wav", 'rb')
#
#         p = pyaudio.PyAudio()
#         stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
#                         channels=wf.getnchannels(),
#                         rate=wf.getframerate(),
#                         output=True)
#         data = wf.readframes(CHUNK)
#         while data != b'':
#             stream.write(data)
#             data = wf.readframes(CHUNK)
#         stream.stop_stream()
#         stream.close()
#         p.terminate()
#         pass
#
#     def __str__(self):
#         return f"Имеется зверь - {self.kind}, возраст - {self.age} лет, зовут {self.name}"
#
#
# cat = Animal("Vasylisa", "cat", 2)
# print(cat.get_voice())
# print(cat)
#
# dog = Animal("Myhtar", "dog", 7)
# print(dog.get_voice())
# print(dog)
#
# horse = Animal("Bycefall", "horse", 5)
# print(horse.get_voice())
# print(horse)
#
# humman = Animal("Dima", "eagle", 32)
# print(humman.get_voice())
# print(humman)



