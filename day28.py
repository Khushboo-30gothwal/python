line = "my name is {} and i am a {} of mnit jaipur having branch {}"
name = "khush"
profession = "student"
branch = "cse"

print(line.format(name,profession,branch))
print(".........difference......")
print(line.format(name,branch,profession))

line1 = "my name is {0} and i am a {2} of mnit jaipur having branch {1}"
print("..........difference........")
print(line1.format(name,branch,profession))

# format method is esay for short lines not large
# it will be confusing in large no of lines
# so f_string come inn scene to reduce the problem occuring through 
# format method in large amount of lines