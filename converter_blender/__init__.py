# Authors: Alberto Jativa
# version ='1.0'
# ----------------------------------------------------------------------------------------------
""" 
Script that converts a CSV file to BVH and imports the animation
"""
# ----------------------------------------------------------------------------------------------
# Addon information
# ----------------------------------------------------------------------------------------------
bl_info = {
    "name": "Converter CSV to BVH",
    "author": "aljanue",
    "version": (1, 0),
    "blender": (3, 6, 0),
    "location": "View3D > Import > Converter",
    "description": "Convert a CSV File to BVH and import the animation",
    "category": "Converter",
}
# ----------------------------------------------------------------------------------------------
# Imports
# ----------------------------------------------------------------------------------------------
import bpy
import os
import sys
from bpy_extras.io_utils import ImportHelper

dir = os.path.dirname(os.path.realpath(__file__))
if not dir in sys.path:
    sys.path.append(dir)
    
import addon

# Class to create a panel for the CSV to BVH conversion
class CSVtoBVH_Panel(bpy.types.Panel):
    """
    Creates a panel for the CSV to BVH conversion
    """
    bl_label = "CSV to BVH"
    bl_idname = "OBJECT_PT_CSVtoBVH"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "CSV to BVH"

    def draw(self, context):
        layout = self.layout

        scene = context.scene
        
        row = layout.row()
        row.label(text="Load and convert a CSV file to BVH", icon='ZOOM_ALL')
        row = layout.row()
        row.operator("object.csvtobvh_operator")

# Operator class to convert the csv file to a bvh
class CSVtoBVH_Operator(bpy.types.Operator, ImportHelper):
    """
    Converts the csv file into a bvh file
    """
    bl_idname = "object.csvtobvh_operator"
    bl_label = "Load and convert!"

    filter_glob: bpy.props.StringProperty(default="*.csv", options={'HIDDEN'})
    
    def execute(self, context):
        csv_file_path = self.filepath
        bvh_file_path = os.path.splitext(csv_file_path)[0] + ".bvh"
        print(bvh_file_path)
        addon.convert_csv_to_bvh(csv_file_path, bvh_file_path)
        addon.open_bvh(bvh_file_path) 
        return{'FINISHED'}
    

# These functions must be declared at the end of the script.
def register():
    """
    Blender function that is used to register and enable all classes, custom properties,
    operators and panels.
    This function is called when the plugin is activated from Blender.
    """                                                                         
    bpy.utils.register_class(CSVtoBVH_Panel)
    
    bpy.utils.register_class(CSVtoBVH_Operator)



def unregister():
    """
    Blender function that is used to perform cleanup and unregister the classes
    and custom properties that were previously registered in the plugin through 
    the register() function. 
    This function is called when the plugin is deactivated or removed from Blender.
    """
    # Classes and operators are unregistered when the plugin is deactivated or removed
    
    bpy.utils.unregister_class(CSVtoBVH_Panel)
    bpy.utils.unregister_class(CSVtoBVH_Operator)


# This if loop prevents the register() command from being executed if the file is being run through an import from another program.
if __name__ == "__main__":
    register()