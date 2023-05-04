import maya.cmds as cmds
from importlib import reload

class MarkingMenu():

    NAME = 'YSTOOL'
    
    def __init__(self):
        self.launch_menu()

    def launch_menu(self):
        dag = cmds.popupMenu(self.NAME,
                             markingMenu = True,
                             ctrlModifier = True,
                             altModifier = True,
                             shiftModifier = False,
                             button = 1,
                             parent = "viewPanes",
                             postMenuCommandOnce = True,
                             postMenuCommand = self.menuItems,
                             )

    
    def menuItems(self, dag, parent):
        cmds.menuItem( label = "A", parent = dag, radialPosition = "NW")
        cmds.menuItem( label = "B", parent = dag, radialPosition = "W")
        cmds.menuItem( label = "C", parent = dag, radialPosition = "SW") 
        cmds.menuItem( label = "D", parent = dag, radialPosition = "S")
        cmds.menuItem( label = "E", parent = dag, radialPosition = "SE")
        cmds.menuItem( label = "F", parent = dag, radialPosition = "E")
        cmds.menuItem( label = "G", parent = dag, radialPosition = "NE")
        cmds.menuItem( label = "H", parent = dag, radialPosition = "N")
