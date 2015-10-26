#!/usr/bin/env python

import argparse

from canari.mode import set_canari_mode, CanariMode
from canari.utils.fs import pushd
from common import canari_main, ParseFieldsAction, project_package_dir
from canari.maltego.runner import local_transform_runner, console_writer
from framework import SubCommand, Argument
from canari.config import load_config


__author__ = 'Nadeem Douba'
__copyright__ = 'Copyright 2012, Canari Project'
__credits__ = []

__license__ = 'GPLv3'
__version__ = '0.7'
__maintainer__ = 'Nadeem Douba'
__email__ = 'ndouba@gmail.com'
__status__ = 'Development'


@SubCommand(
    canari_main,
    help='Runs Canari local transforms in a terminal-friendly fashion.',
    description='Runs Canari local transforms in a terminal-friendly fashion.'
)
@Argument(
    'transform',
    metavar='<transform>',
    help='The name of the transform you wish to run (e.g. sploitego.transforms.nmapfastscan).'
)
@Argument(
    'params',
    metavar='[param1 ... paramN]',
    help='Any extra parameters that can be sent to the local transform.',
    nargs=argparse.ZERO_OR_MORE
)
@Argument(
    'value',
    metavar='<value>',
    help='The value of the input entity being passed into the local transform.'
)
@Argument(
    'fields',
    metavar='[field1=value1...#fieldN=valueN]',
    help='The fields of the input entity being passed into the local transform.',
    default={},
    action=ParseFieldsAction,
    nargs=argparse.OPTIONAL
)  # This parameter will never be consumed because we use a special parser for this transform.
def debug_transform(opts):
    set_canari_mode(CanariMode.LocalDebug)
    with pushd(project_package_dir()):
        local_transform_runner(opts.transform, opts.value, opts.fields, opts.params, load_config(), console_writer)