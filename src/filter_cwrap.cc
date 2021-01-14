#pragma once
#include <stdint.h>
#include <stdexcept>
#include "filter_cwrap.h"

#include "filter.h"


template<typename T>
int median_filter_with_catch(int x, int y, int hx, int hy, int blockhint, const T* in, T* out)
{
   try
   {
      median_filter_2d<T>(x,y,hx,hy,blockhint,in,out );
   } catch (std::invalid_argument& e)
   {
      return 1;
   }
   return 0;
}

int median_filter_2d_float64(int x, int y, int hx, int hy, int blockhint, const double* in, double* out)
{
   return median_filter_with_catch<double>( x, y, hx, hy, blockhint, in, out );
}

int median_filter_2d_float32(int x, int y, int hx, int hy, int blockhint, const float* in, float* out)
{
   return median_filter_with_catch<float>( x, y, hx, hy, blockhint, in, out );
}

int median_filter_2d_uint16(int x, int y, int hx, int hy, int blockhint, const uint16_t* in, uint16_t* out)
{
   return median_filter_with_catch<uint16_t>( x, y, hx, hy, blockhint, in, out );
}

