# file: load_rap_attributes_data_mat.py
# brief: To use the mat data under python.
# author: CRIPAC
# version: 1.0
import sys
import numpy as np
sys.path.append('../util')
from file_operation import *

def loadRAPReID(data_filename):
    """
    load mat file under python.
    Note: It's not a general function, but based on the structure of 
    the variable in mat file.

    Input:
        data_filename - the mat file
    Return:
        Rap reid data in a dictionary whose key is the same with
        that in mat file.
    """

    data = loadMat(data_filename)
    char_existed = data_filename.find('/')
    if char_existed == -1:
        root_key = data_filename.split('.')[0]
    else:
        filename = data_filename.split('/')[-1]
        root_key = filename.split('.')[0]
    # Identities of training samples.
    training_samples_id = data[root_key][0][0][0]
    # Image filename of training samples (to get each item of the filename like
    # this: training_samples_filename[0][0][0], <type 'numpy.unicode'>).
    training_samples_filename = data[root_key][0][0][2]
    image_filenames_train = [ item[0][0] for item in training_samples_filename ]
    image_filenames_train = np.asarray(image_filenames_train)
    # Image filename of test samples.
    test_samples_filename = data[root_key][0][0][3]
    image_filenames_test = [ item[0][0] for item in test_samples_filename ]
    image_filenames_test = np.asarray(image_filenames_test)

    dataset = {'person_identities_train': training_samples_id, \
        'image_filenames_train': image_filenames_train, \
        'image_filenames_test': image_filenames_test}
    return dataset


if __name__=='__main__':

    filename = '/data1/da.li/projects/LSPR/data/ReID/RAP_reid_data.mat'
    data = loadRAPReID(filename)
    print data
