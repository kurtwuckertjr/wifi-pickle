from core.loaders.models.PackagesUI import *

class License(QtGui.QTextEdit):
    def __init__(self,parent = None):
        super(License,self).__init__(parent)
        self.setReadOnly(True)
        self.setWindowTitle('License WiFI-Pickle GPL')
        self.setGeometry(0,0,300,300)
        self.center()
        self.setText(open('LICENSE','r').read())
    def center(self):
        frameGm = self.frameGeometry()
        centerPoint = QtGui.QDesktopWidget().availableGeometry().center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())

class ChangeLog(QtGui.QTextEdit):
    def __init__(self,parent = None):
        super(ChangeLog,self).__init__(parent)
        self.setMinimumHeight(240)
        self.setStyleSheet('''QWidget {
        color: #b1b1b1; background-color: #323232;}''')
        self.setText(open('CHANGELOG','r').read())
        self.setReadOnly(True)

class frmAbout(PickleModule):
    def __init__(self,author,emails,version,
        update,license,desc, parent = None):
        super(frmAbout, self).__init__(parent)
        self.author      = author
        self.emails      = emails
        self.version     = version
        self.update      = update
        self.desc        = QtGui.QLabel(desc[0]+'<br>')
        self.setWindowTitle("About WiFi-Pickle")
        self.Main = QtGui.QVBoxLayout()
        self.frm = QtGui.QFormLayout()
        self.setGeometry(0, 0, 350, 400)
        self.center()
        self.Qui_update()

    def center(self):
        frameGm = self.frameGeometry()
        centerPoint = QtGui.QDesktopWidget().availableGeometry().center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())

    def Qui_update(self):
        self.logoapp = QtGui.QLabel('')
        self.logoapp.setPixmap(QtGui.QPixmap('icons/pickle1.png').scaled(64,64))
        self.form = QtGui.QFormLayout()
        self.form2 = QtGui.QHBoxLayout()
        self.form.addRow(self.logoapp,QtGui.QLabel('<h2>WiFi-Pickle {}</h2>'.format(self.version)))
        self.tabwid = QtGui.QTabWidget(self)
        self.TabAbout = QtGui.QWidget(self)
        self.TabVersion = QtGui.QWidget(self)
        self.TabChangelog = QtGui.QWidget(self)
        self.btn_exit = QtGui.QPushButton("Close")
        self.btn_exit.setFixedWidth(90)
        self.btn_exit.setIcon(QtGui.QIcon('icons/cancel.png'))
        self.btn_exit.clicked.connect(self.close)

        self.formAbout = QtGui.QFormLayout()
        self.formVersion = QtGui.QFormLayout()
        self.formChange = QtGui.QFormLayout()

        # About section
        self.formAbout.addRow(self.desc)
        self.formAbout.addRow(QtGui.QLabel('Last Update:'))
        self.formAbout.addRow(QtGui.QLabel(self.update+'<br>'))
        self.formAbout.addRow(QtGui.QLabel('Feedback:'))
        self.formAbout.addRow(QtGui.QLabel(self.emails[0]))
        #self.formAbout.addRow(QtGui.QLabel(self.emails[1]+'<br>'))
        self.formAbout.addRow(QtGui.QLabel('Copyright 2018, '+self.author)) #[:-14]))
        self.gnu = QtGui.QLabel('<a href="link">License: GNU General Public License Version</a><br>')
        self.gnu.linkActivated.connect(self.link)
        self.formAbout.addRow(self.gnu)
        self.TabAbout.setLayout(self.formAbout)

        # Version Section
        self.formVersion.addRow(QtGui.QLabel('<strong>Version: {}</strong><br>'.format(self.version)))
        self.formVersion.addRow(QtGui.QLabel('Using:'))
        import platform
        python_version = platform.python_version()
        self.formVersion.addRow(QtGui.QLabel('''
        <ul>
          <li>QTVersion: {}</li>
          <li>Python: {}</li>
        </ul>'''.format(QtCore.QT_VERSION_STR,python_version)))
        self.TabVersion.setLayout(self.formVersion)

        # Changelog Section
        self.formChange.addRow(ChangeLog())
        self.TabChangelog.setLayout(self.formChange)

        # self.form.addRow(self.btn_exit)
        self.tabwid.addTab(self.TabAbout,'About')
        self.tabwid.addTab(self.TabVersion,'Version')
        self.tabwid.addTab(self.TabChangelog,'ChangeLog')
        self.form.addRow(self.tabwid)
        self.form2.addSpacing(240)
        self.form2.addWidget(self.btn_exit)
        self.form.addRow(self.form2)
        self.Main.addLayout(self.form)
        self.setLayout(self.Main)

    def link(self):
        self.formLicense = License()
        self.formLicense.show()
