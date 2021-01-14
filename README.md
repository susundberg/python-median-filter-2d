# python-median-filter-2d
Python wrapping for 2D Median Filter (windowed)

Support float32, float64 and uint16 numpy arrays.

# General 

This work is based on https://github.com/suomela/mf2d

Alpha version, bugs are possible, use at your own risk.

# Implementation

From this repository comes the files ```src/filter.*``` that implement the 2d-median filter. I added uint16 variant, and since the filter does average on even cases it can produce +-1 results due rounding. 

For wrapping I added the ```filter_cwrap.*``` files provides convinient C-wrappings for tje actual python wrapper ```filter.py```. 

Please see ```test/test_filter.py``` for example usage.





