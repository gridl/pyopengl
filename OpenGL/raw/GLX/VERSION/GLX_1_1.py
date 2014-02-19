'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GLX import _types as _cs
# End users want this...
from OpenGL.raw.GLX._types import *
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GLX_VERSION_GLX_1_1'
def _f( function ):
    return _p.createFunction( function,_p.GLX,'GLX_VERSION_GLX_1_1')
GLX_EXTENSIONS=_C('GLX_EXTENSIONS',0x3)
GLX_VENDOR=_C('GLX_VENDOR',0x1)
GLX_VERSION=_C('GLX_VERSION',0x2)
@_f
@_p.types(ctypes.c_char_p,ctypes.POINTER(_cs.Display),_cs.c_int)
def glXGetClientString(dpy,name):pass
@_f
@_p.types(ctypes.c_char_p,ctypes.POINTER(_cs.Display),_cs.c_int)
def glXQueryExtensionsString(dpy,screen):pass
@_f
@_p.types(ctypes.c_char_p,ctypes.POINTER(_cs.Display),_cs.c_int,_cs.c_int)
def glXQueryServerString(dpy,screen,name):pass