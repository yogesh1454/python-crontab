import os
import sys
import subprocess
from devices import loader
from argparse import ArgumentParser
import logging
import logging.config
import yaml
# Property based logging
# logging.config.fileConfig(fname='logger.conf', disable_existing_loggers=False)

# yaml file based logging
with open('logger.yaml', 'r') as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)


# Get the logger specified in the file
logger = logging.getLogger(__name__)


def device_transform(file):
    # Run subprocess.run and save output object
    output = subprocess.run(['python', '/Users/Shared/Workspace/Development/NikeBuild/python/cron-script/devices/nma/transform.py', '--filename', file])
    logger.info('############### Transformation Done')
    logger.info('Return code: %s', output.returncode)
    # use decode function to convert to string
   # print('Output:', output.stdout.decode("utf-8"))

def scan_directory(folder):

    files = os.listdir(folder)
    logger.info("File to be process: {0}".format(files))

    for f in files:
        device_transform(f)
        loader.load_file(f)



# main
def main(folder):

    # for now we are scanning the folder for a network, in future we will scan it recursively for each network folder
    scan_directory(folder);

if __name__ == '__main__':
   # logger.basicConfig(level=logging.INFO)
   # logger.info("Scan directoy")
   # for i in range(100000):
   #     logger.info("Print the value: %d", i)
    parser = ArgumentParser()
    parser.add_argument('-i', '--input', default='/Users/Shared/Workspace/Development/NikeBuild/python/cron-script/fileset/nma', help='Input path/to/file.csv', required=False)

    args = parser.parse_args()
    logger.info("Displaying Input Parameters as: %s", args.input)

    main(args.input)
    sys.exit(0)  #0 - success

