#-----------------------------------------------------------------------------#
#   test_source.py                                                            #
#                                                                             #
#   Copyright © 2015-2019, Rajiv Bakulesh Shah, original author.              #
#   All rights reserved.                                                      #
#-----------------------------------------------------------------------------#
'Python source code tests.'



import itertools
import os
import sys
import unittest
import warnings

from isort import SortImports

from pottery import monkey
from tests.base import TestCase



monkey  # Workaround for Pyflakes.  :-(



class SourceTests(TestCase):
    def setUp(self):
        super().setUp()
        warnings.filterwarnings('ignore', category=DeprecationWarning)

    def tearDown(self):
        warnings.filterwarnings('default', category=DeprecationWarning)
        super().tearDown()

    @unittest.skipIf(
        sys.version_info[:2] == (3, 5),
        'isort is broken on Python 3.5 for no good reason ¯\\_(ツ)_/¯'
    )
    def test_imports(self):
        test_dir = os.path.dirname(__file__)
        test_files = (
            f for f in os.listdir(test_dir, absolute=True) if f.endswith('.py')
        )

        source_dir = os.path.dirname(test_dir)
        source_files = (
            f for f in os.listdir(source_dir, absolute=True)
            if f.endswith('.py')
        )

        for f in itertools.chain(source_files, test_files):
            with self.subTest(f=f):
                assert SortImports(f, check=True).correctly_sorted
