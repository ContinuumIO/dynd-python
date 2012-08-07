//
// Copyright (C) 2011-12, Dynamic NDArray Developers
// BSD 2-Clause License, see LICENSE.txt
//

#ifndef _DND__ELWISE_REDUCE_GFUNC_FUNCTIONS_HPP_
#define _DND__ELWISE_REDUCE_GFUNC_FUNCTIONS_HPP_

#include <Python.h>

#include <stdint.h>
#include <sstream>
#include <deque>
#include <vector>

#include <dnd/dtype.hpp>
#include <dnd/ndarray.hpp>
#include <dnd/kernels/kernel_instance.hpp>
#include <dnd/codegen/codegen_cache.hpp>
#include <dnd/gfunc/elwise_reduce_gfunc.hpp>

namespace pydnd {

void elwise_reduce_gfunc_add_kernel(dnd::gfunc::elwise_reduce& gf, dnd::codegen_cache& cgcache, PyObject *kernel,
                            bool associative, bool commutative, const dnd::ndarray& identity);

PyObject *elwise_reduce_gfunc_call(dnd::gfunc::elwise_reduce& gf, PyObject *args, PyObject *kwargs);

inline std::string elwise_reduce_gfunc_debug_dump(dnd::gfunc::elwise_reduce& gf)
{
    std::stringstream ss;
    gf.debug_dump(ss);
    return ss.str();
}

struct elwise_reduce_gfunc_placement_wrapper {
    intptr_t dummy[(sizeof(dnd::gfunc::elwise_reduce) + sizeof(intptr_t) - 1)/sizeof(intptr_t)];
};

inline void elwise_reduce_gfunc_placement_new(elwise_reduce_gfunc_placement_wrapper& v, const char *name)
{
    // Call placement new
    new (&v) dnd::gfunc::elwise_reduce(name);
}

inline void elwise_reduce_gfunc_placement_delete(elwise_reduce_gfunc_placement_wrapper& v)
{
    // Call the destructor
    ((dnd::gfunc::elwise_reduce *)(&v))->~elwise_reduce();
}

// placement cast
inline dnd::gfunc::elwise_reduce& GET(elwise_reduce_gfunc_placement_wrapper& v)
{
    return *(dnd::gfunc::elwise_reduce *)&v;
}

} // namespace pydnd

#endif // _DND__ELWISE_REDUCE_GFUNC_FUNCTIONS_HPP_
