class NumList:
    def findNum(self):
       self.a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
       self.x=self.a   
       for self.x in self.a:
         if self.x <= 5:
           print(self.x)
def main():
    n = NumList();
    n.findNum();
main();
