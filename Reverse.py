def reverse(x):
  rev_sentence = x.split();
  result = []
  for word in rev_sentence:
    result.insert(0,word)
  return " ".join(result)
def main():
  sentence = input("Enter a sentence: ")
  print(reverse(sentence))
main();
