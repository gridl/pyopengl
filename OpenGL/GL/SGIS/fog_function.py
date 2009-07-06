'''OpenGL extension SGIS.fog_function

This module customises the behaviour of the 
OpenGL.raw.GL.SGIS.fog_function to provide a more 
Python-friendly API
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL.SGIS.fog_function import *
### END AUTOGENERATED SECTION