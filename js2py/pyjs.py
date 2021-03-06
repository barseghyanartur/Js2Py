from base import *
from constructors.jsmath import Math
from constructors.jsdate import Date
from constructors.jsobject import Object
from constructors.jsfunction import Function
from constructors.jsstring import String
from constructors.jsnumber import Number
from constructors.jsboolean import Boolean
from constructors.jsregexp import RegExp
from constructors.jsarray import Array
from host.console import console
from host.jseval import Eval
from host.jsfunctions import parseFloat, parseInt, isFinite, isNaN

# Now we have all the necessary items to create global environment for script
__all__ = ['Js', 'PyJsComma', 'PyJsStrictEq', 'PyJsStrictNeq',
           'PyJsException', 'PyJsBshift', 'Scope', 'PyExceptionToJs',
           'JsToPyException', 'JS_BUILTINS', 'appengine', 'set_global_object',
           'JsRegExp', 'PyJsException', 'PyExceptionToJs', 'JsToPyException', 'PyJsSwitchException']

# these were defined in base.py
builtins = ('true','false','null','undefined','Infinity',
            'NaN', 'console', 'String', 'Number', 'Boolean', 'RegExp',
            'Math', 'Date', 'Object', 'Function', 'Array',
            'parseFloat', 'parseInt', 'isFinite', 'isNaN')
            #Array, Function, JSON,   Error is done later :)
            # also some built in functions like eval...

def set_global_object(obj):
    PyJs.GlobalObject = obj
    # make this available
    obj.put('this', obj)
    # register this ( to make it not configurable)
    obj.register('this')



scope = dict(zip(builtins, [globals()[e] for e in builtins]))
# Now add errors:
for name, error in ERRORS.iteritems():
    scope[name] = error
#add eval
scope['eval'] = Eval
JS_BUILTINS = {k:v for k,v in scope.iteritems()}

