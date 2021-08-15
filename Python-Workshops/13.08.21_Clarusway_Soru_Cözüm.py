# With List Comprehension Solutions


# ----------------------------------------


# https://edabit.com/challenge/vTGXrd5ntYRk3t6Ma

# Solution 1

# def is_isogram(txt):
#     txt = txt.lower()
#     for letter in txt:
#         if txt.count(letter) > 1: 
#             return False
#     return True
# print(is_isogram("HheLlo"))

# Solution 2

# def is_isogram(txt):
#     return len(txt) == len(set(txt.lower()))
# print(is_isogram("Heloh"))


# -------------------------------------------


# https://edabit.com/challenge/6CGomPbu3dK536PH2

# Solution 1

# def accumulating_list(lst):
#     k=0
#     t=[]
#     for i in range(len(lst)):
#         k=k+lst[i]
#         t.append(k)
#     return t
# print(accumulating_list([1, 2, 3, 4]))

# Solution 2

# def accumulating_list(lst):
#     return [sum(lst[0:i+1]) for i in range(len(lst))]
# print(accumulating_list([1, 2, 3, 4]))


# -----------------------------------------


# https://edabit.com/challenge/rQkriLJBc9CbfRbJb

# Solution 1

# def index_of_caps(word):
#     result = []
#     for letter in word:
#         if letter.isupper():
#             result.append(word.index(letter))
#     return result
# print(index_of_caps("eDaBiT"))

# Solution 2

# def index_of_caps(word):
# 	return [word.index(letter) for letter in word if letter.isupper()]
# print(index_of_caps("eDabiT"))


# ------------------------------------------------


# https://edabit.com/challenge/646cCaFig6AP89YRo

# Solution 1

# def fizz_buzz(num):
#     a=[]
#     for i in range(1,num+1):
#         if not i%15 :
#             a.append('FizzBuzz')
#         else:
#             if not i%5:
#                 a.append('Buzz')
#             else: 
#                 if not i%3:
#                     a.append('Fizz')
#                 else:
#                     a.append(i)
#     return a
# print(fizz_buzz(15))

# Solution 2

# def fizz_buzz(num):
#   return ['FizzBuzz' if not n%15 else 'Buzz' if not n%5 else 'Fizz' if not n%3 else n for n in range(1,num+1)]
# print(fizz_buzz(15))


# ------------------------------------------


# https://edabit.com/challenge/fmQ9QvPBWL7N9hSkq

# Last List Comprehension Question
# Solution 1

# def unstretch(word):
#     return word[0]+"".join([word[i] for i in range(1,len(word)) if word[i]!=word[i-1]])
# print(unstretch("ppooeemmm"))

# Solution 2

# def unstretch(word):
#     return ''.join([x for x,y in zip(word,word[1:]) if x!=y]) + word[-1]
# print(unstretch("ppooeemmm"))


# -----------------------------------------


# Write a Python code to sort the list at below without using .sort() method of list. elements of list = [999, 333, 2, 8982, 12, 45, 77, 99, 11] Expected output: [2, 11, 12, 45, 77, 99, 333, 999, 8982]

# Solution 1

# list_ = [999, 333, 2, 8982, 12, 45, 77, 99, 11]
# new_list = []

# while list_:
#     min_element = list_[0]
#     for i in list_:
#         if i < min_element:
#             min_element = i
#     new_list.append(min_element)
#     list_.remove(min_element)
# print(new_list)

# Solution 2

# my_list = [999, 333, 2, 8982, 12, 45, 77, 99, 11]
# for i in range(len(my_list)):
#     for j in range(i+1, len(my_list)):
#         if my_list[i] > my_list[j]:
#             my_list[i], my_list[j] = my_list[j],  my_list[i]
# print(my_list)


# -------------------------------------------


# Bir dize kabul eden ve büyük harf ve küçük harf sayısını hesaplayan bir Python işlevi yazın. 
# Örnek Dizge : 'The quick Brow Fox'
# Beklenen Çıktı :
# Büyük harf karakter sayısı : 3
# Küçük harf karakter sayısı : 12

# Solution

# string_ = "The quick Brow Fox"
# new_string_ = "".join(string_.split(" "))
# up , low = 0, 0
# for i in new_string_:
#     if i.isupper():
#         up += 1
#     else:
#         low += 1
# print("Büyük harf karakter sayısı : {}\nKüçük harf karakter sayısı : {}".format(up,low))


# -------------------------------------------


# https://www.reddit.com/r/clarusway/comments/o2t0uj/do_you_want_to_solve_an_interview_question_that/


# Solution

# a=[[1,2,3],[4,5,6],[7,8,9]]
# for i in range(len(a)):
#     for j in range(i,len(a)):
#         a[i][j], a[j][i] = a[j][i], a[i][j]
# for i in a:
#     i.reverse()
# print(a)

# -------------------------------------------

#map ve filtre fonksiyonu bir arada bir cözüm
# Bu listede "ek" ifadesini barindiran sözcüklerin uzunluklarini bir listeye yazdiralim

# liste_1 = ["sarma", "ekeske", "börek", "ekmek", "dolma", "kebap"]

# liste_2 = filter(lambda x:"ek" in x, liste_1)
# liste_3 = map(lambda x:len(x),liste_2)
# print(list(liste_3))

