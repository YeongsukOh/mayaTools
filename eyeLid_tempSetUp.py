import maya.cmds as cmds

# it can be able to change part
crvShape = "R_eyeLidUp_lowCrvShape"
name = crvShape.split("Shape")[0]
jointCounts = 5
ratio = 1/(jointCounts-1)
initRatio = 0

for number in range(jointCounts):
    curveInfo = cmds.createNode("pointOnCurveInfo", n = "pointOnCurveInfo_" + name)
    cmds.connectAttr(crvShape + '.worldSpace[0]', curveInfo + '.inputCurve')
    joint = cmds.createNode("joint", n = name + "_jnt")
    cmds.setAttr(curveInfo + '.turnOnPercentage', True)
    cmds.setAttr(curveInfo + '.parameter', initRatio)
    cmds.connectAttr(curveInfo + '.position', joint + '.translate')
    
    initRatio += ratio