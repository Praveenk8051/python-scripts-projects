import cv2
from tensorflow.python.platform import gfile
import ntpath
import os
import argparse


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

def read_image(image_path):
    """Gets and prints the spreadsheet's header columns

    Args:
        image_path (str): image file path
    Returns:
        numpy array: pixel values
    """
    return cv2.imread(image_path, cv2.IMREAD_UNCHANGED)


def write_image(image, path):
    """Gets and prints the spreadsheet's header columns

    Args:
        image : numpy array, pixel values
        path : path where image should be written
    Returns:
        None
    """
    cv2.imwrite(path, image)


def resize_images(file_list, save_path):
    """Resize the images
    Args:
        path: list of files 
   save_path: path where files should be saved 
    Returns:
        None
    """
    for i in range(len(file_list)):
        img = read_image(file_list[i])

        resized_img = cv2.resize(img, (600, 600))
        _, tail = ntpath.split(file_list[i])
        new_path = save_path + '/' + tail
        
        write_image(new_path, resized_img)


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
    args = parser.parse_args()
    file_list = create_file_list(args.pick_files_path)
    resize_images(file_list, args.save_files_path)