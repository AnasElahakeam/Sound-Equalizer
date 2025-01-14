from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph as pg
import RetranslateUI
import Spectrogram
import Navigations
import Resources
import Equalizer
import Data
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setGeometry(QtCore.QRect(0, 0, 1110, 450))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(False)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Resources/images/sig.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 0, 1070, 350))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(6, 0))
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setIconSize(QtCore.QSize(32, 32))
        self.tabWidget.setElideMode(QtCore.Qt.ElideLeft)
        #self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setMovable(True)
        #self.tabWidget.setTabBarAutoHide(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.Graph_Before = pg.PlotWidget(self.tab)
        self.Graph_Before.setGeometry(QtCore.QRect(50, 550, 0 , 0))
        self.Graph_Before.setObjectName("Graph_Before")
        self.Graph_Before.setTitle("Before")

        self.Spectrogram_Before = pg.GraphicsLayoutWidget(self.tab)
        self.Spectrogram_Before.setGeometry(QtCore.QRect(1050, 520, 0, 0))
        self.Spectrogram_Before.setObjectName("Spectrogram_Before")
        self.Spectroplot_Before = self.Spectrogram_Before.addPlot()

        self.img_Before = pg.ImageItem()
        self.Spectroplot_Before.addItem(self.img_Before)
        self.hist_Before = pg.HistogramLUTItem()
        self.hist_Before.setImageItem(self.img_Before)

        self.Spectrogram_Before.addItem(self.hist_Before)
        self.Spectrogram_Before.show()
        self.hist_Before.gradient.restoreState(
            {'mode': 'rgb',
                'ticks': [(0.5, (0, 182, 188, 255)),
                          (1.0, (246, 111, 0, 255)),
                          (0.0, (75, 0, 113, 255))]})


        self.Spectrogram_After = pg.GraphicsLayoutWidget(self.tab)
        self.Spectrogram_After.setGeometry(QtCore.QRect(1050, 10, 0, 0))
        self.Spectrogram_After.setObjectName("Spectrogram_After")
        self.Spectroplot_After = self.Spectrogram_After.addPlot()

        self.img_After = pg.ImageItem()
        self.Spectroplot_After.addItem(self.img_After)
        self.hist_After = pg.HistogramLUTItem()
        self.hist_After.setImageItem(self.img_After)
        
        self.Spectrogram_After.addItem(self.hist_After)
        self.Spectrogram_After.show()
        self.hist_After.gradient.restoreState(
            {'mode': 'rgb',
                'ticks': [(0.5, (0, 182, 188, 255)),
                          (1.0, (246, 111, 0, 255)),
                          (0.0, (75, 0, 113, 255))]})

        self.Graph_After = pg.PlotWidget(self.tab)
        self.Graph_After.setGeometry(QtCore.QRect(50, 10, 961, 271))
        self.Graph_After.setObjectName("Graph_After")
        self.Graph_After.setTitle("After")
        self.frame = QtWidgets.QFrame(self.tab)
        self.frame.setGeometry(QtCore.QRect(50, 310, 0, 0))
        self.frame.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame.setAutoFillBackground(True)
        self.frame.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setLineWidth(0)
        self.frame.setMidLineWidth(0)
        self.frame.setObjectName("frame")
        self.layoutWidget = QtWidgets.QWidget(self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(1, 15, 961, 161))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setSizeConstraint(
            QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        self.Slider = []
        for i in range(10):
            self.Slider.append(QtWidgets.QSlider(self.layoutWidget))
            sizePolicy.setHeightForWidth(
                self.Slider[i].sizePolicy().hasHeightForWidth())
            self.Slider[i].setSizePolicy(sizePolicy)
            self.Slider[i].setMaximum(5)
            self.Slider[i].setSliderPosition(1)
            self.Slider[i].setOrientation(QtCore.Qt.Vertical)
            self.Slider[i].setInvertedControls(False)
            self.Slider[i].setTickPosition(
                QtWidgets.QSlider.TicksBothSides)
            self.Slider[i].setTickInterval(1)
            self.Slider[i].setObjectName("Slider_{}".format(i+1))
            self.horizontalLayout.addWidget(self.Slider[i])

        self.layoutWidget_2 = QtWidgets.QWidget(self.frame)
        self.layoutWidget_2.setGeometry(QtCore.QRect(0, 180, 961, 31))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_2.setSizeConstraint(
            QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = []
        for i in range(10):
            self.label.append(QtWidgets.QLabel(self.layoutWidget_2))
            self.label[i].setAlignment(
                QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
            self.label[i].setIndent(3+i*6)
            self.label[i].setObjectName("label_{}".format(i+1))
            self.horizontalLayout_2.addWidget(self.label[i])

        self.tabWidget.addTab(self.tab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1537, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuNavigation = QtWidgets.QMenu(self.menubar)
        self.menuNavigation.setObjectName("menuNavigation")
        self.menuScroll = QtWidgets.QMenu(self.menuNavigation)
        self.menuScroll.setObjectName("menuScroll")
        self.menuZoom = QtWidgets.QMenu(self.menuNavigation)
        self.menuZoom.setObjectName("menuZoom")
        self.menuSpeed = QtWidgets.QMenu(self.menuNavigation)
        self.menuSpeed.setObjectName("menuSpeed")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuTheme = QtWidgets.QMenu(self.menubar)
        self.menuTheme.setObjectName("menuTheme")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setFloatable(False)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Resources/images/open.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen.setIcon(icon1)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/Resources/images/save.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon2)
        self.actionSave.setObjectName("actionSave")
        self.actionTab = QtWidgets.QAction(MainWindow)
        self.actionTab.setObjectName("actionTab")
        self.actionZoom_in = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(
            ":/Resources/images/zoom in.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionZoom_in.setIcon(icon3)
        self.actionZoom_in.setObjectName("actionZoom_in")
        self.actionZoom_out = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(
            ":/Resources/images/zoom out.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionZoom_out.setIcon(icon4)
        self.actionZoom_out.setObjectName("actionZoom_out")
        self.actionLeft = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/Resources/images/back.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLeft.setIcon(icon5)
        self.actionLeft.setObjectName("actionLeft")
        self.actionRight = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/Resources/images/next.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRight.setIcon(icon6)
        self.actionRight.setObjectName("actionRight")
        self.actionFaster = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(
            ":/Resources/images/Speed Up.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFaster.setIcon(icon7)
        self.actionFaster.setObjectName("actionFaster")
        self.actionSlower = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(
            ":/Resources/images/Speed Down.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSlower.setIcon(icon8)
        self.actionSlower.setObjectName("actionSlower")
        self.actionPlay = QtWidgets.QAction(MainWindow)
        self.actionPlay.setCheckable(True)
        self.actionPlay.setChecked(False)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/Resources/images/play.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon9.addPixmap(QtGui.QPixmap(":/Resources/images/pause.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionPlay.setIcon(icon9)
        self.actionPlay.setObjectName("actionPlay")
        self.actionSpectrogram = QtWidgets.QAction(MainWindow)
        self.actionSpectrogram.setCheckable(True)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(
            ":/Resources/images/spectr.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSpectrogram.setIcon(icon10)
        self.actionSpectrogram.setObjectName("actionSpectrogram")
        self.actionEqualizer = QtWidgets.QAction(MainWindow)
        self.actionEqualizer.setCheckable(True)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(
            ":/Resources/images/Equalizer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionEqualizer.setIcon(icon11)
        self.actionEqualizer.setObjectName("actionEqualizer")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionClose_Tab = QtWidgets.QAction(MainWindow)
        self.actionClose_Tab.setObjectName("actionClose_Tab")
        self.actionGraph_theme = QtWidgets.QAction(MainWindow)
        self.actionGraph_theme.setObjectName("actionGraph_theme")
        self.actionSpectrogram_theme = QtWidgets.QAction(MainWindow)
        self.actionSpectrogram_theme.setObjectName("actionSpectrogram_theme")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClose_Tab)
        self.menuFile.addAction(self.actionExit)
        self.menuScroll.addAction(self.actionLeft)
        self.menuScroll.addAction(self.actionRight)
        self.menuZoom.addAction(self.actionZoom_in)
        self.menuZoom.addAction(self.actionZoom_out)
        self.menuSpeed.addAction(self.actionFaster)
        self.menuSpeed.addAction(self.actionSlower)
        self.menuNavigation.addAction(self.menuZoom.menuAction())
        self.menuNavigation.addSeparator()
        self.menuNavigation.addAction(self.menuScroll.menuAction())
        self.menuNavigation.addSeparator()
        self.menuNavigation.addAction(self.actionPlay)
        self.menuNavigation.addAction(self.menuSpeed.menuAction())
        self.menuEdit.addAction(self.actionSpectrogram)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionEqualizer)
        self.menuEdit.addSeparator()
        self.menuTheme.addAction(self.actionGraph_theme)
        self.menuTheme.addAction(self.actionSpectrogram_theme)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuNavigation.menuAction())
        self.menubar.addAction(self.menuTheme.menuAction())
        self.toolBar.addAction(self.actionOpen)
        self.toolBar.addAction(self.actionSave)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionZoom_out)
        self.toolBar.addAction(self.actionZoom_in)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionSlower)
        self.toolBar.addAction(self.actionLeft)
        self.toolBar.addAction(self.actionPlay)
        self.toolBar.addAction(self.actionRight)
        self.toolBar.addAction(self.actionFaster)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionEqualizer)
        self.toolBar.addAction(self.actionSpectrogram)
                                                                        #Methods' Declaration
        getFile = Data.getFile
        retranslateUi = RetranslateUI.retranslateUi
        ShowSpectrogram = Spectrogram.ShowSpectrogram
        ShowEqualizer = Equalizer.ShowEqualizer
        ZoomIn = Navigations.Zoom_in
        ZoomOut = Navigations.Zoom_out
        ScrollLeft = Navigations.scroll_left
        ScrollRight = Navigations.scroll_right
                                                                        #Calling Methods
        retranslateUi(self, MainWindow)
        self.actionOpen.triggered.connect(lambda checked: getFile(self))
        self.actionSpectrogram.triggered.connect(
            lambda checked: ShowSpectrogram(self,MainWindow))
        self.actionEqualizer.triggered.connect(
            lambda checked: ShowEqualizer(self, MainWindow))
        self.actionZoom_in.triggered.connect(lambda checked: ZoomIn(self))
        self.actionZoom_out.triggered.connect(lambda checked: ZoomOut(self))
        self.actionLeft.triggered.connect(lambda checked: ScrollLeft(self))
        self.actionRight.triggered.connect(lambda checked: ScrollRight(self))
        

   


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
