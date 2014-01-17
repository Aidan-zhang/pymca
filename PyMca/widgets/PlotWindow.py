#/*##########################################################################
# Copyright (C) 2004-2014 European Synchrotron Radiation Facility
#
# This file is part of the PyMca X-ray Fluorescence Toolkit developed at
# the ESRF by the Software group.
#
# This toolkit is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 2 of the License, or (at your option)
# any later version.
#
# PyMca is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# PyMca; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
# PyMca follows the dual licensing model of Riverbank's PyQt and cannot be
# used as a free plugin for a non-free program.
#
# Please contact the ESRF industrial unit (industry@esrf.fr) if this license
# is a problem for you.
#############################################################################*/
__author__ = "V.A. Sole - ESRF Software Group"
__doc__ = """
This window is a solution for PyMca.
It handles the plugins and adds a toolbar to the PlotWidget

"""
import sys
import os
import traceback
from PyMca.plotting import PlotWidget
try:
    from PyMca.plotting.backends import MatplotlibBackend
    MATPLOTLIB = True
except:
    MATPLOTLIB = False
try:
    from PyMca.plotting.backends import PyQtGraphBackend
    PYQTGRAPH = True
except:
    PYQTGRAPH = False

from PyMca import PyMcaQt as qt
from PyMca.PyMca_Icons import IconDict
QTVERSION = qt.qVersion()
DEBUG = 0

