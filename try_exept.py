createFile = open("myfile2.txt", "x")
with open("myfile2.txt", "w") as file:
    file.write("1\n")
    file.write("96\n")
    file.write("34\n")
    file.write("91\n")
    file.write("678\n")
    file.write("276\n")
    file.write("3")
file.close()
total = 0
with open('myfile2.txt') as infile:
        for line in infile:
            try:
                num = int(line)
                total += num
            except ValueError:
                print(
                    "'{}' is not a number".format(line.rstrip())
                )
print(total)
infile.close()
