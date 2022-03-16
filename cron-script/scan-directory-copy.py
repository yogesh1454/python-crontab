import os
import sys
import subprocess
from argparse import ArgumentParser

def process_file(file):
    # Run subprocess.run and save output object
   # output = subprocess.run(['python', '/Users/Shared/Workspace/Development/NikeBuild/python/hello.py'], capture_output=True)
    output = subprocess.run(['python', '/Users/Shared/Workspace/Development/NikeBuild/python/hello.py'])
    print('###############')
    print('Return code:', output.returncode)
    # use decode function to convert to string
    print('Output:', output.stdout.decode("utf-8"))

def scan_directory(folder):
    files = os.listdir(folder)
    for f in files:
        print("file name:", f)
        process_file(f)



# main
def main(folder):
    scan_directory(folder);

if __name__ == '__main__':
    print("Scan directoy")
    parser = ArgumentParser()

    parser.add_argument('-i', '--input', default='../cron-script', help='Input path/to/file.csv', required=False)
    parser.add_argument('-oc', '--output-csv', help='Output path/to/confusion_matrix.csv', required=False)

    args = parser.parse_args()
    print("Displaying Output as: % s" % args.input)


    main(args.input)
    sys.exit(0)  #0 - success

