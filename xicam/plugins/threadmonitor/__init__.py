from qtpy.QtCore import *
from qtpy.QtGui import *
from qtpy.QtWidgets import *

from xicam.gui.static import path
from xicam.core.threads import manager as threadmanager
from xicam.plugins import GUIPlugin, GUILayout


class ThreadMonitorPlugin(GUIPlugin):
    name = 'Thread Monitor'

    def __init__(self):
        self.monitorwidget = QListView()
        self.toolbar = QToolBar()
        actionPause = QAction(QIcon(str(path('icons/pause.png'))), "Pause", self.toolbar)
        actionPause.triggered.connect(self.pause)
        actionPause.setCheckable(True)
        self.toolbar.addAction(actionPause)
        self.stages = {'Monitor': GUILayout(self.monitorwidget, top=self.toolbar)}
        super(ThreadMonitorPlugin, self).__init__()

        self.model = threadmanager
        self.monitorwidget.setModel(self.model)
        self._test()


    def pause(self):
        if self.timer.isActive():
            self.timer.stop()
        else:
            self.timer.start()



    def _test(self):

        from xicam.core import threads
        import time
        def test():
            a = 0
            for i in range(10):
                a += 1
                time.sleep(1)

        for i in range(100):
            t = threads.QThreadFuture(test)
            t.start()
