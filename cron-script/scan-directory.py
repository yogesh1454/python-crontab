import os
import sys
import subprocess
from devices import loader
from argparse import ArgumentParser
import logging.config
import yaml

# Property based logging
# logging.config.fileConfig(fname='logger.conf', disable_existing_loggers=False)

# Get Configuration
with open('scan-conf.yaml', 'r') as cf:
    scan_config = yaml.safe_load(cf.read())
    logging.info("Scan Folder Properties: {0}".format(scan_config))

# yaml file based logging
with open(scan_config.get('scan').get('logConfig'), 'r') as f:
    logging_config = yaml.safe_load(f.read())
    logging.config.dictConfig(logging_config)

# Get the logger specified in the file
logger = logging.getLogger(__name__)


def device_transform(srcFile, targetFile):
    # Run subprocess.run and save output object
    output = subprocess.run(['python', '/Users/Shared/Workspace/Development/NikeBuild/python/cron-script/devices/nma/transform.py', '--src', srcFile, '--target', targetFile])
    logger.info('############### Transformation Done')
    logger.info('Return code: %s', output.returncode)
    # use decode function to convert to string
   # print('Output:', output.stdout.decode("utf-8"))

def scan_directory(folder):

    files = os.listdir(folder)
    logger.info("File to be process: {0}".format(files))

    for f in files:
        device_transform(f, outputFileName(f))
        loader.load_file(f)


def outputFileName(inputFile):
    file_tuple = os.path.splitext(inputFile)
    logger.info("File Tuple Parts: {0}".format(file_tuple))
    return file_tuple[0] + '.yaml'

# main
def main(folder):

    # for now we are scanning the folder for a network, in future we will scan it recursively for each network folder
    scan_directory(folder);

if __name__ == '__main__':

    parser = ArgumentParser()
    parser.add_argument('-i', '--input', help='Input path/to/file.csv', required=False)

    args = parser.parse_args()
    logger.info("Displaying Input Parameters as: %s", args.input)

    if(args.input == None):
        args.input = scan_config.get('scan').get('basePath')
    main(args.input)
    sys.exit(0)  #0 - success

