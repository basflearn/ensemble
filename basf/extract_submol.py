#!/usr/bin/python

# MIT License
#
# Copyright (c) 2018 Stefan Chmiela
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from __future__ import print_function

import argparse
import os
import sys

import numpy as np

from sgdml.train import GDMLTrain
from sgdml.predict import GDMLPredict
from sgdml.utils import io, ui


parser = argparse.ArgumentParser(
    description='Computes mean field forces for a dataset, from a set of models.'
)
parser.add_argument(
    'dataset',
    metavar='<dataset>',
    type=lambda x: ui.is_file_type(x, 'dataset'),
    help='path to dataset file',
)

args = parser.parse_args()
dataset_path, dataset = args.dataset

dataset = dict(dataset)


keep_idx = [0,1,2,3,4,5,66,67,68]


dataset['R'] = dataset['R'][:,keep_idx,:]
dataset['F'] = dataset['F'][:,keep_idx,:]
dataset['z'] = dataset['z'][keep_idx]

dataset['theory'] = '{} {}'.format('mean_field_F ', dataset['theory'])
dataset['md5'] = io.dataset_md5(dataset)

np.savez_compressed('MEAN_'+dataset_path, **dataset)