import glob
import os
import ntpath
import random
from shutil import copyfile, move
import argparse


def create_jpeg_file_list(image_path):
    """

    :param image_path: path where jpeg images reside
    :return: None
    """
    list_of_file = []
    for files in glob.glob(os.path.join(image_path, '*.jpeg')):
        list_of_file.append(files)
    return list_of_file


def check_path_exists(path):
    """

    :param path: train and test folder in destination path
    :return:
    """
    if not os.path.exists(path + '/train'):
        os.makedirs(path + '/train')
    if not os.path.exists(path + '/test'):
        os.makedirs(path + '/test')


def shuffle_divide(file_list):
    """

    :param file_list: list of all jpeg files
    :return: None
    """
    random.shuffle(file_list)
    test_data = file_list[-int(0.2 * len(file_list)):]
    train_data = file_list[:int(0.8 * len(file_list))]
    return test_data, train_data


def copy_data(data, list_of_files, str_value, destination_path):
    """

    :param data: train/test data
    :param list_of_files: list of all jpeg files
    :param str_value: 'test' or 'train
    :param destination_path: path where test/train folders needs to be saved
    :return: None
    """
    for i in range(len(data)):
        head, tail = ntpath.split(list_of_files[i])
        copyfile(list_of_files[i], (destination_path + '/' + str_value + '/' + tail))
        copyfile(list_of_files[i].replace('jpeg', 'xml'), (destination_path + '/test/' + tail.replace('jpeg', 'xml')))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--images_path',
        type=str,
        default='',
        help='Path to folders inside which jpg, jpeg files reside'
    )
    parser.add_argument(
        '--destination_path',
        type=str,
        default='',
        help='Path to folders where test and train should reside'
    )
    args = parser.parse_args()
    list_of_file = create_jpeg_file_list(args.images_path)
    check_path_exists(args.destination_path)
    train_data, test_data = shuffle_divide(list_of_file)
    print('Folder creation done')
    copy_data(train_data, list_of_file, 'train', args.destination_path)
    print('Created train data')
    copy_data(test_data, list_of_file, 'test', args.destination_path)
    print('Created test data')
