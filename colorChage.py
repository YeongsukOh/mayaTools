import maya.cmds as cmds
 
def customColor(color):
    selectedItems = cmds.ls(sl = True)[0]
    itemShape = cmds.listRelatives(selectedItems, shapes = True)[0]
    cmds.setAttr(itemShape + ".overrideEnabled", 1)
    cmds.setAttr(itemShape + ".overrideRGBColors", 1)
        
    rgb = ("R","G","B")
        
    cmds.setAttr(itemShape + ".overrideEnabled",1)
    cmds.setAttr(itemShape + ".overrideRGBColors",1)
        
    for channel, color in zip(rgb, color):
        cmds.setAttr(itemShape + ".overrideColor%s" %channel, color)
    
def colorChangerUI():
    if cmds.window("ColorCode",exists=1):
        cmds.deleteUI("ColorCode")
    else:
        cmds.window("ColorCode",tlb=1,t="Custom Color Tool",s=0)
        cmds.gridLayout(cw=30,nc=6,nr=2)
        
        cmds.canvas("RED",rgbValue=(1,0,0),width=20,height=20,pc="customColor((1,0,0))")
        cmds.canvas("ORANGE",rgbValue=(1,0.5,0),width=20,height=20,pc="customColor((1,0.5,0))")
        cmds.canvas("YELLOW",rgbValue=(1,1,0),width=20,height=20,pc="customColor((1,1,0))")
        cmds.canvas("GREEN",rgbValue=(0.5,1,0),width=20,height=20,pc="customColor((0.5,1,0))")
        cmds.canvas("BLUE",rgbValue=(0,0,1),width=20,height=20,pc="customColor((0,0,1))")
        cmds.canvas("DARKBLUE",rgbValue=(0.35,0,1),width=20,height=20,pc="customColor((0.35,0,1))")

        cmds.canvas("ChineseOrange",rgbValue=(0.965, 0.427, 0.267),width=20,height=20,pc="customColor((0.965, 0.427, 0.267))")
        cmds.canvas("Rajah",rgbValue=(0.996, 0.682, 0.396),width=20,height=20,pc="customColor((0.996, 0.682, 0.396))")
        cmds.canvas("KeyLime",rgbValue=(0.902, 0.965, 0.616),width=20,height=20,pc="customColor((0.902, 0.965, 0.616))")
        cmds.canvas("LightMossGreen",rgbValue=(0.667, 0.871, 0.655),width=20,height=20,pc="customColor((0.667, 0.871, 0.655))")
        cmds.canvas("GreenSheen",rgbValue=(0.392, 0.761, 0.651),width=20,height=20,pc="customColor((0.392, 0.761, 0.651))")
        cmds.canvas("CyanCornflowerBlue",rgbValue=(0.176, 0.529, 0.733),width=20,height=20,pc="customColor((0.176, 0.529, 0.733))")
 
        cmds.showWindow("ColorCode")
        cmds.window("ColorCode",edit=1,wh=(180,64))
        
colorChangerUI()