"""      
Не закончен классворк 
День 3.Неделя 2. 28 октября.
Тема: Словари       

#служит для описания объектов

Словарь - это изменяемый неупорядоченный тип данных, представляющий собой набор элементов по типу "ключ:значение".

Словари ещё называют ассоциативными массивами или хеш-таблицами.

Литерали являются {key:element,key:element}

Для нахождения конкретной информации без перебора при помощи ключа

Отличтельные свойства:
 * Не могут двух элементов с одинаковыми ключами, а одинаковые элементы, но различные ключи имеют место быть
 * Ключом может быть любой неизменяемый тип данных, а значением любой тип данных
 * Словарь неупорядоченный, обращение к элементам по индексу невозможно
 * Обращение возможно по ключам, заключенным в квадратные скобки

Методы:
 * get() 
 * update()
 * pop()

Можно перебирать с помощью метода items()
my_dict = {1: 'makers', 2 'bootcamp'}
for key.value in my_dict.items():
    print(key,value)

"""
# dict_ = {}
# dict_1 = dict()
# print(type(dict_))
# print(dict_1)



# dict4 = {'1':'value', 3:'value2'}
# some_dict = {'a':1,'b':2,'a':3}
# print(some_dict)

# headphones = {'brand':'Hoco', 'model': 'W28', 'color':'white','type':'wireless'}
# print(headphones['brand']) #Hoco
# print(headphones['type']) #W28
# print(headphones['volume']) # KeyError 'volume'

"""
В словарях есть ключ пары

"""

# my_dict ={"name": "Sam", "last_name": "White", "age": "23"}
# print(type(my_dict)) #class 'dict'


"""
Альтернативный способ создания словарей с помощью конструкции dict() -возвращает словарь
Но на его создание накладываются некоторый ограничения
"""
# my_dict = dict(a =1, b=2, c=3)
# print(my_dict) #{'a': 1, 'b': 2, 'c': 3}
# my_dict2 = {'a':1, 'b':2, 'c':3}
# print(my_dict2) #{'a': 1, 'b': 2, 'c': 3}


"""
Превращение списка  и кортежа в словарь
Но вид списка должен выглядеть так, если будет иметь другой вид выдадут ошибку
Таким же образом можно превратить кортеж в словарь
"""
# my_list = [['m',1],['b',3],['c',6]]
# my_dict = dict(my_list)
# print(my_dict) #{'m': 1, 'b': 3, 'c': 6}

# my_tuple = (('m',1),('b',3),('c',6))
# my_dict = dict(my_tuple)
# print(my_dict) #{'m': 1, 'b': 3, 'c': 6}


"""
Таким образом мы можем совмещать альтарнативные способы создания словарей
и создать новый расширенный словарь
"""
# my_list = (('m',1),('b',3),('c',6))
# my_dict = dict(my_list, a=1,b=3,c=3)
# print(my_dict) #{'m': 1, 'b': 3, 'c': 3, 'a': 1}


"""
Ключи могут только неизменяемый тип данных, а его значение любой тип данных

"""
# dict_ = {1:'Makers', '2': True, False: []}
# print(dict_)

# dict_ ={[list]: 'list'}
# print(dict_) #unhashable type: 'list'


"""
Начиная с версии Python 3.6
Принт выводит словарь как упорядоченный
Но все же к ним нельзя применять идентификацию, то есть нужно запомнить, что он все же относится к неупорядоченному типу
"""
# dict_ = {1:'Makers', '2': True, False: []}
# print(dict_)


"""
Обращение к словарю при помощи ключа для получения его элемента

"""
# dict_ ={'Tom': 'black',
#         'Alice': 'yellow',
#         'Sam': 'green'}
# print(dict_['Alice']) #yellow


"""
Как изменить элемент словаря и добавить к нему новый элемент ? #добавление
dictionary['key'] = 'element' -для добавления нового элемента или изменения старого

"""
# dict_ ={'Tom': 'black',
#         'Alice': 'yellow',
#         'Sam': 'green'}
# dict_['Alice'] = 'pink'
# # print(dict_) #{'Tom': 'black', 'Alice': 'pink', 'Sam': 'green'}
# dict_['Raychel']='blue'
# print(dict_) #{'Tom': 'black', 'Alice': 'pink', 'Sam': 'green', 'Raychel': 'blue'}


# a = {'name': 'Ivan','last_name':'Petrov'}
# a['age']=25
# print(a)



"""
Методы словарей
"""

