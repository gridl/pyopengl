'''OpenGL extension ANDROID.image_native_buffer

This module customises the behaviour of the 
OpenGL.raw.EGL.ANDROID.image_native_buffer to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/ANDROID/image_native_buffer.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.EGL import _types
from OpenGL.raw.EGL.ANDROID.image_native_buffer import *
from OpenGL.raw.EGL.ANDROID.image_native_buffer import _EXTENSION_NAME

def glInitImageNativeBufferANDROID():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

### END AUTOGENERATED SECTION