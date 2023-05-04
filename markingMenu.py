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

    
    def menuItem(self, menu, parent):
        
        cmds.menuItem( parent = menu, label = "A", radialPosition = "NW")
        cmds.menuItem( parent = menu, label = "B",radialPosition = "W")
        cmds.menuItem( parent = menu, label = "C",radialPosition = "SW") 
        cmds.menuItem( parent = menu, label = "D",radialPosition = "S")
        cmds.menuItem( parent = menu, label = "E",radialPosition = "SE")
        cmds.menuItem( parent = menu, label = "F",radialPosition = "E")
        cmds.menuItem( parent = menu, label = "G",radialPosition = "NE")
        cmds.menuItem( parent = menu, label = "H",  radialPosition = "N")

reload(MarkingMenu)
test = MarkingMenu()
