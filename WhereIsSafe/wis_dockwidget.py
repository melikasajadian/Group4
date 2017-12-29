# -*- coding: utf-8 -*-
"""
/***************************************************************************
 WhereIsSafeDockWidget
                                 A QGIS plugin
 This Plugin provides users with info about available options in case of toxic gas spread
                             -------------------
        begin                : 2017-12-27
        git sha              : $Format:%H$
        copyright            : (C) 2017 by Melika Sajadian
        email                : melikasajadian@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os

from PyQt4 import QtGui, uic
from PyQt4.QtCore import pyqtSignal

from PyQt4 import QtCore, uic
from PyQt4.QtGui import QWidget, QLabel, QHBoxLayout, QVBoxLayout, QDockWidget, QPixmap, QPushButton, QListWidgetItem, \
    QGridLayout
from qgis.core import *
from qgis.networkanalysis import *
from qgis.gui import *
import processing
from datetime import datetime, timedelta

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'wis_dockwidget_base.ui'))


class WhereIsSafeDockWidget(QtGui.QDockWidget, FORM_CLASS):

    closingPlugin = pyqtSignal()

    def __init__(self,iface, parent=None):
        """Constructor."""
        super(WhereIsSafeDockWidget, self).__init__(parent)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)

        self.iface=iface
        self.canvas = self.iface.mapCanvas()

        self.start_btn.clicked.connect(self.situOverview)
        self.monitor_btn.clicked.connect(self.go2monitorFun)
        self.profile_btn.clicked.connect(self.go2profileFun)
        self.backm_btn.clicked.connect(self.back2mapFun)
        self.backp_btn.clicked.connect(self.back2mapFun)
        self.call_btn.clicked.connect(self.callFun)
        self.endcall_btn.clicked.connect(self.back2mapFun)



        self.Monitor.hide()
        self.Profile.hide()
        self.Call112.hide()



    def closeEvent(self, event):
        self.closingPlugin.emit()
        event.accept()


    def situOverview(self):
        self.FirstPage.hide()

    def go2monitorFun(self):
        self.map_canvas.hide()
        self.Monitor.show()
        getattr(self.Monitor, "raise")()

    def go2profileFun(self):
        self.map_canvas.hide()
        self.Profile.show()
        getattr(self.Profile, "raise")()

    def back2mapFun(self):
        self.Profile.hide()
        self.Monitor.hide()
        self.Call112.hide()
        self.map_canvas.show()
        getattr(self.map_canvas, "raise")()

    def callFun(self):
        self.map_canvas.hide()
        self.Call112.show()
        getattr(self.Call112, "raise")()







