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
