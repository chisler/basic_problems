import re

text = "https://stepik.org/lesson/Принцип-Дирихле-8163/step/54?discussion=55008&reply=292904"
#use re.findall to get all the links
links = re.findall('(\/lesson.*?step\/\d*)\?discussion=(\d+)(.*reply=(\d+))?', text)

print(links)