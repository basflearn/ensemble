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

def _add_argument_dir_with_file_type(parser, type, or_file=False):
    parser.add_argument(
        '%s_dir' % type,
        metavar='<%s_dir%s>' % (type, '_or_file' if or_file else ''),
        type=lambda x: ui.is_dir_with_file_type(x, type, or_file=or_file),
        help='path to %s directory%s' % (type, ' or file' if or_file else ''),
    )


parser = argparse.ArgumentParser(
    description='Computes mean field forces for a dataset, from a set of models.'
)
parser.add_argument(
    'dataset',
    metavar='<dataset>',
    type=lambda x: ui.is_file_type(x, 'dataset'),
    help='path to dataset file',
)
_add_argument_dir_with_file_type(parser, 'model', or_file=True)

args = parser.parse_args()
dataset_path, dataset = args.dataset


dataset = dict(dataset)
dataset['R'] = dataset['R'][1:25000, :, :]
dataset['F'] = dataset['F'][1:25000, :, :]
dataset['E'] = dataset['E'][1:25000]


R = dataset['R']
n_dataset = R.shape[0]

print(R.shape)

F_mean = np.zeros(R.shape)

model_dir, model_file_names = args.model_dir
n_models = len(model_file_names)

for i, model_file_name in enumerate(model_file_names):
    model_path = os.path.join(model_dir, model_file_name)
    print(model_path)

    model = np.load(model_path)

    gdml = GDMLPredict(model)
    _,F = gdml.predict(R.reshape(n_dataset,-1))

    F_mean += F.reshape(n_dataset,-1,3)

F_mean /= n_dataset

dataset = dict(dataset)
dataset['F'] = F_mean
dataset['theory'] = '{} {}'.format('mean_field_F ', dataset['theory'])
dataset['md5'] = io.dataset_md5(dataset)

np.savez_compressed('MEAN_'+dataset_path, **dataset)