import tarfile
filename = "archive/ar.tar"
file_obj = tarfile.open(filename,'r')
file = file_obj.extractfile("first.txt")
print("Content of the file are")
print(file.read())
file_obj.close()
