import unittest
from unittest.mock import mock_open, patch
from contextlib import contextmanager
from io import StringIO
import solution


class NotMocked(Exception):
    def __init__(self, filename):
        super(NotMocked, self).__init__(
            "The file %s was opened, but not mocked." % filename)
        self.filename = filename


@contextmanager
def mock_open(filename, contents=None, complain=True):
    """Mock the open() builtin function on a specific filename
.
    Let execution pass through to open() on files different than
    :filename:. Return a StringIO with :contents: if the file was
    matched. If the :contents: parameter is not given or if it is None,
    a StringIO instance simulating an empty file is returned.
.
    If :complain: is True (default), will raise an AssertionError if
    :filename: was not opened in the enclosed block. A NotMocked
    exception will be raised if open() was called with a file that was
    not mocked by mock_open.

    Source: https://mapleoin.github.io/perma/mocking-python-file-open
    """
    open_files = set()

    def mock_file(*args):
        if args[0] == filename:
            f = StringIO(contents)
            f.name = filename
        else:
            mocked_file.stop()
            f = open(*args)
            mocked_file.start()
        open_files.add(f.name)
        return f

    mocked_file = patch('builtins.open', mock_file)
    mocked_file.start()
    try:
        yield
    except NotMocked as e:
        if e.filename != filename:
            raise
    mocked_file.stop()
    try:
        open_files.remove(filename)
    except KeyError:
        if complain:
            raise AssertionError("The file %s was not opened." % filename)
    for f_name in open_files:
        if complain:
            raise NotMocked(f_name)


class Test(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(Test, self).__init__(*args, **kwargs)
        self.nr = ""

    def setUp(self):
        self.solution = solution.Solution(self.nr)

    def tearDown(self):
        print(self._testMethodName+":")
        print(self.solution)
        print("")

    def set_param(self, key, value):
        self.solution.set_param(key, value)

    def execute_test(self, test_input):
        with mock_open('/input.txt', test_input, False):
            self.solution.calculate(True)

    def get_solution(self, nr):
        return self.solution.get_solution(nr)