"""
get(key, None)- принимает ключ и возвращает его значение, 
если этого ключа не существует возвращает None

Отличается от обычного получения значения с помощью [], 
тем что если ключа нет он возвращеет None по умолчанию
, но его можно изменить добавив get(key,'str')
"""
# my_dict = {1:'Tom', 2:'John', 3:'Alice'}

# print(my_dict.get(3))
# print(my_dict.get(5, 'No such key'))


"""
clear() - очищает словарь

"""
# my_dict = {1:'Tom', 2:'John', 3:'Alice'}
# my_dict.clear()
# print(my_dict) #{}
# print(id(my_dict))


"""
copy() - копирует один словарь в другой

"""
# my_dict = {1:'Tom', 2:'John', 3:'Alice'}
# my_dict2 = my_dict
# my_dict[2]= 'Rachel'
# print(my_dict) #{1: 'Tom', 2: 'Rachel', 3: 'Alice'}
# print(my_dict2) #{1: 'Tom', 2: 'Rachel', 3: 'Alice'}

# my_dict = {1:'Tom', 2:'John', 3:'Alice'}
# my_dict2 = my_dict.copy()
# my_dict[2]= 'Rachel'
# print(my_dict) #{1: 'Tom', 2: 'Rachel', 3: 'Alice'}
# print(my_dict2) #{1: 'Tom', 2: 'John', 3: 'Alice'}


"""
pop(key,default)- удаляет элемент по ключу, но может возвратить удаленный элемент, если обратиться к нему через print. 
Если такого элемента нет и value не здан, то происходит KeyError. 
Если value не задан возвращает value

"""
# dict_ = {'name': 'Kate', 'height':170, 'weight':0}
# print(dict_.pop('weight')) #50
# # deleted =dict.pop('age','no such key in dictionary')
# # print(dict_) #{'name': 'Kate', 'height': 170}
# # print(deleted)

# a = {'a':1,'b':3,'c':4}
# deleted =a.pop('e',6)
# print(deleted) #KeyError
# print(a)

# key = 'e'
# a = {'a':1,'b':3,'c':4}
# deleted =a.pop(key ,None)
# print(deleted) #None
# print(a) #{'a': 1, 'b': 3, 'c': 4}
"""
popitem() - удаляет любую пару ключ значение, но начиная с версии 3.6 удаляет последнее значение

"""
# dict_ = {'name': 'Kate', 'height': 170, 'weight': 50}
# print(dict_.popitem()) #('weight', 50)
# print(dict_)  # {'name': 'Kate', 'height': 170}


"""
setdefault(key, default) - возвращение по ключу
Отличается от других способов получению по ключу, 
тем что если данного ключа нет, то можно вместо default написать любое значение и мы получем значение default

"""
# dict_ = dict(a=1,b=3,c=4)
# print(dict_.setdefault('d',5)) 


"""
update()- расширяет один словарь за счет другого

"""
# dict1 = {1:'Tom', 2:'Alice'}
# dict2 = {3:'Bob',4:'JOhn'}
# dict1.update(dict2)
# print(dict1) #{1: 'Tom', 2: 'Alice', 3: 'Bob', 4: 'JOhn'}
# print(dict2) #{3: 'Bob', 4: 'JOhn'}

# dict1 = {1:'Tom', 2:'Alice'}
# dict2 = {2:'Bob',4:'JOhn'}
# dict1.update(dict2)
# print(dict1) #{1: 'Tom', 2: 'Bob', 4: 'JOhn'}
# print(dict2) #{2: 'Bob', 4: 'JOhn'}


"""
fromkeys(seq, value) -  берет из последовательностью, которую мы берем и 
делает из элементов этой последовательности ключи  и вторым элементом принимает значени для каждого ключа.

"""
# numbers = [1,2,3,4,5]
# new_dict = dict.fromkeys(numbers,'makers')
# print(new_dict) #{1: 'makers', 2: 'makers', 3: 'makers', 4: 'makers', 5: 'makers'}


"""
Перебор элементов словаря

items()- возвращает ключи и значения
keys()- возвращает только ключи
values()- возвращает только значения
"""
# dict_ ={'name':'Kate', 'height':170, 'weight':50}

# print(dict_.items())  #dict_items([('name', 'Kate'), ('height', 170), ('weight', 50)])
# print(dict_.keys())   #dict_keys(['name', 'height', 'weight'])
# print(dict_.values()) #dict_values(['Kate', 170, 50])


# a = {'name': 'Jack','last_name':'Jones'}

# a.keys()   #dict_keys(['name','last_name])
# a.values()  #dict_values(['Jack','Jones'])
# a.values() #dict_item(['name','Jack'], 'last_name','Jones')

