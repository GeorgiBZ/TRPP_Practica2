import requests
import tarfile
import os
import shutil
from nicegui import ui


response = requests.get('https://dl-cdn.alpinelinux.org//alpine//v3.14//main//x86_64//APKINDEX.tar.gz')

with open('APKINDEX.tar.gz', 'wb') as tf:
    tf.write(response.content)

os.mkdir('main')

with tarfile.open('APKINDEX.tar.gz', "r:gz") as tf:
    tf.extractall('main')

os.remove('APKINDEX.tar.gz')





response = requests.get(' https://dl-cdn.alpinelinux.org/alpine/v3.14/community/x86_64/APKINDEX.tar.gz')

with open('APKINDEX.tar.gz', 'wb') as tf:
    tf.write(response.content)

os.mkdir('community')

with tarfile.open('APKINDEX.tar.gz', "r:gz") as tf:
    tf.extractall('community')

os.remove('APKINDEX.tar.gz')


f0 = open("Pack.txt", "w+")
f1 = open((os.getcwd() + "/community/APKINDEX"))
f2 = open((os.getcwd() + "/main/APKINDEX"))

f0.write(f1.read())
f0.write(f2.read())

f0.close()
f1.close()
f2.close()


package = "pulsemixer" #input("Зависимости какого пакета найти? ")

f = open("Pack.txt")
s = ""

for i in f.read().splitlines():
    if (i != ""):
        s += i + '\n'
    else:
        if (("P:" + package) == list(s.splitlines())[1]):
            break
        else:
            s = ""

#print(s)
f.close()

dependence = []

for i in list(s.split('\n')):
    if (i[0:2] == "D:"):
        dependence = list(i[2:].split(' '))


#print(dependence)

graph = "graph"

for i in dependence:
    graph += "\n\t"
    graph += package + " --> " + i + ";"




shutil.rmtree('main')
shutil.rmtree('community')
os.remove("Pack.txt")

ui.mermaid(graph)
ui.run()


print(graph)



