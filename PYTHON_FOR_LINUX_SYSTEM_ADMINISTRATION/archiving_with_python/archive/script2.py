import tarfile

filename = "bk.tar"

fileObj = tarfile.open(filename,"w")
fileObj.add("./data/first.txt")
fileObj.add("./data/second.txt")
fileObj.close()

