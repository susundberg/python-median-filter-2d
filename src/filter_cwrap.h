#pragma once
#include <stdint.h>

extern "C" 
{
   int median_filter_2d_float64(int x, int y, int hx, int hy, int blockhint, const double* in, double* out);
   int median_filter_2d_float32(int x, int y, int hx, int hy, int blockhint, const float* in, float* out);
   int median_filter_2d_uint16(int x, int y, int hx, int hy, int blockhint, const uint16_t* in, uint16_t* out);
}

