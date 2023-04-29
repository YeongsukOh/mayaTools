import maya.cmds as cmds


class MyTool():

    NAMETOOL = "toolBox"

    def launcingUi(self):    
        window = cmds.window(self.NAMETOOL, title = "simpleTools", widthHeight = (300,150))
        cmds.columnLayout(adjustableColumn = True)
        cmds.button(label = "cube", command = self.createPolyCube)
        cmds.button(label = "sphere", command = self.createPolysphere)
        cmds.setParent("..")
        cmds.showWindow(window)


    def createPolyCube(self,*args):
        cmds.polyCube()

    
    def createPolysphere(self, *args):
        cmds.polySphere()
        

tool = MyTool()
tool.launcingUi()
