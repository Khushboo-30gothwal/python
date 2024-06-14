#first creating list of questions
l1 = ["what is the color of rose?"]
l2 = ["who is current prime minister of INDIA?"]
l3 = ["which party in year 2024 voting?"]

#creating option list for all questions
op1 = ["a.red", "b.pink", "c.yellow", "d.blue"]
op2 = ["a.modi", "b.rahul", "c.yogi", "d.none"]
op3 = ["a.bjp", "b.congress", "c.nda", "d.aap"]

#seeting questions with their correct answer
for i in l1:
  if op1 == "b.pink":
    print("sahi jvab")
  else:
    print("galat jvab")

for i in l2:
  if op2 == "a.modi":
    print("sahi jvab")
  else:
    print("galat jvab")

for i in l3:
  if op3 == "a.bjp":
    print("sahi jvab")
  else:
    print("galat jvab")

print("1st question in kbc of amount 1k is: ", l1, "and it's options are: ",
      op1)
print("give your answer ")