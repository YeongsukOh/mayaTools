import maya.cmds as cmds
from importlib import reload

class MarkingMenu():

    NAME = 'YSTOOL'
    
    def __init__(self):
        self._remove_old()
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


    def _remove_old(self):
        """
        Checks if there is a marking menu with the given name and if so deletes it to prepare for creating a new one.
        We do this in order to be able to easily update our marking menus
        Return: n/a
        """
        if cmds.popupMenu(MarkingMenu.NAME, exists=1):
            cmds.deleteUI(MarkingMenu.NAME)
    
    
    def menuItems(self, dag, parent):
        cmds.menuItem( parent = dag, label = "A", radialPosition = "NW", command = self.test)
        cmds.menuItem( parent = dag, label = "B", radialPosition = "W")
        cmds.menuItem( parent = dag, label = "C", radialPosition = "SW") 
        cmds.menuItem( parent = dag, label = "D", radialPosition = "S")
        cmds.menuItem( parent = dag, label = "E", radialPosition = "SE")
        cmds.menuItem( parent = dag, label = "F", radialPosition = "E")
        cmds.menuItem( parent = dag, label = "G", radialPosition = "NE")
        cmds.menuItem( parent = dag, label = "H", radialPosition = "N")


    def test(self):
        print("test")
