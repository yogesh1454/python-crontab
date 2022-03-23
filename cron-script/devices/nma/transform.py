import sys
import os

print("Tranform Scripts Params: ", sys.argv)
print("Transform the nma file", sys.argv[2])

print(os.getcwd())
file = "output/"+sys.argv[4]

f = open(file, "w")
f.write("Now the file has more content!")
f.close()
print("Transfom file name is: ", sys.argv[4])

