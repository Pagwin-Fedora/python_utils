from inspect import Parameter, Signature
from functools import partial, wraps
import sys
## A function that's used by the base_init_util class to handle binding an accurate function signature to __init__
#def _init_util_init_param_bind(init_func=None,*,fields=[]):
    #handles the case where the wrapper is getting it's fields argument before it does work to the __init__ function of  base_init_util
    #print(init_func)
#    print(fields)
#    if init_func is None:
#        return partial(_init_util_init_param_bind,fields=fields)
#    sig = Signature([Parameter(name,
#                Parameter.POSITIONAL_OR_KEYWORD)
#                for name in fields])
#    @wraps(init_func)
#    def wrapper(*args, **kwargs):
        #print(*args)
        #note if args need to be pulled out as part of some future functionality of this function just capture the returned value from sig.bind(*args, **kwargs)
#        print(sig,"asdfasdfasdfasdf------------")
#        print(*args)
#        sig.bind(*args,**kwargs)
#        return init_func(*args,**kwargs)
#    return wrapper
##a class decorator that can be used to have a class instantiated via fields provided through ither the __init__ function or a _fields attribute
def easy_init(cls):
    if hasattr(cls, '__init__') and type(cls.__init__).__name__ == 'function' and callable(cls.__init__):
        sig = Signature.from_callable(cls.__init__)
        sig = sig.replace(parameters=list(map(lambda val:val[1],filter(lambda val:val[0]!='self',sig.parameters.items()))))
        init_func = cls.__init__
    elif hasattr(cls,'_fields') and type(cls._fields) is list:
        sig = Signature([Parameter(name,
            Parameter.POSITIONAL_OR_KEYWORD)
            for name in cls._fields])
        init_func = lambda self,/,*args, **kwargs: None
        #print(sig)
    def new_init(self,*args,**kwargs):
        #print(self,file=sys.stderr)
        #print(*args,'\n',**kwargs)
        print(sig)
        bound = sig.bind(*args, **kwargs)
        for  name,val in bound.arguments.items():
            print(name)
            setattr(self,name,val)
        return init_func(self,*args,**kwargs)
    new_init.__signature__ = sig
    setattr(cls, '__init__',new_init)
    return cls
## A class that can be inherited from to avoid repitition in making __init__ functions for classes
#class base_init_util:
#    _fields = ['asdf']
#    @_init_util_init_param_bind(fields=_fields)
#    def __init__(*args, **kwargs):
#        print('test run')
#        for name,val in zip(self.__class__.fields, args):
#            setattr(self,name,val)
