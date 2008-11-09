'''OpenGL extension SGIX.impact_pixel_texture

This module customises the behaviour of the 
OpenGL.raw.GL.SGIX.impact_pixel_texture to provide a more 
Python-friendly API
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL.SGIX.impact_pixel_texture import *
### END AUTOGENERATED SECTION