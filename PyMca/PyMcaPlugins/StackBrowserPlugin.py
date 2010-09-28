"""

A Stack plugin is a module that will be automatically added to the PyMca stack windows
in order to perform user defined operations on the data stack.

These plugins will be compatible with any stack window that provides the functions:
    #data related
    getStackDataObject
    getStackData
    getStackInfo
    setStack

    #images related
    addImage
    removeImage
    replaceImage

    #mask related
    setSelectionMask
    getSelectionMask

    #displayed curves
    getActiveCurve
    getGraphXLimits
    getGraphYLimits

    #information method
    stackUpdated
    selectionMaskUpdated
"""
import StackPluginBase
try:
    from PyMca import StackBrowser
    import PyMca.PyMca_Icons as PyMca_Icons
except ImportError:
    print "ROIStackPlugin importing from somewhere else"
    import StackBrowser
    import PyMca_Icons

DEBUG = 0

class StackBrowserPlugin(StackPluginBase.StackPluginBase):
    def __init__(self, stackWindow, **kw):
        StackPluginBase.DEBUG = DEBUG
        StackPluginBase.StackPluginBase.__init__(self, stackWindow, **kw)
        self.methodDict = {'Show':[self._showWidget,
                                   "Show Stack Image Browser",
                                   PyMca_Icons.brushselect]}
        self.__methodKeys = ['Show']
        self.widget = None

    def stackUpdated(self):
        if DEBUG:
            print "StackBrowserPlugin.stackUpdated() called"
        if self.widget is None:
            return
        if self.widget.isHidden():
            return
        stack = self.getStackDataObject()
        self.widget.setStackDataObject(stack, stack_name="Stack Index")
        mask = self.getStackSelectionMask()
        self.widget.setSelectionMask(mask)

    def selectionMaskUpdated(self):
        if self.widget is None:
            return
        if self.widget.isHidden():
            return
        mask = self.getStackSelectionMask()
        self.widget.setSelectionMask(mask)

    def mySlot(self, ddict):
        if DEBUG:
            print "mySlot ", ddict['event'], ddict.keys()
        if ddict['event'] == "selectionMaskChanged":
            self.setStackSelectionMask(ddict['current'])
        elif ddict['event'] == "addImageClicked":
            self.addImage(ddict['image'], ddict['title'])
        elif ddict['event'] == "removeImageClicked":
            self.removeImage(ddict['title'])
        elif ddict['event'] == "replaceImageClicked":
            self.replaceImage(ddict['image'], ddict['title'])
        elif ddict['event'] == "resetSelection":
            self.setStackSelectionMask(None)

    #Methods implemented by the plugin
    def getMethods(self):
        return self.__methodKeys

    def getMethodToolTip(self, name):
        return self.methodDict[name][1]

    def getMethodPixmap(self, name):
        return self.methodDict[name][2]

    def applyMethod(self, name):
        return apply(self.methodDict[name][0])

    def _showWidget(self):
        if self.widget is None:
            self.widget = StackBrowser.StackBrowser(parent=None,
                                                    rgbwidget=None,
                                                    selection=True,
                                                    colormap=True,
                                                    imageicons=True,
                                                    standalonesave=True)
            self.widget.setSelectionMode(True)
            qt = StackBrowser.qt
            qt.QObject.connect(self.widget,
                   qt.SIGNAL('MaskImageWidgetSignal'),
                   self.mySlot)

        #Show
        self.widget.show()
        self.widget.raise_()        

        #update
        self.stackUpdated()


MENU_TEXT = "Stack Image Browser"
def getStackPluginInstance(stackWindow, **kw):
    ob = StackBrowserPlugin(stackWindow)
    return ob