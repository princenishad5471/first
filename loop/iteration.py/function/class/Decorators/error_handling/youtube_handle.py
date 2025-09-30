file=open("youtube.txt", "w")

try:
    file.write("chai or coffee")
finally:
    file.close()

with open("youtube.txt", "w") as file:
    file.write("coffee or python")