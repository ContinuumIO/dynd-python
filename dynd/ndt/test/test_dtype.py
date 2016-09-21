import sys
import ctypes
import unittest
from dynd import ndt

class TestType(unittest.TestCase):
    def test_tuple(self):
        tp = ndt.tuple(ndt.int32, ndt.float64)

    def test_struct(self):
        tp = ndt.struct(x = ndt.int32, y = ndt.float64)

class TestTypeFor(unittest.TestCase):
    def test_bool(self):
        self.assertEqual(ndt.bool, ndt.type_for(True))
        self.assertEqual(ndt.bool, ndt.type_for(False))

    def test_int(self):
        self.assertEqual(ndt.int32, ndt.type_for(0))
        self.assertEqual(ndt.int32, ndt.type_for(1))
        self.assertEqual(ndt.int32, ndt.type_for(7))

    def test_float(self):
        pass

class TestDType(unittest.TestCase):
    def test_bool_type_properties(self):
        self.assertEqual(type(ndt.bool), ndt.type)
        self.assertEqual(str(ndt.bool), 'bool')
        self.assertEqual(ndt.bool.data_size, 1)
        self.assertEqual(ndt.bool.data_alignment, 1)

    def test_int_type_properties(self):
        self.assertEqual(type(ndt.int8), ndt.type)
        self.assertEqual(str(ndt.int8), 'int8')
        self.assertEqual(ndt.int8.data_size, 1)
        self.assertEqual(ndt.int8.data_alignment, 1)

        self.assertEqual(type(ndt.int16), ndt.type)
        self.assertEqual(str(ndt.int16), 'int16')
        self.assertEqual(ndt.int16.data_size, 2)
        self.assertEqual(ndt.int16.data_alignment, 2)

        self.assertEqual(type(ndt.int32), ndt.type)
        self.assertEqual(str(ndt.int32), 'int32')
        self.assertEqual(ndt.int32.data_size, 4)
        self.assertEqual(ndt.int32.data_alignment, 4)

        self.assertEqual(type(ndt.int64), ndt.type)
        self.assertEqual(str(ndt.int64), 'int64')
        self.assertEqual(ndt.int64.data_size, 8)
        self.assertTrue(ndt.int64.data_alignment in [4,8])

        self.assertEqual(type(ndt.intptr), ndt.type)
        if ctypes.sizeof(ctypes.c_void_p) == 4:
            self.assertEqual(str(ndt.intptr), 'int32')
            self.assertEqual(ndt.intptr.data_size, 4)
            self.assertEqual(ndt.intptr.data_alignment, 4)
        else:
            self.assertEqual(str(ndt.intptr), 'int64')
            self.assertEqual(ndt.intptr.data_size, 8)
            self.assertEqual(ndt.intptr.data_alignment, 8)

    def test_uint_type_properties(self):
        self.assertEqual(type(ndt.uint8), ndt.type)
        self.assertEqual(str(ndt.uint8), 'uint8')
        self.assertEqual(ndt.uint8.data_size, 1)
        self.assertEqual(ndt.uint8.data_alignment, 1)

        self.assertEqual(type(ndt.uint16), ndt.type)
        self.assertEqual(str(ndt.uint16), 'uint16')
        self.assertEqual(ndt.uint16.data_size, 2)
        self.assertEqual(ndt.uint16.data_alignment, 2)

        self.assertEqual(type(ndt.uint32), ndt.type)
        self.assertEqual(str(ndt.uint32), 'uint32')
        self.assertEqual(ndt.uint32.data_size, 4)
        self.assertEqual(ndt.uint32.data_alignment, 4)

        self.assertEqual(type(ndt.uint64), ndt.type)
        self.assertEqual(str(ndt.uint64), 'uint64')
        self.assertEqual(ndt.uint64.data_size, 8)
        self.assertTrue(ndt.uint64.data_alignment in [4,8])

        self.assertEqual(type(ndt.uintptr), ndt.type)
        if ctypes.sizeof(ctypes.c_void_p) == 4:
            self.assertEqual(str(ndt.uintptr), 'uint32')
            self.assertEqual(ndt.uintptr.data_size, 4)
            self.assertEqual(ndt.uintptr.data_alignment, 4)
        else:
            self.assertEqual(str(ndt.uintptr), 'uint64')
            self.assertEqual(ndt.uintptr.data_size, 8)
            self.assertEqual(ndt.uintptr.data_alignment, 8)

    def test_float_type_properties(self):
        self.assertEqual(type(ndt.float32), ndt.type)
        self.assertEqual(str(ndt.float32), 'float32')
        self.assertEqual(ndt.float32.data_size, 4)
        self.assertEqual(ndt.float32.data_alignment, 4)

        self.assertEqual(type(ndt.float64), ndt.type)
        self.assertEqual(str(ndt.float64), 'float64')
        self.assertEqual(ndt.float64.data_size, 8)
        self.assertTrue(ndt.float64.data_alignment in [4,8])

    def test_complex_type_properties(self):
        self.assertEqual(type(ndt.complex_float32), ndt.type)
        self.assertEqual(str(ndt.complex_float32), 'complex[float32]')
        self.assertEqual(ndt.complex_float32.data_size, 8)
        self.assertEqual(ndt.complex_float32.data_alignment, 4)

        self.assertEqual(type(ndt.complex_float64), ndt.type)
        self.assertEqual(str(ndt.complex_float64), 'complex[float64]')
        self.assertEqual(ndt.complex_float64.data_size, 16)
        self.assertTrue(ndt.complex_float64.data_alignment in [4,8])


    def test_fixed_string_type_properties(self):
        d = ndt.make_fixed_string(10, 'ascii')
        self.assertEqual(str(d), "fixed_string[10, 'ascii']")
        self.assertEqual(d.data_size, 10)
        self.assertEqual(d.data_alignment, 1)
