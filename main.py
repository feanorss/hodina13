# class LinkedList:
#     def __init__(self):
#         self.head = None
#
#     def vloz(self, prvok):
#         if self.head is None:
#             self.head = prvok
#         else:
#             aktualny = self.head
#             while aktualny.next:
#                 aktualny = aktualny.next
#             aktualny.next = prvok
#
#
#
#     def vypis(self):
#         if self.head is None:
#             print("Zoznam je praydnz")
#         else:
#             aktualny = self.head
#             print(aktualny.data)
#             while aktualny.next:
#                 aktualny = aktualny.next
#                 print(aktualny.data)
#
#     def obsahuje(self, meno):
#         aktualny = self.head
#         if aktualny.data == meno:
#             return True
#         while aktualny.next:
#             aktualny = aktualny.next
#             if aktualny.data == meno:
#                 return True
#         return False
#
#     # def vymenit(self, meno):
#     #     aktualny=self.head
#     #     while aktualny.next:
#     #         aktualny = aktualny.next
#     #         if aktu
#
# class Prvok:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#
# mojLinked = LinkedList()
# # prvok1 = Prvok("Milan")
# # mojLinked.vloz(prvok1)
# # prvok2 = Prvok("Jozo")
# # mojLinked.vloz(prvok2)
# # prvok3 = Prvok("Fero")
# # mojLinked.vloz(prvok3)
# mojLinked.vypis()
# print("test")
# # print(mojLinked.obsahuje("Jozo"))
# # print(mojLinked.obsahuje("Milan"))

# import json
# class Student():
#     def __init__(self, name, age, country):
#         self.name = name
#         self.age = age
#         self.country = country
#         self.studentov_kamos=None
#
#     def __str__(self):
#         return f"Student sa vola {self.name} z krajiny {self.country} a ma {self.age} rokov"
#
#
#     def to_json(self):
#         return json.dumps(self, default=lambda obj: obj.__dict__)
#     def vloz_do_suboru(self, nazov_suboru):
#         with open(nazov_suboru, "w") as file:
#             file.write(self.to_json())
#             # pickle.dump(self,file)
#
#     # @staticmethod
#     # def vytvor_zo_suboru(nazov_suboru):
#     #     with open(nazov_suboru, "rb") as file:
#     #         return pickle.load(file)
#
#
# patrik = Student("Patrik",30,"Slovakia")
# milan = Student("Milan",33,"Italy")
# patrik.studentov_kamos=milan
# patrik.vloz_do_suboru("patrik.json")
# # patrik_zo_suboru=Student.vytvor_zo_suboru("patrik.dat")
# # print(patrik_zo_suboru)
# # print(patrik)
# # serialized=pickle.dumps(patrik)
# # print(serialized)
# # patrik_obnoveny=pickle.loads(serialized)
# # print(patrik_obnoveny)