"""
Пример перебора элементов словаря с помощью цикла for
При переборе словаря, если не указывают по чему именно перебирает, Питон перебирает только ключи

"""
# contacts ={
#     'Alice': '+9965053553353',
#     'John': '+996535353453',
#     'Sam':'+9963453453543'}

# for info in contacts:
#     print(info) # выводит только ключи, если не применять никаие методы
 
# for name,tel in contacts:
#     print(name,tel) #too many values to unpack (expected 2)

# for key, val in contacts.items():
#     print(f'Name: {key}, tel: {val}') # получаем и ключи, и элементы. Также можно применять вместо items() : key(s), values()
"""
обход по ключам:
"""
# a={'a':13,'b':43,'c':56}

# for key in a:
#     print(key)

# for key in a.keys():
#     print(key)
"""
обход по значениям:

"""
# a={'a':13,'b':43,'c':56}

# for i in a.values:
#     print(i)

# for key in a:
#     print(a[key])

"""
обход по элементам:
"""
# a={'a':13,'b':43,'c':56}

# for item in a.items():
#     print(item[0])
#     print(item[1])

# for key,value in a.items():
#     print(key)
#     print(value)


# nested_dictionary = {
#     'Makers': {
#         'Aibek': 23,
#         'Adilet':27,
#         'Aidai':21,
#         'Nurbek':{
#         'age':18,
#         'height':190,
#         'weight':80}
#     }
# }
# # print(nested_dictionary['Makers']) #{'Aibek': 23, 'Adilet': 27, 'Aidai': 21}
# print(nested_dictionary['Makers']['Nurbek']['height']) #190



"""
Classrwork. Классная работа
"""


"""
1) Создайте словарь university, и заполните данными, 
которые бы отражали количество учащихся на разных факультетах (программирование, экономика, медицина). 
Внесите изменения в словарь согласно следующему: 
а) в одном из факультетов изменилось количество учащихся, 
б) в университете появился новый факультет(лингвистика), 
с) в университете был расформирован (удален) другой факультет (медицины). 
Вычислите общее количество учащихся в университете.
"""
# писать код здесь
# university = {}


"""
2) Создайте словарь, где ключами являются числа, а значениями – строки. Поменяйте ключи и значения местами.
Например: исходный словарь - {1: ‘a’, 2: ‘b’, 3: ‘c’}
На выходе - {‘a’: 1, ‘b’: 2, ‘c’: 3}
"""
# писать код здесь


"""
3) Создайте программу, которая запрашивает у вас количество гостей, которых вы хотите пригласить. Далее запрашивает у вас имена гостей поочередно. Как только вы введете последнего гостя программа должна выдать вам список гостей и их порядковые номера в виде словаря.
"""
# писать код здесь


"""
4) Вы идете в магазин за продуктами. У вас есть список продуктов, в котором перечислены наименования продуктов и количество. Каждый раз, когда вы кладете тот или иной продукт в корзину, вы убираете этот продукт из списка. После того, как ваш список опустеет, вы идете к кассе и расплачиваетесь. Реализуйте данную задачу в вашем коде.
* Используйте все знания, которые вы получили
"""
# писать код здесь




"""         Task.Таски  """
"""
1.Создайте словарь

 a = {'x': 1, 'y': 2, 'z': 1}
и распечатайте один из ключей

"""
# a = {'x': 1, 'y': 2, 'z': 1}
# for key in a.keys():
#     print(key)
#     break
"""
2.Объявите словарь

 a = {'a': 1, 'b': 2, 'c': 1}
удалите один из элементов и распечатайте удалённый элемент.

"""
# a = {'a': 1, 'b': 2, 'c': 1}
# print(a.pop('a'))

"""
3.Объявите словарь

a = {'a': 1, 'b': 2, 'c': 1}
добавьте в него новую пару ключ: значение

{'f': 55}
специальным методом и распечатайте.

"""
# a = {'a': 1, 'b': 2, 'c': 1}
# a['f']=55
# print(a)
"""
Oбъявите словарь

a = {'a': 1, 'b': 2, 'c': 1}
удалите всего его элементы специальным методом и распечатайте словарь. Результат в терминале, должен быть такой:

{} 

"""
# a = {'a': 1, 'b': 2, 'c': 1}
# a.clear()
# print(a)

"""
5.Дан словарь

 a = {'a': 1, 'b': 2, 'c': 1}
выведите все его ключи методом словаря, то есть только a, b, c

"""
# a = {'a': 1, 'b': 2, 'c': 1}
# print(list(a.keys()))


"""
7.Дан словарь

 a = {'a': 1, 'b': 2, 'c': 1}
пройдитесь по нему циклом и распечатайте все ключи.

"""
# a = {'a': 1, 'b': 2, 'c': 1}
# for key in a.keys():
#     print(key)