#        self.assertEqual(d.encoding, 'ascii')

        d = ndt.make_fixed_string(10, 'ucs2')
        self.assertEqual(str(d), "fixed_string[10, 'ucs2']")
        self.assertEqual(d.data_size, 20)
        self.assertEqual(d.data_alignment, 2)
 #       self.assertEqual(d.encoding, 'ucs2')

        d = ndt.make_fixed_string(10, 'utf8')
        self.assertEqual(str(d), 'fixed_string[10]')
        self.assertEqual(d.data_size, 10)
        self.assertEqual(d.data_alignment, 1)
#        self.assertEqual(d.encoding, 'utf8')

        d = ndt.make_fixed_string(10, 'utf16')
        self.assertEqual(str(d), "fixed_string[10, 'utf16']")
        self.assertEqual(d.data_size, 20)
        self.assertEqual(d.data_alignment, 2)
 #       self.assertEqual(d.encoding, 'utf16')

        d = ndt.make_fixed_string(10, 'utf32')
        self.assertEqual(str(d), "fixed_string[10, 'utf32']")
        self.assertEqual(d.data_size, 40)
        self.assertEqual(d.data_alignment, 4)
  #      self.assertEqual(d.encoding, 'utf32')

    def test_scalar_types(self):
        self.assertEqual(ndt.bool, ndt.type(bool))
        self.assertEqual(ndt.int32, ndt.type(int))
        self.assertEqual(ndt.float64, ndt.type(float))
        self.assertEqual(ndt.complex_float64, ndt.type(complex))
        self.assertEqual(ndt.string, ndt.type(str))
        self.assertEqual(ndt.bytes, ndt.type(bytearray))
        if sys.version_info[0] == 2:
            self.assertEqual(ndt.string, ndt.type(unicode))
        if sys.version_info[0] >= 3:
            self.assertEqual(ndt.bytes, ndt.type(bytes))

    def test_fixed_bytes_type(self):
        d = ndt.make_fixed_bytes(4, 4)
        self.assertEqual(str(d), 'fixed_bytes[4, align=4]')
        self.assertEqual(d.data_size, 4)
        self.assertEqual(d.data_alignment, 4)

        d = ndt.make_fixed_bytes(9, 1)
        self.assertEqual(str(d), 'fixed_bytes[9]')
        self.assertEqual(d.data_size, 9)
        self.assertEqual(d.data_alignment, 1)

        # Alignment must not be greater than data_size
        self.assertRaises(RuntimeError, ndt.make_fixed_bytes, 1, 2)
        # Alignment must be a power of 2
        self.assertRaises(RuntimeError, ndt.make_fixed_bytes, 6, 3)
        # Alignment must divide into the data_size
        self.assertRaises(RuntimeError, ndt.make_fixed_bytes, 6, 4)

    def test_cstruct_type(self):
        self.assertFalse(ndt.type('{x: int32}') == ndt.type('{y: int32}'))

    def test_struct_type(self):
        tp = ndt.make_struct([ndt.int32, ndt.int64], ['x', 'y'])
        self.assertTrue(tp.field_types, [ndt.int32, ndt.int64])
        self.assertTrue(tp.field_names, ['x', 'y'])
        self.assertEqual(tp.arrmeta_size, 2 * ctypes.sizeof(ctypes.c_void_p))
        self.assertTrue(tp.data_size is None)

    def test_tuple_type(self):
        tp = ndt.type('(int32, int64)')
        self.assertTrue(tp.field_types, [ndt.int32, ndt.int64])
        self.assertEqual(tp.arrmeta_size, 2 * ctypes.sizeof(ctypes.c_void_p))
        self.assertTrue(tp.data_size is None)

    def test_type_shape(self):
        # The shape attribute of ndt.type
        tp = ndt.type('3 * 4 * int32')
        self.assertEqual(tp.shape, (3, 4))
        tp = ndt.type('Fixed * 3 * var * int32')
        self.assertEqual(tp.shape, (-1, 3, -1))
        tp = ndt.type('var * 3 * 2 * int32')
        self.assertEqual(tp.shape, (-1, 3, 2))

if __name__ == '__main__':
    unittest.main(verbosity=2)
