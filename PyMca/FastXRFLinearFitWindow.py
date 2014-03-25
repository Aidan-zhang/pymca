#/*##########################################################################
# Copyright (C) 2013 European Synchrotron Radiation Facility
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
__author__ = "V.A. Sole - ESRF Data Analysis"
import sys
import numpy
from PyMca import PyMcaQt as qt
from PyMca.PyMca_Icons import IconDict
from PyMca import PyMcaFileDialogs

DEBUG = 0

class FastXRFLinearFitWindow(qt.QWidget):
    def __init__(self, parent=None):
        qt.QWidget.__init__(self, parent)
        self.setWindowTitle("FastXRFLinearFitWindow")
        self.setWindowIcon(qt.QIcon(qt.QPixmap(IconDict['gioconda16'])))
        self.mainLayout = qt.QGridLayout(self)
        self.mainLayout.setContentsMargins(0, 0, 0, 0)

        # configuration file
        configLabel = qt.QLabel(self)
        configLabel.setText("Fit Configuration File:")
        self._configLine = qt.QLineEdit(self)
        self._configLine.setReadOnly(True)

        self._configButton = qt.QPushButton(self)
        self._configButton.setText("Browse")
        self._configButton.setAutoDefault(False)
        self._configButton.clicked.connect(self.browseConfigurationFile)

        # output directory
        outLabel   = qt.QLabel(self)
        outLabel.setText("Output dir:")
        self._outLine = qt.QLineEdit(self)
        self._outLine.setReadOnly(True)

        self._outButton = qt.QPushButton(self)
        self._outButton.setText('Browse')
        self._outButton.setAutoDefault(False)
        self._outButton.clicked.connect(self.browseOutputDir)

        # output file name
        fileLabel   = qt.QLabel(self)
        fileLabel.setText("Output file root:")
        self._fileLine = qt.QLineEdit(self)
        self._fileLine.setReadOnly(False)
        self._fileLine.setText("images")

        # concentrations
        self._concentrationsBox = qt.QCheckBox(self)
        self._concentrationsBox.setText("calculate concentrations")
        self._concentrationsBox.setChecked(False)
        self._concentrationsBox.setEnabled(True)

        # weight method
        self._weightWidget = qt.QWidget(self)
        self._weightWidget.mainLayout = qt.QHBoxLayout(self._weightWidget)
        self._weightWidget.mainLayout.setContentsMargins(0, 0, 0, 0)
        self._weightWidget.mainLayout.setSpacing(0)
        self._weightButtonGroup = qt.QButtonGroup(self._weightWidget)
        i = 0
        weightLabel = qt.QLabel(self)
        weightLabel.setText("Weight policy: ")
        for txt in ["No Weight (Fastest)", "Average Weight (Fast)", "Individual Weights (slow)"]:
            button = qt.QRadioButton(self._weightWidget)
            button.setText(txt)
            self._weightButtonGroup.addButton(button)
            self._weightButtonGroup.setId(button, i)
            self._weightWidget.mainLayout.addWidget(button)
            i += 1
        self._weightButtonGroup.buttons()[0].setChecked(True)
        #self._weightWidget.mainLayout.addWidget(qt.HorizontalSpacer(self._weightWidget))

        self.mainLayout.addWidget(configLabel, 0, 0)
        self.mainLayout.addWidget(self._configLine, 0, 1)
        self.mainLayout.addWidget(self._configButton, 0, 2)
        self.mainLayout.addWidget(outLabel, 1, 0)
        self.mainLayout.addWidget(self._outLine, 1, 1)
        self.mainLayout.addWidget(self._outButton, 1, 2)
        self.mainLayout.addWidget(fileLabel, 2, 0)
        self.mainLayout.addWidget(self._fileLine, 2, 1)
        self.mainLayout.addWidget(self._concentrationsBox, 4, 0, 1, 2)
        self.mainLayout.addWidget(weightLabel, 3, 0)
        self.mainLayout.addWidget(self._weightWidget, 3, 1, 1, 1)

    def sizeHint(self):
        return qt.QSize(int(1.8 * qt.QWidget.sizeHint(self).width()),
                        qt.QWidget.sizeHint(self).height())

    def browseConfigurationFile(self):
        f = PyMcaFileDialogs.getFileList(parent=self,
                                     filetypelist=["Configuration files (*.cfg)"],
                                     message="Open a new fit config file",
                                     mode="OPEN",
                                     single=True)
        if len(f):
            self._configLine.setText(f[0])

    def browseOutputDir(self):
        f = PyMcaFileDialogs.getExistingDirectory(parent=self,
                                     message="Please select output directory",
                                     mode="OPEN")
        if len(f):
            self._outLine.setText(f)

    def getParameters(self):
        ddict = {}
        ddict['configuration'] = qt.safe_str(self._configLine.text())
        ddict['output_dir'] = qt.safe_str(self._outLine.text())
        ddict['file_root'] = qt.safe_str(self._fileLine.text())
        if self._concentrationsBox.isChecked():
            ddict['concentrations'] = 1
        else:
            ddict['concentrations'] = 0
        ddict['weight_policy'] = self._weightButtonGroup.checkedId()
        return ddict
        
class FastXRFLinearFitDialog(qt.QDialog):
    def __init__(self, parent=None):
        qt.QDialog.__init__(self, parent)   
        self.setWindowTitle("Fast XRF Linear Fit Dialog")
        self.setWindowIcon(qt.QIcon(qt.QPixmap(IconDict['gioconda16'])))
        self.mainLayout = qt.QGridLayout(self)
        self.mainLayout.setContentsMargins(10, 10, 10, 10)
        self.parametersWidget = FastXRFLinearFitWindow(self)

        self.rejectButton= qt.QPushButton(self)
        self.rejectButton.setAutoDefault(False)
        self.rejectButton.setText("Cancel")
        
        self.acceptButton= qt.QPushButton(self)
        self.acceptButton.setAutoDefault(False)
        self.acceptButton.setText("OK")

        self.rejectButton.clicked.connect(self.reject)
        self.acceptButton.clicked.connect(self.accept)
        
        self.mainLayout.addWidget(self.parametersWidget, 0, 0, 5, 4)
        self.mainLayout.addWidget(self.rejectButton, 6, 1)
        self.mainLayout.addWidget(self.acceptButton, 6, 2)

    def getParameters(self):
        return self.parametersWidget.getParameters()

if __name__ == "__main__":
    app = qt.QApplication([])
    w = FastXRFLinearFitDialog()
    ret = w.exec_()
    if ret:
        print(w.getParameters())
    #app.exec_()
