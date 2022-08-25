def Birthday():
    bir={"Albert Einstein":"01/12/2000",
         "Benjamin Franklin":"12/12/2000",
         "Ada Lovelace":"18/04/2000"}
    print("Welcome to the birthday dictionary. We know the birthdays of:")
    for i in bir:
        print(i)
    print("Who's birthday do you want to look up?")
    a=input()
    if a in bir:
        print(a,"s birthday is",bir[a])

Birthday()hh