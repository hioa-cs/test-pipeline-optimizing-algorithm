import sys
import support
import os.path


def main(dataset_name):
    dataset = support.get_dataset(dataset_name)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("No dataset added as an argument")
        print("Exiting script...")
        exit(0)

    dataset_name = sys.argv[1]

    if not os.path.isfile(dataset_name):
        print ("File {} does not exist".format(dataset_name))
        print("Exiting script...")
        exit(0)

    main(dataset_name)

