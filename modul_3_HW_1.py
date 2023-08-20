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

#задача про книгу
# class Book:
#     def __init__(self, name: str, autor: str, pages: int) -> None:
#         self.name = name
#         self.autor = autor
#         self.pages = pages
#
#     def open_this_page(self, nomber: int) -> None:
#         if nomber < self.pages:
#             print(f"Книга открылась на странице номер {nomber}, ведь она это может")
#         else:
#             print(" в данном экземпляре нет столько страниц, дорогой товарисчщ")
#
#     def __str__(self):
#         return f"Представляем вашему вниманию книгу {self.name} за авторством уважаемого (или нет) {self.autor} будет держать вас в напряжении на всех {self.pages} страницах"
#
#
# conan = Book("Конан варвар", "Роберт И. Говард", 522)
# print(conan)
# print("пробуем открыть на странице 714")
# conan.open_this_page(714)
# print("пробуем открыть на странице 212")
# conan.open_this_page(212)
# print(conan)

# задача про альбом
class MusicAlbum:
    def __init__(self, artist: str, name: str, track_list: list) -> None:
        self.artist = artist
        self.name = name
        self.track_list = track_list

    def __str__(self):
        return f"альбом <{self.name}>, за авторством {self.artist}, спикок треков :{self.track_list}"

    def add_track(self, track: str) -> None:
        self.track_list.append(track)
        print(f"Трек {track} добавлен в альбом")

    def remove_track(self, track) -> None:
        if track in self.track_list:
            self.track_list.remove(track)
            print(f"Трек {track} удален из альбома")
        else:
            print("Дружище, такого трека нет")

    def play_track(self, track) -> None:
        if track in self.track_list:
            print(f"Трек <{track}> из альбома <{self.name}> радует нас своим звучанием")
        else:
            print("Дружище, такого трека нет, послушай чего нибудь другое")


pygacheva = ["какое то там лето", "арлекино", "даром преподаватели"]
sytkin = ["Москва- Нева", "7 тысяч над землей", "далеко"]
jb = ["Кимоно Винокура", "Музыкальный патриот"]

alla = MusicAlbum("Алла Борисна", "Broskina - the madam", pygacheva)
valera = MusicAlbum("Валерий Сюткин", "То, что надо", sytkin)
pacany = MusicAlbum("Джордано Бруно", "Можно не запивать", jb)

print(alla)
alla.add_track("Айсберг")
print(alla)
alla.remove_track("арлекино")
print(alla)

print(valera)
print("удаляем трек то что надо")
valera.remove_track("то что надо")
valera.add_track("то что надо")
print(valera)

print(pacany)
pacany.play_track("Музыкальный патриот")
