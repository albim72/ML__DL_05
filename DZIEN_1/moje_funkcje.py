print("To jest test skryptu main.py")
#przykład 1 - funkcja
n=100

def ax(a):
    return a**3+10
def policz(a:int,b:int,c:int,y:float=9)->int:
    global n
    n = (a+b)*y-c+n + ax(c)
    return n

print(policz(4,3,1,4))
print(policz(2.2,3,0.45,4))
print(policz(56,True,0.005,-3))
print(policz(3,8,3.5))
print(n)

#przykład 2 - funkcje anonimowe

print((lambda a:a+16)(17))
s = lambda a,b,z=3:(a*b-2*z)/(a+b+z)
print(s(2,5,7))
print(s(2,5))

num = [56,3,63,-64,0,210,432,2132,-34,-453,333,0,190,267]

#zadanie - -utwórz listę nbparzyste i przekaż do niej elementy list num o wartości parzystej

nbparzyste = list(filter(lambda x:x%2==0,num))
print(nbparzyste)

#utwórz nową listę cube i przekaż do niej elementy list num podmniesione do potęgi trzeciej
cube = list(map(lambda x:x**3,num))
print(cube)

#funkcje wyższego rzędu
from bfunkcje import konkurs,bonus

def witaj(imie):
    return f"Miło Cię widzieć {imie}"

def osoba(funkcja,*args):
    return funkcja(*args)

print(osoba(witaj,"Olaf"))
print(osoba(konkurs,"Alicja",67,13))
print(osoba(bonus,67,20))
print(osoba(bonus,33,20))
