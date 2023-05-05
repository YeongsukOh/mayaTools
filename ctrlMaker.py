import maya.cmds as cmds
import maya.OpenMaya as OpenMaya
import json

# load curveShape data
filePath = "C:\\Users\\Yourim Kim\\Documents\\maya\\2022\\scripts\\mayaTools\\curveShapeData.json"

with open(filePath, "r") as curveShapeData:
    data = json.load(curveShapeData)

print(data['crossHeadStick'])

# getting position

# to select transform node of selectedItem
selectedItem = cmds.ls(selection = True)[0]

# convert type from list to tuple
translateVal = cmds.xform(selectedItem, q = True, t = True, ws=True)
rotateVal = cmds.xform(selectedItem, q = True, ro = True)

print(translateVal)
print(rotateVal)
# upack the items to distribute translate X,Y,Z
tX,tY,tZ = translateVal
rX,rY,rZ = rotateVal

# saving curve shape data to json

# loading curve shape data that I choose
ctrl = cmds.curve(p = data['diamondStick'], d = 1)

# maybe xform command will help to get and use location data: need to check


# making group and offset group node as well
grp = cmds.group(em = True, n = "GRP_" + ctrl)
grpOff = cmds.group(em = True, n = "GRP_" + ctrl + "_offset")

cmds.parent(grpOff, grp)
cmds.parent(ctrl,grpOff)

# matching translate values to ctrl

cmds.setAttr(grp + ".translateX", tX)
cmds.setAttr(grp + ".translateY", tY)
cmds.setAttr(grp + ".translateZ", tZ)

# matching rotate values to ctrl
cmds.setAttr(grp + ".rotateX", rX)
cmds.setAttr(grp + ".rotateY", rY)
cmds.setAttr(grp + ".rotateZ", rZ)

# making UI at the end


# get the curveShape that we want
curveData = []
vertexes = cmds.ls(sl = True, fl = True)
for vertex in vertexes:
    position = cmds.xform(vertex, q = True, translation = True)
    curveData.append(position)

print(curveData)
