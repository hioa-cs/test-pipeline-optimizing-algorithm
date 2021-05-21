import sys
import support
import os.path
import random 
import argparse

def generate_dependencies(dataset):
    len = len(dataset)

def main(dataset_name):
    dataset = support.get_dataset(dataset_name)

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Algorithm for optimizing test sets')

    parser.add_argument("-f", type=str, dest='filename', description='The input file name of dataset')
    parser.add_argument('-tests', type=int, dest='tests',  default=[], description='An array specifying the number of tests x which should have a dependency y, can not exceed maximum number of tests available')
    parser.add_argument("-depend", type=int, dest='dependencies', default=[], description='For each test x in --tests, specifies the number of dependencies that should be created')

    args = parser.parse_args()

    if len(args.dependencies) != len(args.tests):
        print("The number of tests don't correspond with the number of added dependencies...")
        print("Tests {}, Dependencies {}".format(len(args.dependencies), len(args.tests)))
        print("Exiting script...")
        exit(0)
    if not os.path.isfile(args.filename):
        print ("File {} does not exist".format(args.filename))
        print("Exiting script...")
        exit(0)

    dependencies = list(map(lambda x, y:(x,y), args.dependencies, args.tests))
    main(dataset_name, dependencies)

