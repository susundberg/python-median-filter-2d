

import ctypes
from ctypes import c_int 

import numpy
import logging
import typing

LOG = logging.getLogger("median_filter")


class MedianFilterException(Exception):
    pass


class MedianFilter():
    def __init__(self, path: str):
        LOG.info("Load DLL '%s'", path)

        try:
            self.dll = ctypes.CDLL(path)
        except FileNotFoundError as e:
            raise MedianFilterException("Could not load DLL: " + str(e))

        self.filter_cpp: typing.Dict[typing.Any, typing.Any] = {}
        for dtype in [numpy.float32, numpy.float64, numpy.uint16]:
            self.filter_cpp[numpy.dtype(dtype)] = self._load_dll("median_filter_2d_" + dtype.__name__, dtype)

    def _load_dll(self, name: str, dtype) -> typing.Callable:
        fun = getattr(self.dll, name)


        data_ptr = numpy.ctypeslib.ndpointer( dtype=dtype, ndim=1, flags='C_CONTIGUOUS')

        fun.argtypes = [c_int, c_int, c_int, c_int, c_int, data_ptr, data_ptr]
        fun.restype = c_int

        def wrapped_fun(*pargs):
            types = ",".join([str(type(x)) for x in pargs])
            LOG.debug("Calling DLL fun '%s': %s", name, types)
            ret = fun(*pargs)
            LOG.debug("Calling DLL fun '%s' DONE: %s!", name, ret)
            if ret == 0:
                return
            raise MedianFilterException("Calling C++ filter failed ret: %d" % ret)
        return wrapped_fun

    def filter(self, window_x, window_y, input_array, block_size_hint=0):
        """ Filter with median filter. The window size is (window_z*2 + 1). """

        xsize = input_array.shape[1]
        ysize = input_array.shape[0]

        input_array = input_array.flatten()
        output_array = numpy.zeros(shape=input_array.shape, dtype=input_array.dtype)

        try:
            result_fun = self.filter_cpp[output_array.dtype]
        except KeyError:
            print(self.filter_cpp)
            import pdb; pdb.set_trace()
            raise MedianFilterException("Not supported for array type '%s'" % input_array.dtype)


        result_fun(xsize, ysize, window_x, window_y, block_size_hint, input_array, output_array)
        return output_array.reshape( ysize, xsize )
