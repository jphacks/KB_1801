import os

num = 2
os.system('touch hoge.txt')
f = open('hoge.txt', 'w')
f.write(str(num))
f.close()
os.system('scp ./hoge.txt pi@192.168.179.4:/home/pi/jpHackason/lineapi/info/hoge.txt')


