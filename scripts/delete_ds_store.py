import os
import argparse


def delete_ds_store(path):
    for files in os.listdir(path):
        folder_in_path = path + files
        print(folder_in_path)
        for j in os.listdir(folder_in_path):
            if j.endswith('.DS_Store'):
                path_ = os.path.join(folder_in_path, j)
                print("Deleting: %s" % path_)

                if os.remove(path_):
                    print("Deleted!")
                else:
                    print("Unable to Delete...")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--directory_path',
        type=str,
        default='',
        help='Path where all directories reside'
    )
    args = parser.parse_args()
    delete_ds_store(args.path)
