__all__ = ['void', 'bool', 'int8', 'int16', 'int32', 'int64',
            'uint8', 'uint16', 'uint32', 'uint64',
            'float32', 'float64', 'cfloat32', 'cfloat64',
            'complex_float32', 'complex_float64',
            'complex64', 'complex128']

from _pydnd import w_dtype as dtype

void = dtype('void')
bool = dtype('bool')
int8 = dtype('int8')
int16 = dtype('int16')
int32 = dtype('int32')
int64 = dtype('int64')
uint8 = dtype('uint8')
uint16 = dtype('uint16')
uint32 = dtype('uint32')
uint64 = dtype('uint64')
float32 = dtype('float32')
float64 = dtype('float64')
complex_float32 = dtype('complex<float32>')
complex_float64 = dtype('complex<float64>')
cfloat32 = complex_float32
cfloat64 = complex_float64
# Aliases for people comfortable with the Numpy complex namings
complex64 = cfloat32
complex128 = cfloat64
