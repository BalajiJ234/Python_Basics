def removeDuplicates(x):
  listB = []
  for i in x:
    if i not in listB:
      listB.append(i)
  return listB

def main():
    listA = [int(x) for x in input().split()]
    print("THIS IS LIST WITH DUPLICATES.....",listA)
    print("THIS IS THE NEW LIST AFTER REMOVING DUPLICATES....",removeDuplicates(listA))
main();
