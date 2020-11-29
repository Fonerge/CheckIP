!/usr/bin/env python3

import os, time, json, urllib, requests

os.system('clear') #Очистка терминала.

CheckIP = True #Цикл для функций программы.

logo = """----------------------- 
CheckIP by Fonerge
--------------v 1.1----"""
print(logo) #Вывод логотипа.

time.sleep(2)

while CheckIP:

	a = str(input('[1] Пробить номер телефона.\n[2] Пробить IP-адрес.\n[3] Выход.\nВыберите действие --> '))

	if a == '3':		#Функция отключения программмы.
		time.sleep(2)
		os.system('clear')
		print('Удачного дня!')
		break

	if a == "1": 	   #Функция для пробива номера.
		phone = input("Введите номер телефона --> ")

		getInfo = ("https://htmlweb.ru/geo/api.php?json&telcod=" + phone)
		infoPhone = urllib.request.urlopen(getInfo)
		infoPhone = json.load(infoPhone)

		print("-" * 40)
		print("Номер сотового: ", "+" + phone)
		print("Страна: ", infoPhone["country"]["name"])
		print("Регион: ", infoPhone["region"]["name"])
		print("Округ: ", infoPhone["region"]["okrug"])
		print("Оператор: ", infoPhone["0"]["oper"])
		print( "Часть света: ", infoPhone["country"]["location"])
		print("-" * 40)

	elif a == "2":  #Функция для пробива ip-адреса
		getIP = input("Введите IP-адрес --> ")
		url = ("https://ipinfo.io/" + getIP + "/json") #Делаем запрос на json-данные.

		try:
			getInfo = urllib.request.urlopen(url) #Собираем json-данные с сайта.
		except:
			print( "\n[!] - IP not found! - [!]\n" )

		infoList = json.load(getInfo)	#Собираем json-данные в единную переменную.

		print("-" * 40)			#Выводим полученные данные.
		print("IP: ", infoList['ip'])
		print("Город: ", infoList['city'])
		print("Регион: ", infoList['region'])
		print("Страна: ", infoList['country'])
		print("Местоположение: ", infoList['loc'])
		print("Провайдер: ", infoList['org'])
		print("Часовой пояс: ", infoList['timezone'])
		print("-" * 40)
