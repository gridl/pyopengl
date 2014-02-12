'''OpenGL extension INTEL.fragment_shader_ordering

This module customises the behaviour of the 
OpenGL.raw.GL.INTEL.fragment_shader_ordering to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/INTEL/fragment_shader_ordering.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL import _types
from OpenGL.raw.GL.INTEL.fragment_shader_ordering import *
from OpenGL.raw.GL.INTEL.fragment_shader_ordering import _EXTENSION_NAME

def glInitFragmentShaderOrderingINTEL():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

### END AUTOGENERATED SECTION