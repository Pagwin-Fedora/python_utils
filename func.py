import functools
from inspect import Parameter, Signature
## returns a new function that's a composite of the outer and inner functions where the inner function can only have 1 argument, if further functions are provided as args they are composited within the composite of outer and inner
def composite(outer,inner,*args):
    comp = None
    if callable(outer) and callable(inner):
        def temp(*args, **kwargs):
            return outer(inner(*args,**kwargs))
        comp = temp
    else:
        raise TypeError("the outer and inner functions you provide have to be callable")
    comp.__signature__ = Signature.from_callable(inner).replace(return_annotation=Signature.from_callable(outer).return_annotation)
    if len(args)!=0:
        if all(callable, args):
            return composite(comp,args[0],*args)
        else:
            raise TypeError("all functions provided need to be callable in order to be composited")
    return comp
##returns a new function that's a composite of the outer and inner functions where you can specify outer arguments as you build the composite function
def composite_outer_arguments(outer,inner,*args,**kwargs):
    if callable(outer) and callable(inner):
        def comp(*iargs,**ikwargs):
            return outer(inner(*iargs,**ikwargs),*args,**ikwargs)

    comp.__signature__ = Signature.from_callable(inner).replace(return_annotation=Signature.from_callable(outer).return_annotation)
    return comp
    else:
        raise TypeError("the outer and inner functions you provide have to be callable")
## returns an nth order partial where n is the number of functions provided beforehand where each call of the partial allows a user to provide all arguments past the first argument for each function(probably doesn't work don't use without testing)
def composite_partial(*funcs):
    if all(callable,funcs):
        def part(*oargs,**okwargs)
            def comp(*args, **kwargs):
                funcs[0](funcs[1](*args,**kwargs),*oargs,**okwargs)
        return __composite_partial__(part,funcs[2:])
    else:
        yield TypeError("All functions need to be callable")
def __composite_partial__(part,funcs):
    def npart(*oargs,**okwargs):
        f = part(*oargs,**okwargs)
        def comp(*args, **kwargs):
            return f(funcs[0](*args,**kwargs))
    return __composite_partial__(part,funcs[1:])
