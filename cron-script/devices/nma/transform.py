import sys
import os

print("Transform the nma file", sys.argv)
print(os.getcwd())
file = "output/"+"transformed_"+sys.argv[2]

f = open(file, "w")
f.write("Now the file has more content!")
f.close()

