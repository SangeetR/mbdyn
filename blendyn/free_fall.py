bl_info = {
    "name": "Free-Fall Add-on",
    "author": "Sangeet Rathi",
    "version": (3, 0),
    "blender": (2, 92, 0),
    "category": "Physics",
    "description": "A blender add on to show free fall using mbdyn",
    "install_requires":"pandas"
}

import bpy
import pandas as pd
# import pandas as pd

"""

    For free fall we only need one output file 
    "free_falling_body.mov"

"""

mbdynOutputPath = "C:\\Users\\DELL\\Desktop\\sync\\free_falling_body.mov" # Change this path to your output file  

class GSOC_OT_free_fall(bpy.types.Operator):
    """A free fall body in blender using mbdyn"""
    bl_idname = "gsoc.freefall"
    bl_label = "Free falling body"

    def excute(self, context): 
        ffd = pd.read_csv("free_falling_body.mov", sep=" ", names=["node_no", "x", "y", "z", "eular_x", "eular_y", "eular_z", "vx", "vy", "vz", "wx", "wy", "wz"])
        bpy.ops.mesh.premitive_cube_add()
        x = ffd["x"].values
        y = ffd["y"].values
        z = ffd["z"].values
        frame_no = 0
        obj = bpy.context.active_object
        for i in range(len(x)):
            bpy.context.scene.frame_set(frame_no)
            obj.location = (x[i], y[i], z[i])
            obj.keyframe_insert(data_path="location", index=-1)
            frame_no += 20
        
        return {'FINISHED'}


def register():
    bpy.utils.register_class(GSOC_OT_free_fall)
    return "All Registered"
def unregister():
    bpy.utils.unregister_class(GSOC_OT_free_fall)
    return "All Unregistered"

