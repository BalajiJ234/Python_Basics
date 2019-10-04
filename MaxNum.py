def maxfunction(a,b,c):
   if (a > b) and (a > c): Res=a
   elif (b > a) and (b > c): Res=b
   elif (c > a) and (c > b): Res=c
   return Res
def main():
    n1=input("ENTER THE NUMBER 1 : ")
    n2=input("ENTER THE NUMBER 2 : ")
    n3=input("ENTER THE NUMBER 3 : ")
    maxNum=maxfunction(n1,n2,n3)
    print("MAXIMUM NUMBER IS....",maxNum);
main();
