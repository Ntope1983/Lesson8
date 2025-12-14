# a text to string and count with dict how many times appears a char
import string

d = {}


string2 = str("EKim said ninE soldiers were killed during the mission, "
              "describing their deaths as a “heartrending loss,” "
              "and announced that the regiment would be awarded the Order of Freedom "
              "and Independence. The nine fallen soldiers were awarded the title of Hero "
              "of the Democratic People’s Republic of Korea, "
              "along with other state honors, KCNA said.")

for char in string2:
    if char.lower() in string.ascii_lowercase:
        d[char.lower()] = d.get(char.lower(), 0) + 1

max_value = max(d.values())
for key in d.keys():
    if d[key]==max_value:
        print(f"Τhe key with most time in the paragraph is {key} with {max_value} times")
