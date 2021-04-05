import ntpath
import os
import argparse
from tensorflow.python.platform import gfile


def create_file_list(path):
    """Create list of file paths
    Args:
        path: folder containing image files
    Returns:
        list: list of image file paths
    """
    file_list = []
    extensions = ['jpg', 'jpeg', 'JPG', 'JPEG', 'png']
    for extension in extensions:
        file_glob = os.path.join(path, '*.' + extension)
        file_list.extend(gfile.Glob(file_glob))
    return file_list


def rename_files(file_list, save_path, file_name):
    """rename the files
    Args:
        file_list: list of image file paths
        save_path: path where renamed files to be saved
        file_name: the names of the file
    Returns:
        None
    """
    count = 0
    for i in range(len(file_list)):
        print(file_list[i])
        _, tail = ntpath.split(file_list[i])
        _, b = tail.split(".")
        trackName = file_name+str(count)
        os.rename(file_list[i], os.path.join(save_path, trackName + "." + b))
        count = count + 1


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--pick_files_path',
        type=str,
        default='',
        help='Path where files to be renamed reside'
    )
    parser.add_argument(
        '--save_files_path',
        type=str,
        default='',
        help='Path where files are to be saved'
    )
    parser.add_argument(
        '--name_of_the_file',
        type=str,
        default='',
        help='custom name to be given'
    )
    args = parser.parse_args()
    file_list = create_file_list(args.pick_files_path)
    print(file_list)
    rename_files(file_list, args.save_files_path, args.name_of_the_file)
