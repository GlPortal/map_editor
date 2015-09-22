import bpy
import os
import string
import re

from .mapHelpers import *

class fixMap(bpy.types.Operator):
    bl_idname = "wm.fix_map"
    bl_label = "Fix map"
    bl_description = "Fix the map before exporting."
    bl_options = {"UNDO"}
    
    def execute(self, context):
        bpy.ops.object.select_all(action='SELECT')
        bpy.ops.object.transform_apply(rotation=True)
        bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
        bpy.ops.object.select_all(action='DESELECT')
        
        return {'FINISHED'}

class checkMap(bpy.types.Operator):
    bl_idname = "wm.check_map"
    bl_label = "Check map"
    bl_description = "Check the map for problems."
    
    def execute(self, context):
        bpy.ops.object.map_check_dialog('INVOKE_DEFAULT')
        
        return {'FINISHED'}