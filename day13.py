#use upper to conver all letter in big
str1 = "AbcDEfghIJ"
print("upper", str1.upper())

#using lower t convert all letter in small
str1 = "AbcDEfghIJ"
print("lower",str1.lower())

#using strip to remove spaces before and after the word
str2 = " Silver Spoon "
print("strip",str2.strip())

# using rstrip to remove trailing characters
str3 = "Hello !!!"
print("rstrip",str3.rstrip("!"))

#using replace tsring to replace words
str2 = "Silver Spoon"
print("replace",str2.replace("Sp", "M"))

#using split to split the string an specified instance and reurn final strings as list form
str2 = "Silver Spoon"
print("split",str2.split(" "))      

#using capitalize() convert into alphabetes first letter of every word
str1 = "hello"
capStr1 = str1.capitalize()
print("capitalize",capStr1)
str2 = "hello WorlD"
capStr2 = str2.capitalize()
print("capitalize",capStr2)

#using centre() to align the string to the center as per the given parameters
str1 = "Welcome to the Console!!!"
print("centre",str1.center(50))

#using characters
str1 = "Welcome to the Console!!!"
print("centre",str1.center(50, "."))\

#using count() to count the number of times the given value occured
str2 = "Abracadabra"
countStr = str2.count("a")
print("counter",countStr)

#using endswith() to check whether the given string ends with given character or not
str1 = "Welcome to the Console !!!"
print("endswith",str1.endswith("!!!"))
#also check inbetween values 
str1 = "Welcome to the Console !!!"
print("endswith",str1.endswith("to", 4, 10))

#using find() to find the first occurence of the given value and where it is present
str1 = "He's name is Dan. He is an honest man."
print("find",str1.find("is"))

#using index() to find the first occurrence of the given value and 
#where it is present(not present = -1 and present = index)
str1 = "He's name is Dan. He is an honest man."
print("find",str1.find("Daniel"))

str1 = "He's name is Dan. Dan is an honest man."
print("index",str1.index("Dan"))

#isalnum() to check whether the string have A-Z, a-z, and 0-9
#(entire) otherwise return false
str1 = "WelcomeToTheConsole"
print("isalnum",str1.isalnum())

#isalpha() to check whether the string have a-z, A-Z
str1 = "Welcome"
print("isalpha",str1.isalpha())

#islower() to check whether all characters of the string in lowercase or not
str1 = "hello everyone"
print("islower",str1.islower())

#isprintabale() to check whether the string is printable or not
str1 = "We wish you a Merry Christmas"
print("isprintable",str1.isprintable())

str2 = "We wish you a Merry Christmas\n"
print("isprintable",str2.isprintable())#here'\n' is not printable

#isspace() to check whether the string contains space or not
str1 = "        "       #using Spacebar
print("isspace",str1.isspace())
str2 = "        "       #using Tab
print("isspace",str2.isspace())
str3 = "    hii  my name is  khush"
print("isspace",str3.isspace())#it contains some word in string

#istitle() to check that the given string is an title or not
str1 = "Power Of The Unity"
print("istitle",str1.istitle())
str2 = "To kill a Mocking bird"
print("istitle",str2.istitle())

#isupper() to check the string's all characters are in uppercase or not
str1 = "WORLD HEALTH ORGANIZATION"
print("isupper",str1.isupper())

#startswith() to check whether the string start with given values or not
str1 = "!!@python is an interpreted language"
print("startswith",str1.startswith("!!"))
print("startswith",str1.startswith("python"))

#swapcase() to change the character casing of the string
str1 = "Python Is Interpreted Language"
print("swapcase",str1.swapcase())

#title() to convert the string in uppercase mode(all word's first letter)
str1 = "story of fairies"
print("title", str1.title())