import os

print("Current working Directory")
print(os.getcwd())

print("creating directory ...")
os.mkdir("./mytestdir")

print("List current dir")
print(os.listdir())


filename = "test.txt"


## creating an empty file

with open(filename,"w"):
    pass


os.rename(filename,"renamedfile.txt")
print("rename complete")
