import unittest
import subprocess
import numpy
import logging
from src.filter import MedianFilter


INPUT_DATA = [4, 4, 4, 4, 4, 4, 4, 4, 4,
              0, 4, 0, 0, 2, 0, 0, 0, 4,
              0, 0, 0, 0, 2, 0, 0, 0, 4,
              0, 9, 0, 0, 2, 2, 2, 4, 4]

ASSUMED_RES = [4, 4, 4, 3, 3, 3, 2, 4, 4,
               2, 0, 0, 2, 2, 2, 0, 4, 4,
               0, 0, 0, 0, 0, 2, 0, 2, 4,
               0, 0, 0, 0, 1, 2, 1, 3, 4]


INPUT_DATA = numpy.array(INPUT_DATA, dtype=numpy.uint16).reshape(4, 9)
ASSUMED_RES = numpy.array(ASSUMED_RES, dtype=numpy.uint16).reshape(4, 9)
print(INPUT_DATA)


class Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        subprocess.run(("make", "build/filter.so"), check=True)

    def setUp(self):
        self.median = MedianFilter("./build/filter.so")

    def run_filter(self, dtype):
        res = self.median.filter(1, 1, numpy.array(INPUT_DATA, dtype=dtype))
        print(res)
        error = numpy.max( numpy.abs( numpy.array( res, dtype=numpy.uint16 ) - ASSUMED_RES ))
        self.assertEqual( error, 0 )

    def test_0_filter_uint16(self):
        self.run_filter(numpy.uint16)

    def test_1_filter_float32(self):
        self.run_filter(numpy.float32)

    def test_1_filter_float64(self):
        self.run_filter(numpy.float64)

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    unittest.main()
