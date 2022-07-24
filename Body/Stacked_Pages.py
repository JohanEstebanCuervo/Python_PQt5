from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from Pages.Page_Capture import *
from Pages.Page_Camera import *
from Pages.Page_Iluminator import *
from Pages.Page_ColorReproduction import *


class Stacked_Pages(QStackedWidget):

    def __init__(self, App):
        super(Stacked_Pages, self).__init__(App)
        self.App = App
        self.setObjectName(u"Stacked_Pages")

        self.page_capture = Page_Capture(App)
        self.addWidget(self.page_capture)

        self.page_camera = Page_Camera(App)
        self.addWidget(self.page_camera)

        self.page_iluminator = Page_Iluminator(App)
        self.addWidget(self.page_iluminator)

        self.page_colorReproduction = Page_ColorReproduction(App)
        self.addWidget(self.page_colorReproduction)

        self.setCurrentIndex(0)