class PlotWindow(PlotWidget.PlotWidget):
    def __init__(self, parent=None, backend=None, plugins=True, newplot=False, **kw):
        if backend is None:
            if PYQTGRAPH:
                backend = PyQtGraphBackend.PyQtGraphBackend
            elif MATPLOTLIB:
                backend = MatplotlibBackend.MatplotlibBackend
        super(PlotWindow, self).__init__(parent=parent, backend=backend)
        self.pluginsIconFlag = plugins
        self.newplotIconsFlag = newplot
        self.setWindowType(None)      # None, "SCAN", "MCA"
        self._initIcons()
        self._buildToolBar(kw)
        self._toggleCounter = 0

    def setWindowType(self, wtype=None):
        if wtype not in [None, "SCAN", "MCA"]:
            print("Unsupported window type. Default to None")
        self.plotType = wtype

    def _initIcons(self):
        self.normalIcon	= qt.QIcon(qt.QPixmap(IconDict["normal"]))
        self.zoomIcon	= qt.QIcon(qt.QPixmap(IconDict["zoom"]))
        self.roiIcon	= qt.QIcon(qt.QPixmap(IconDict["roi"]))
        self.peakIcon	= qt.QIcon(qt.QPixmap(IconDict["peak"]))

        self.zoomResetIcon	= qt.QIcon(qt.QPixmap(IconDict["zoomreset"]))
        self.roiResetIcon	= qt.QIcon(qt.QPixmap(IconDict["roireset"]))
        self.peakResetIcon	= qt.QIcon(qt.QPixmap(IconDict["peakreset"]))
        self.refreshIcon	= qt.QIcon(qt.QPixmap(IconDict["reload"]))

        self.logxIcon	= qt.QIcon(qt.QPixmap(IconDict["logx"]))
        self.logyIcon	= qt.QIcon(qt.QPixmap(IconDict["logy"]))
        self.xAutoIcon	= qt.QIcon(qt.QPixmap(IconDict["xauto"]))
        self.yAutoIcon	= qt.QIcon(qt.QPixmap(IconDict["yauto"]))
        self.togglePointsIcon = qt.QIcon(qt.QPixmap(IconDict["togglepoints"]))

        self.fitIcon	= qt.QIcon(qt.QPixmap(IconDict["fit"]))
        self.searchIcon	= qt.QIcon(qt.QPixmap(IconDict["peaksearch"]))

        self.averageIcon	= qt.QIcon(qt.QPixmap(IconDict["average16"]))
        self.deriveIcon	= qt.QIcon(qt.QPixmap(IconDict["derive"]))
        self.smoothIcon     = qt.QIcon(qt.QPixmap(IconDict["smooth"]))
        self.swapSignIcon	= qt.QIcon(qt.QPixmap(IconDict["swapsign"]))
        self.yMinToZeroIcon	= qt.QIcon(qt.QPixmap(IconDict["ymintozero"]))
        self.subtractIcon	= qt.QIcon(qt.QPixmap(IconDict["subtract"]))
        
        self.printIcon	= qt.QIcon(qt.QPixmap(IconDict["fileprint"]))
        self.saveIcon	= qt.QIcon(qt.QPixmap(IconDict["filesave"]))            

        self.pluginIcon     = qt.QIcon(qt.QPixmap(IconDict["plugin"])) 

    def _buildToolBar(self, kw=None):
        if kw is None:
            kw = {}
        self.toolBar = qt.QToolBar(self)
        #Autoscale
        self._addToolButton(self.zoomResetIcon,
                            self._zoomReset,
                            'Auto-Scale the Graph')

        #y Autoscale
        self.yAutoScaleButton = self._addToolButton(self.yAutoIcon,
                            self._yAutoScaleToggle,
                            'Toggle Autoscale Y Axis (On/Off)',
                            toggle = True)
        self.yAutoScaleButton.setChecked(True)
        self.yAutoScaleButton.setDown(True)


        #x Autoscale
        self.xAutoScaleButton = self._addToolButton(self.xAutoIcon,
                            self._xAutoScaleToggle,
                            'Toggle Autoscale X Axis (On/Off)',
                            toggle = True)
        self.xAutoScaleButton.setChecked(True)
        self.xAutoScaleButton.setDown(True)

        #y Logarithmic
        if kw.get('logy', True):
            self.yLogButton = self._addToolButton(self.logyIcon,
                                self._toggleLogY,
                                'Toggle Logarithmic Y Axis (On/Off)',
                                toggle = True)
            self.yLogButton.setChecked(False)
            self.yLogButton.setDown(False)

        #x Logarithmic
        if kw.get('logx', True):
            self.xLogButton = self._addToolButton(self.logxIcon,
                                self._toggleLogX,
                                'Toggle Logarithmic X Axis (On/Off)',
                                toggle = True)
            self.xLogButton.setChecked(False)
            self.xLogButton.setDown(False)

        #toggle Points/Lines
        tb = self._addToolButton(self.togglePointsIcon,
                             self._togglePointsSignal,
                             'Toggle Points/Lines')


        #fit icon
        if kw.get('fit', False):
            self.fitButton = self._addToolButton(self.fitIcon,
                                         self._fitIconSignal,
                                 'Simple Fit of Active Curve')


        if self.newplotIconsFlag:
            tb = self._addToolButton(self.averageIcon,
                                self._averageIconSignal,
                                 'Average Plotted Curves')

            tb = self._addToolButton(self.deriveIcon,
                                self._deriveIconSignal,
                                 'Take Derivative of Active Curve')

            tb = self._addToolButton(self.smoothIcon,
                                 self._smoothIconSignal,
                                 'Smooth Active Curve')

            tb = self._addToolButton(self.swapSignIcon,
                                self._swapSignIconSignal,
                                'Multiply Active Curve by -1')

            tb = self._addToolButton(self.yMinToZeroIcon,
                                self._yMinToZeroIconSignal,
                                'Force Y Minimum to be Zero')

            tb = self._addToolButton(self.subtractIcon,
                                self._subtractIconSignal,
                                'Subtract Active Curve')
        #save
        infotext = 'Save Active Curve or Widget'
        tb = self._addToolButton(self.saveIcon,
                                 self._saveIconSignal,
                                 infotext)

        if self.pluginsIconFlag:
            infotext = "Call/Load 1D Plugins"
            tb = self._addToolButton(self.pluginIcon,
                                 self._pluginClicked,
                                 infotext)

        self.toolBar.addWidget(qt.HorizontalSpacer(self.toolBar))

        # ---print
        tb = self._addToolButton(self.printIcon,
                                 self.printGraph,
                                 'Prints the Graph')

        self.addToolBar(self.toolBar)

    def _addToolButton(self, icon, action, tip, toggle=None):
        tb      = qt.QToolButton(self.toolBar)            
        tb.setIcon(icon)
        tb.setToolTip(tip)
        if toggle is not None:
            if toggle:
                tb.setCheckable(1)
        self.toolBar.addWidget(tb)
        tb.clicked.connect(action)
        return tb
                
    def _zoomReset(self):
        if DEBUG:
            print("_zoomReset")
        self.resetZoom()

    def _yAutoScaleToggle(self):
        if DEBUG:
            print("toggle Y auto scaling")
        if self.isYAxisAutoScale():
            self.setYAxisAutoScale(False)
            self.yAutoScaleButton.setDown(False)
            self.yAutoScaleButton.setChecked(False)
            ymin, ymax = self.getGraphYLimits()
            self.setGraphYLimits(ymin, ymax)
        else:
            self.setYAxisAutoScale(True)
            self.yAutoScaleButton.setDown(True)
            self.resetZoom()

    def _xAutoScaleToggle(self):
        if DEBUG:
            print("toggle X auto scaling")
        if self.isXAxisAutoScale():
            self.setXAxisAutoScale(False)
            self.xAutoScaleButton.setDown(False)
            self.xAutoScaleButton.setChecked(False)
            xmin, xmax = self.getGraphXLimits()
            self.setGraphXLimits(xmin, xmax)
        else:
            self.setXAxisAutoScale(True)
            self.xAutoScaleButton.setDown(True)
            self.resetZoom()
                       
    def _toggleLogX(self):
        if DEBUG:
            print("toggle logarithmic X scale")
        if self.isXAxisLogarithmic():
            self.setXAxisLogarithmic(False)
        else:
            self.setXAxisLogarithmic(True)

    def setXAxisLogarithmic(self, flag=True):
        super(PlotWindow, self).setXAxisLogarithmic(flag) 
        self.xLogButton.setChecked(flag)
        self.xLogButton.setDown(flag)

    def _toggleLogY(self):
        if DEBUG:
            print("_toggleLogY")
        if self.isYAxisLogarithmic():
            self.setYAxisLogarithmic(False)
        else:
            self.setYAxisLogarithmic(True)

    def setYAxisLogarithmic(self, flag=True):
        super(PlotWindow, self).setYAxisLogarithmic(flag) 
        self.yLogButton.setChecked(flag)
        self.yLogButton.setDown(flag)

    def _togglePointsSignal(self):
        if DEBUG:
            print("toggle points signal")
        self._toggleCounter = (self._toggleCounter + 1) % 3
        if self._toggleCounter == 1:
            self.setDefaultPlotLines(True)
            self.setDefaultPlotPoints(True)
        elif self._toggleCounter == 2:
            self.setDefaultPlotPoints(True)
            self.setDefaultPlotLines(False)
        else:
            self.setDefaultPlotLines(True)
            self.setDefaultPlotPoints(False)

    def _fitIconSignal(self):
        print("fit icon signal")

    def _averageIconSignal(self):
        print("average icon signal")

    def _deriveIconSignal(self):
        print("deriveIconSignal")

    def _smoothIconSignal(self):
        print("smoothIconSignal")

    def _swapSignIconSignal(self):
        print("_swapSignIconSignal")

    def _yMinToZeroIconSignal(self):
        print("_yMinToZeroIconSignal")

    def _subtractIconSignal(self):
        print("_subtractIconSignal")

    def _saveIconSignal(self):
        print("_saveIconSignal")

    def _pluginClicked(self):
        actionList = []
        menu = qt.QMenu(self)
        text = qt.QString("Reload")
        menu.addAction(text)
        actionList.append(text)
        menu.addSeparator()
        callableKeys = ["Dummy"]
        for m in self.pluginList:
            if m in ["PyMcaPlugins.Plugin1DBase", "Plugin1DBase"]:
                continue
            module = sys.modules[m]
            if hasattr(module, 'MENU_TEXT'):
                text = qt.QString(module.MENU_TEXT)
            else:
                text = os.path.basename(module.__file__)
                if text.endswith('.pyc'):
                    text = text[:-4]
                elif text.endswith('.py'):
                    text = text[:-3]
                text = qt.QString(text)
            methods = self.pluginInstanceDict[m].getMethods(plottype=self.plotType) 
            if not len(methods):
                continue
            menu.addAction(text)
            actionList.append(text)
            callableKeys.append(m)
        a = menu.exec_(qt.QCursor.pos())
        if a is None:
            return None
        idx = actionList.index(a.text())
        if idx == 0:
            n = self.getPlugins()
            if n < 1:
                msg = qt.QMessageBox(self)
                msg.setIcon(qt.QMessageBox.Information)
                msg.setText("Problem loading plugins")
                msg.exec_()
            return        
        key = callableKeys[idx]
        methods = self.pluginInstanceDict[key].getMethods(plottype=self.plotType)
        if len(methods) == 1:
            idx = 0
        else:
            actionList = []
            methods.sort()
            menu = qt.QMenu(self)
            for method in methods:
                text = qt.QString(method)
                pixmap = self.pluginInstanceDict[key].getMethodPixmap(method)
                tip = qt.QString(self.pluginInstanceDict[key].getMethodToolTip(method))
                if pixmap is not None:
                    action = qt.QAction(qt.QIcon(qt.QPixmap(pixmap)), text, self)
                else:
                    action = qt.QAction(text, self)
                if tip is not None:
                    action.setToolTip(tip)
                menu.addAction(action)
                actionList.append((text, pixmap, tip, action))
            qt.QObject.connect(menu, qt.SIGNAL("hovered(QAction *)"), self._actionHovered)
            a = menu.exec_(qt.QCursor.pos())
            if a is None:
                return None
            idx = -1
            for action in actionList:
                if a.text() == action[0]:
                    idx = actionList.index(action)
        try:
            self.pluginInstanceDict[key].applyMethod(methods[idx])    
        except:
            msg = qt.QMessageBox(self)
            msg.setIcon(qt.QMessageBox.Critical)
            msg.setWindowTitle("Plugin error")
            msg.setText("An error has occured while executing the plugin:")
            msg.setInformativeText(str(sys.exc_info()[1]))
            msg.setDetailedText(traceback.format_exc())
            msg.exec_()

    def _actionHovered(self, action):
        tip = action.toolTip()
        if str(tip) != str(action.text()):
            qt.QToolTip.showText(qt.QCursor.pos(), tip)

    def printGraph(self):
        print("prints the graph")

if __name__ == "__main__":
    import numpy
    x = numpy.arange(100.)
    y = x * x
    app = qt.QApplication([])
    plot = PlotWindow()#uselegendmenu=True)
    plot.show()
    plot.addCurve(x, y, "dummy")
    plot.addCurve(x+100, x*x)
    plot.addCurve(x, -y, "- dummy")
    print("Active curve = ", plot.getActiveCurve(just_legend=True))
    print("X Limits = ",     plot.getGraphXLimits())
    print("Y Limits = ",     plot.getGraphYLimits())
    print("All curves = ",   plot.getAllCurves(just_legend=True))
    #plot.removeCurve("dummy")
    #plot.addCurve(x, 2 * y, "dummy 2")
    #print("All curves = ",   plot.getAllCurves())
    app.exec_()

    