"""
9.Создайте словарь a с числовыми значениями. Создайте новый словарь b, такой же как словарь а, но все четные значения замените на 2.

 Пример: Ввод -> 
 a = {'a': 1, 'b': 4, 'c': 1, 'd': 5, 'e': 6} 
 Вывод -> 
 b = {'a': 1, 'b': 2, 'c': 1, 'd': 5,  'e': 2}

"""
# a = {'a': 1, 'b': 4, 'c': 1, 'd': 5, 'e': 6} 
# b =a.copy()
# b['b']=2
# b['e']=2
# print(b)

"""
10.Дан словарь, удалите из него все элементы с пустыми значениями.

Пример:

 a = {'a': None, 'b': 1, 'c': 2, 'd': None, 'e': 3}
->

 {'b': 1, 'c': 2, 'e': 3}

"""
# a = {'a': None, 'b': 1, 'c': 2, 'd': None, 'e': 3}
# a.pop('a')
# a.pop('d')
# print(a)


"""
11.Создайте словарь a, где ключами будут названия товаров, а значениями их цены, затем пройдитесь циклом по нему и 
поменяйте все значения элементов, разделив их на 5.

Ввод:

a = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25} 
Вывод:

{'apple': 0.08, 'orange': 0.06999999999999999, 'banana': 0.05} 

"""
# a = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25} 
# a['apple'] = 0.08
# a['orange'] =0.35
# a['banana']=0.05
# print(a)

"""
12.Создайте словарь где ключами будут фрукты, а значением их цены. Удалите те элементы, значение которых будет чётным (специальным методом) и 
распечатайте результат.

Ввод:

a = {'apple': 2, 'orange': 5, 'banana': 10} 
Вывод:

{'orange': 5} 

"""
# a = {'apple': 2, 'orange': 5, 'banana': 10} 
# a.pop('apple')
# a.pop('banana')
# print(a)


"""
13.Создайте словарь, затем поменяйте местами ключи и значения. Распечайте полученный результат.

Ввод:

a = {'a': 1, 'b': 2, 'c': 3} 
Вывод:

{1: 'a', 2: 'b', 3: 'c'} 

"""
# a = {'a': 1, 'b': 2, 'c': 3} 
# b=dict()
# for key,value in a.items():
#     b[value]=key
# print(b)
"""
14.Создайте словарь, где значениями будут являться числа. Найдите сумму этих значений и распечатайте результат.

Ввод:

a = {'a': 3, 'b': 2}
Вывод: 5

"""
# a = {'a': 3, 'b': 2}
# b = a['a']+a['b']    
# print(b)
"""
15.Создайте любой словарь тремя возможными способами.

"""
# a1={'a':1,'b':2}
# a2=dict()
# a3 = {a: a ** 2 for a in range(7)}
# print(a1,a2,a3)
                       
"""
Экстра задание 2
Напишите код, который создает словарь следующим образом, вам дана строка, например:

string = "pythonist" 
нужно создать новый словарь, ключами которого будут буквы строки, а значениями числа, соответствующие количеству повторений данной буквы в строке.

dict_ = {"p":1, "y":1, "t":2, "h":1, "o":1, "n":1, "i":1, "s":1} 

"""
# string = "pythonist" 
# dict_={}
# keys =[]
# for key in string:
#     keys.append(key)

# dict_=dict.fromkeys(keys,1)
# for key1 in dict_:
#     if key1 =='t':
#         dict_['t']=2
        
# print(dict_)

"""
Extra Task3

Создайте словарь в переменной school и заполните данными, 
которые бы отражали количество учащихся в разных классах. 
Например: school = {'1a':20,'2a':30,'3a':30} 
Далее сделайте копию словаря school в переменную school2 
Внесите следующие изменения в словарь school2: 
а) в первом классе изменилось количество учащихся, теперь там учится 25 человек. 
Необходимо обновить словарь специальным методом. 
б) в школе появился новый класс 7a c количеством учащихся: 10. 
Добавьте его тем же методом что и в предидущем условии. 
с) в школе был расформирован (удален) второй класс. 
Удалите второй элемент специальным методом 
d) вычислите общее количество учащихся и запишите результат 
в перменную total затем распечатайте результат. 


"""

# school = {'1a':20,'2a':30,'3a':30} 
# school2 = school.copy() 
# school2.update({'1a':25}) 
# school2.update({'7a':10}) 
# school2.pop('2a') 
# total = sum(school2.values()) 
# print(total)

"""
Молодец!!!
Тема пройдена :)
"""