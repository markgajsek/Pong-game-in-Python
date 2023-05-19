import turtle #uvoz knjižnice turtle
import winsound #uvoz knjižnice winsound
import time #uvoz knjižnice time

#spremenljivke
zacetni_cas = time.time()

visina_okna=600
sirina_okna=800

zacetna_hitrost_loparja=0
zacetna_hitrost_zoge=0

#nastavi okno
okno = turtle.Screen()#novo okno
okno.title("Ping Pogn") #naslov
okno.bgcolor("light green") #barva ozadja
okno.setup(width=sirina_okna, height=visina_okna) #definicija okna s parametri
okno.tracer(0) #animacija se izklopi


#točke
tocke_skupaj=0#točke igralcev skupaj
tocke_igralca_a = 0 #točke za igralca 1
tocke_igralca_b = 0 #točke za igralca 2




lopar_a = turtle.Turtle() #nov turle lopar a
lopar_a.speed(zacetna_hitrost_loparja) #začetna hitrost
lopar_a.shape("square") #Oblika
lopar_a.color("blue") #barva 
lopar_a.shapesize(stretch_wid=6, stretch_len=1) #velikost loparja s parametri
lopar_a.penup() #dvigne turtke
lopar_a.goto(-345, 0) #levo začne risati



lopar_b = turtle.Turtle() 
lopar_b.speed(zacetna_hitrost_loparja)
lopar_b.shape("square")               #isto kot lopar a
lopar_b.color("red")
lopar_b.shapesize(stretch_wid=6, stretch_len=1)
lopar_b.penup()
lopar_b.goto(345, 0)




zoga = turtle.Turtle() #nov turtle zoga
zoga.speed(zacetna_hitrost_zoge) #zacetna hitrot
zoga.shape("circle") #oblika
zoga.color("yellow")#barva
zoga.penup() #dvigne turtle
zoga.goto(0, 0) #začne risati v sredini
zoga.dx = 0.45 #smer začetnega gibanja žoge po x osi
zoga.dy = -0.45 #smer začetnega gibanja žoge po y soi



#pen
pen = turtle.Turtle() #risanje nov turtle
pen.speed(0) #začetna hitrost risala
pen.color("white") #barva risala
pen.penup() #dvigni turtle
pen.hideturtle() #skrij turtle risalo
pen.goto(sirina_okna/sirina_okna, 250) #začetek risanja
pen.write("Igralec A : 0  Igralec B :0", align="center", font=("Arial", 25, "normal")) #napis nad igriščem 



#funkcije za premik loparja

def lopar_a_gor(): #definiraj premikanje loparja gor
    y = lopar_a.ycor() #y koorinata loparja
    y += 40 #hitrost za gor
    
    lopar_a.sety(y) #nove koordinate loparja 


def lopar_a_dol(): #definiraj premikanje loparja dol
    y = lopar_a.ycor() #y koorinata loparja
    y -= 40 #hitrost za dol
    
    lopar_a.sety(y) #nove koordinate loparja 



def lopar_b_gor():
    y = lopar_b.ycor()
    y += 40
   
    lopar_b.sety(y)  #enako kot lopar a


def lopar_b_dol():
    y = lopar_b.ycor()
    y -= 40
    lopar_b.sety(y)




    
okno.listen() #bere tipkovnico medtem ko program runna
okno.onkeypress(lopar_a_gor, "w") #w kliče funkcijo gor
okno.onkeypress(lopar_a_dol, "s") #s kliče funkcijio dol

okno.onkeypress(lopar_b_gor, "Up") #puščica gor kliče funkcijo gor
okno.onkeypress(lopar_b_dol, "Down") #puščica dol kliče funkcijo dol



#zanka
while True:
    
    okno.update() #posodobitev okna

    skupni_cas = time.time() - zacetni_cas #izračun skupnega časa

    #premik žoge
    zoga.setx(zoga.xcor() + zoga.dx) #prišteva koordinate od žoge v x smeri
    zoga.sety(zoga.ycor() + zoga.dy) #prišteva koordinate od žoge v y smeri


    #preverjanje kordinat žoge
    if zoga.ycor() > 300: #če je več kot 300 v y smeri
        zoga.sety(300) #se odbije
        zoga.dy *= -1 #spremeni smer gibanja
        winsound.PlaySound("lala",winsound.SND_ASYNC) #in zaigra se sound

    if zoga.ycor() < -300:      #enako na levi strani kot na desni
        zoga.sety(-300)
        zoga.dy *= -1
        winsound.PlaySound("lala.wav", winsound.SND_ASYNC) #zaigraj zvok
        
#lopar x koordinata preverjanje
    if zoga.xcor() > 400: #če je večje kot 400
        zoga.setx(400) #gre na 400
        zoga.dx *= -1 #spremeni smer žoge
        tocke_igralca_a += 1 #in doda točko
        tocke_igralca_b -= 0.5 #odvzame točko
        pen.clear() #izbris niza
        pen.write("igralec A :{}   igralec B : {}".format(tocke_igralca_a, tocke_igralca_b), align="center", font=("Arial", 25, "normal")) #napis in posodobitev točk

    if zoga.xcor() < -400:
        zoga.setx(-400)
        zoga.dx *= -1         #enako na levi kot na desni starni
        tocke_igralca_b += 1
        tocke_igralca_a -= 0.5
        pen.clear()
        pen.write("igralec A : {}  igralec B : {}".format(tocke_igralca_a, tocke_igralca_b), align="center", font=("Arial", 25, "normal"))


  
    if (zoga.xcor() > 340 and zoga.xcor() < 350) and (zoga.ycor() < lopar_b.ycor() + 40 and zoga.ycor() > lopar_b.ycor() - 40): #preverjanje trka med žogo in loparjem lopar je med 340 in 350
        zoga.setx(340) #nova koordinata žoge
        zoga.dx *= -1 #spreminjanje smeri žoge
        winsound.PlaySound("lala.wav", winsound.SND_ASYNC) #igraj zvok

    
    if (zoga.xcor() < -340 and zoga.xcor() > -350) and (zoga.ycor() < lopar_a.ycor() + 40 and zoga.ycor() > lopar_a.ycor() - 40): #lopar b enako kot lopar a
        zoga.setx(-340)
        zoga.dx *= -1
        winsound.PlaySound("lala.wav", winsound.SND_ASYNC)


    if (tocke_igralca_a == 11): #če igralec a doseže 11 končaj in izpiši
        print("Zmagovalec je igralec a")    
        break; #prekine while True

    if (tocke_igralca_b == 11):
        print("Zmagovalec je igralec b") #če igralec b doseže 11 končaj in izpiši
        break; #prekine while True
    if (tocke_igralca_b == 10 and tocke_igralca_a==10):
        print("Neodločeno je, ponovi!") #če igralec a in b imata 10 točk je neodločeno in se program zaključi
        break; #prekine while True
    if (tocke_igralca_a == - 3): #če igralec a doseže -3 točke končaj in izpiši
        print("Igralec a je avtomatsko zgubil")    
        break; #igra se konča, če igralec doseže 0 točk

    if (tocke_igralca_b == -3):
        print("Igralec b je avtomatsko zgubil") #če igralec b doesže -3 točke končaj izpiši
        break; #prekine while True
    
print("Čas igre: ", round(skupni_cas), "sekund.") #izpiši čas igre

