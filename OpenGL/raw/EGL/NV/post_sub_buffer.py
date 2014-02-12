'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.EGL import _types as _cs
# End users want this...
from OpenGL.raw.EGL._types import *
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'EGL_NV_post_sub_buffer'
def _f( function ):
    return _p.createFunction( function,_p.EGL,'EGL_NV_post_sub_buffer')
EGL_POST_SUB_BUFFER_SUPPORTED_NV=_C('EGL_POST_SUB_BUFFER_SUPPORTED_NV',0x30BE)
@_f
@_p.types(_cs.EGLBoolean,_cs.EGLDisplay,_cs.EGLSurface,_cs.EGLint,_cs.EGLint,_cs.EGLint,_cs.EGLint)
def eglPostSubBufferNV(dpy,surface,x,y,width,height):pass