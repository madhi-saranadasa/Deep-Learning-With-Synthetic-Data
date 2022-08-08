import bpy
import random
import os
from math import *

cameraAngle = [90, 0, 0]
angleTolerance = [10, 180, 10]
bLesion = True
iterations = 4000

lumen = bpy.data.node_groups["LumenNodes"]
camera = bpy.data.objects['Camera']

def RandomizeCamera():
    adjustx = random.uniform(angleTolerance[0] * -1, angleTolerance[0])
    adjusty = random.uniform(angleTolerance[1] * -1, angleTolerance[1])
    adjustz = random.uniform(angleTolerance[2] * -1, angleTolerance[2])
    
    camera.rotation_euler[0] = radians(cameraAngle[0] + adjustx)
    camera.rotation_euler[1] = radians(cameraAngle[1] + adjusty)
    camera.rotation_euler[2] = radians(cameraAngle[2] + adjustz)
    
def RenderImage(path):
    bpy.context.scene.render.filepath = os.path.join(bpy.data.filepath, path)
    bpy.ops.render.render(write_still = True)
    
def RandomizeLumen():
    
    lumen.nodes["LesionBool"].boolean = bLesion
    lumen.nodes["Index"].integer = random.randint(0,4)
    lumen.nodes["UVTransform"].inputs[1].default_value[1] = random.uniform(0, 0.2)
    lumen.nodes["Diameter"].inputs[4].default_value = random.uniform(7, 10.5)


for i in range(0, iterations):
    
    RandomizeLumen()
    RandomizeCamera()
    
    if bLesion:
        lumen.nodes["Set Material"].inputs[2].default_value = bpy.data.materials["LumenMat"]
        path = "../Images/Lesion/Lesion" + str(i) + ".jpg"
        RenderImage(path)
        
        lumen.nodes["Set Material"].inputs[2].default_value = bpy.data.materials["MaskMat"]
        path = "../Images/Mask/Mask" + str(i) + ".jpg"
        RenderImage(path)
    else:
        lumen.nodes["Set Material"].inputs[2].default_value = bpy.data.materials["LumenMat"]
        path = "../Images/Normal/Normal" + str(i) + ".jpg"
        RenderImage(path)
        
    if i % 50 == 0:
        print(i)
    