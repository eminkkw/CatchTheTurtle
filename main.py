'''
> Nasıl bir karakterin başka yerlere spamlanması
> Geri sayan sayaç
> Karakterin üzerine tıklandığı zaman nasıl score artabilir
'''
import turtle
from turtle import Screen, Turtle
import random

FONT = ('Arial', 20, 'normal')

def countdown(time):
    emin.clear()

    if time > 0:
        emin.goto(0, 150)
        emin.penup()
        emin.write(time, align='center', font=FONT)
        screen.ontimer(lambda: countdown(time - 1), 1000)
    else:
        emin.write("Click Screen", align='center', font=FONT)



emin = Turtle()
emin.hideturtle()
emin.write("Click Screen", align='center', font=FONT)

# Karakteri oluştur
karakter = Turtle()
karakter.shape("turtle")

screen = Screen()
screen.bgcolor("orange")
countdown(20)

# Rastgele konuma gitmek için fonksiyon tanımla
def rastgele_konum():
    x = random.randint(-200, 200)  # X koordinatı için rastgele değer
    y = random.randint(-200, 200)  # Y koordinatı için rastgele değer
    karakter.penup()  # Çizim yapmadan hareket etmek için
    karakter.goto(x, y)  # Rastgele konuma git

# Tıklama olayına tepki veren fonksiyonu tanımla
def tıklama(x, y):
    karakter_tıklama(x, y)

# Karakterin üzerine tıklama olayına tepki veren fonksiyonu tanımla
def karakter_tıklama(x, y):
    rastgele_konum()

counter = 0
def karakter_tıklandığında(x,y):
    global counter
    counter += 1
    sayac_guncelle()

sayac = turtle.Turtle()

def sayac_guncelle():
    sayac.goto(0,100)
    sayac.penup()
    sayac.clear()
    sayac.write(counter, font=FONT)

kazandın = turtle.Turtle()

sayac_guncelle()
# Tıklama olayını ekrana bağla
screen.onclick(tıklama)
karakter.onclick(karakter_tıklama)
karakter.onclick(karakter_tıklandığında)

screen.mainloop()
