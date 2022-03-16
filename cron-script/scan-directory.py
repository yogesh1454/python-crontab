import os
import sys
import subprocess
from devices import loader
from argparse import ArgumentParser

def device_transform(file):
    # Run subprocess.run and save output object
    output = subprocess.run(['python', '/Users/Shared/Workspace/Development/NikeBuild/python/cron-script/devices/nma/transform.py', '--filename',file])
    print('############### Transformation Done')
    print('Return code:', output.returncode)
    # use decode function to convert to string
   # print('Output:', output.stdout.decode("utf-8"))

def scan_directory(folder):

    files = os.listdir(folder)
    print("File to be process: ", files)

    for f in files:
        device_transform(f)
        loader.load_file(f)



# main
def main(folder):

    # for now we are scanning the folder for a network, in future we will scan it recursively for each network folder
    scan_directory(folder);

if __name__ == '__main__':
    print("Scan directoy")

    parser = ArgumentParser()
    parser.add_argument('-i', '--input', default='/Users/Shared/Workspace/Development/NikeBuild/python/cron-script/fileset/nma', help='Input path/to/file.csv', required=False)

    args = parser.parse_args()
    print("Displaying Input Parameters as: % s" % args.input)

    main(args.input)
    sys.exit(0)  #0 - success

