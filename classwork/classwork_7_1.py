name = "    +  aleX    bu  sh!,.  sB        "

######################################################################################
# delete whitespaces left right
# print(id(name))
name = name.strip()
print(id(name))

name = name.title()
print(name)

name = name.strip("!,.==-_+_ ")
print(name)

name = name.upper()
print(name)
name = name.lower()
print(name)

# name = " " + name
name = name.capitalize()
print(name)

name = name.replace("  ", " ").replace("  ", " ")
print(name)

name = name.replace("bu sh", "bush")
print(name)

german = "ß"
german_s_lower = german.lower()
print(german_s_lower)
german_s_upper = german_s_lower.upper()
print(german_s_upper)