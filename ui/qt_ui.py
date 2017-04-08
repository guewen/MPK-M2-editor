# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        # MainWindow.resize(1032, 764)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(8)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(-1, -1, -1, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.options = QtWidgets.QGridLayout()
        self.options.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.options.setContentsMargins(1, 5, 5, 5)
        self.options.setObjectName("options")
        self.getAllPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.getAllPushButton.setObjectName("getAllPushButton")
        self.getAllPushButton.clicked.connect(self.get_all_programmes)

        self.options.addWidget(self.getAllPushButton, 0, 1, 1, 1)
        self.getCurrentPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.getCurrentPushButton.setObjectName("getCurrentPushButton")
        self.getCurrentPushButton.clicked.connect(self.get_active_programme)

        self.options.addWidget(self.getCurrentPushButton, 0, 0, 1, 1)
        self.sendCurrentPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.sendCurrentPushButton.setObjectName("sendCurrentPushButton")
        self.options.addWidget(self.sendCurrentPushButton, 1, 0, 1, 1)
        self.sendAllPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.sendAllPushButton.setObjectName("sendAllPushButton")
        self.options.addWidget(self.sendAllPushButton, 1, 1, 1, 1)
        self.liveUpdateCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.liveUpdateCheckBox.setObjectName("liveUpdateCheckBox")
        self.options.addWidget(self.liveUpdateCheckBox, 0, 2, 1, 1)
        self.gridLayout.addLayout(self.options, 1, 0, 1, 1)
        self.programmes = QtWidgets.QTabWidget(self.centralwidget)
        self.programmes.setEnabled(True)
        self.programmes.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.programmes.setObjectName("programmes")

        # Programmes
        self.progs = []
        for prog_i in range(1, 5):
            prog = {}
            prog["prog1"] = QtWidgets.QWidget()
            prog["prog1"].setObjectName("prog%s" % prog_i)
            prog["gridLayout_2"] = QtWidgets.QGridLayout(prog["prog1"])
            prog["gridLayout_2"].setContentsMargins(0, 0, 0, 0)
            prog["gridLayout_2"].setObjectName("gridLayout_2")
            prog["knobsGroupBox"] = QtWidgets.QGroupBox(prog["prog1"])
            prog["knobsGroupBox"].setObjectName("knobsGroupBox")
            prog["gridLayout_5"] = QtWidgets.QGridLayout(prog["knobsGroupBox"])
            prog["gridLayout_5"].setContentsMargins(0, 0, 0, 0)
            prog["gridLayout_5"].setSpacing(0)
            prog["gridLayout_5"].setObjectName("gridLayout_5")

            # Knobs
            prog["knobs"] = []
            for knob_i in range(8):
                knob = {}
                knob["knobGroupBox"] = QtWidgets.QGroupBox(prog["knobsGroupBox"])
                knob["knobGroupBox"].setObjectName("knobGroupBox")
                knob["knobGridLayout"] = QtWidgets.QGridLayout(knob["knobGroupBox"])
                knob["knobGridLayout"].setContentsMargins(0, 0, 0, 0)
                knob["knobGridLayout"].setSpacing(0)
                knob["knobGridLayout"].setObjectName("knobGridLayout")
                knob["knobCCSpinBox"] = QtWidgets.QSpinBox(knob["knobGroupBox"])
                knob["knobCCSpinBox"].setMaximum(127)
                knob["knobCCSpinBox"].setObjectName("knobCCSpinBox")
                knob["knobGridLayout"].addWidget(knob["knobCCSpinBox"], 0, 1, 1, 1)
                knob["knobMinSpinBox"] = QtWidgets.QSpinBox(knob["knobGroupBox"])
                knob["knobMinSpinBox"].setMaximum(127)
                knob["knobMinSpinBox"].setObjectName("knobMinSpinBox")
                knob["knobGridLayout"].addWidget(knob["knobMinSpinBox"], 1, 1, 1, 1)
                knob["knobMinLabel"] = QtWidgets.QLabel(knob["knobGroupBox"])
                knob["knobMinLabel"].setObjectName("knobMinLabel")
                knob["knobGridLayout"].addWidget(knob["knobMinLabel"], 1, 0, 1, 1)
                knob["knobMaxSpinBox"] = QtWidgets.QSpinBox(knob["knobGroupBox"])
                knob["knobMaxSpinBox"].setMaximum(127)
                knob["knobMaxSpinBox"].setProperty("value", 127)
                knob["knobMaxSpinBox"].setObjectName("knobMaxSpinBox")
                knob["knobGridLayout"].addWidget(knob["knobMaxSpinBox"], 2, 1, 1, 1)
                knob["knobMaxLabel"] = QtWidgets.QLabel(knob["knobGroupBox"])
                knob["knobMaxLabel"].setObjectName("knobMaxLabel")
                knob["knobGridLayout"].addWidget(knob["knobMaxLabel"], 2, 0, 1, 1)
                knob["knobCCLabel"] = QtWidgets.QLabel(knob["knobGroupBox"])
                knob["knobCCLabel"].setObjectName("knobCCLabel")
                knob["knobGridLayout"].addWidget(knob["knobCCLabel"], 0, 0, 1, 1)

                prog["gridLayout_5"].addWidget(knob["knobGroupBox"], knob_i/4+1, knob_i%4, 1, 1)
                prog["knobs"].append(knob)
            prog["gridLayout_2"].addWidget(prog["knobsGroupBox"], 0, 1, 1, 1)

            prog["miscLayout"] = QtWidgets.QHBoxLayout()
            prog["miscLayout"].setObjectName("miscLayout")
            prog["joystickLayout"] = QtWidgets.QGroupBox(prog["prog1"])
            prog["joystickLayout"].setObjectName("joystickLayout")
            prog["verticalLayout"] = QtWidgets.QVBoxLayout(prog["joystickLayout"])
            prog["verticalLayout"].setObjectName("verticalLayout")
            prog["jsXAxisLayout"] = QtWidgets.QHBoxLayout()
            prog["jsXAxisLayout"].setObjectName("jsXAxisLayout")
            prog["jsXAxisLabel"] = QtWidgets.QLabel(prog["joystickLayout"])
            prog["jsXAxisLabel"].setObjectName("jsXAxisLabel")
            prog["jsXAxisLayout"].addWidget(prog["jsXAxisLabel"])
            prog["jsXAxisLayout_2"] = QtWidgets.QVBoxLayout()
            prog["jsXAxisLayout_2"].setSpacing(0)
            prog["jsXAxisLayout_2"].setObjectName("jsXAxisLayout_2")
            prog["jsXAxisComboBox"] = QtWidgets.QComboBox(prog["joystickLayout"])
            prog["jsXAxisComboBox"].setObjectName("jsXAxisComboBox")
            prog["jsXAxisComboBox"].addItem("")
            prog["jsXAxisComboBox"].addItem("")
            prog["jsXAxisComboBox"].addItem("")
            prog["jsXAxisLayout_2"].addWidget(prog["jsXAxisComboBox"])
            prog["jsXLeftWidget"] = QtWidgets.QWidget(prog["joystickLayout"])
            prog["jsXLeftWidget"].setEnabled(False)
            prog["jsXLeftWidget"].setObjectName("jsXLeftWidget")
            prog["gridLayout_3"] = QtWidgets.QGridLayout(prog["jsXLeftWidget"])
            prog["gridLayout_3"].setContentsMargins(0, 0, 0, 0)
            prog["gridLayout_3"].setSpacing(0)
            prog["gridLayout_3"].setObjectName("gridLayout_3")
            prog["jsXLeftLabel"] = QtWidgets.QLabel(prog["jsXLeftWidget"])
            prog["jsXLeftLabel"].setObjectName("jsXLeftLabel")
            prog["gridLayout_3"].addWidget(prog["jsXLeftLabel"], 0, 0, 1, 1)
            prog["jsXLeftLabelSpinBox"] = QtWidgets.QSpinBox(prog["jsXLeftWidget"])
            prog["jsXLeftLabelSpinBox"].setMaximum(127)
            prog["jsXLeftLabelSpinBox"].setObjectName("jsXLeftLabelSpinBox")
            prog["gridLayout_3"].addWidget(prog["jsXLeftLabelSpinBox"], 0, 1, 1, 1)
            prog["jsXRightLabel"] = QtWidgets.QLabel(prog["jsXLeftWidget"])
            prog["jsXRightLabel"].setObjectName("jsXRightLabel")
            prog["gridLayout_3"].addWidget(prog["jsXRightLabel"], 1, 0, 1, 1)
            prog["jsXRightSpinBox"] = QtWidgets.QSpinBox(prog["jsXLeftWidget"])
            prog["jsXRightSpinBox"].setMaximum(127)
            prog["jsXRightSpinBox"].setObjectName("jsXRightSpinBox")
            prog["gridLayout_3"].addWidget(prog["jsXRightSpinBox"], 1, 1, 1, 1)
            prog["jsXLeftLabelSpinBox"].raise_()
            prog["jsXRightSpinBox"].raise_()
            prog["jsXLeftLabel"].raise_()
            prog["jsXRightLabel"].raise_()
            prog["jsXAxisLayout_2"].addWidget(prog["jsXLeftWidget"])
            prog["jsXAxisLayout"].addLayout(prog["jsXAxisLayout_2"])
            prog["verticalLayout"].addLayout(prog["jsXAxisLayout"])
            prog["jsYAxisLayout"] = QtWidgets.QHBoxLayout()
            prog["jsYAxisLayout"].setObjectName("jsYAxisLayout")
            prog["jsYAxisLabel"] = QtWidgets.QLabel(prog["joystickLayout"])
            prog["jsYAxisLabel"].setObjectName("jsYAxisLabel")
            prog["jsYAxisLayout"].addWidget(prog["jsYAxisLabel"])
            prog["jsYAxisLayout_2"] = QtWidgets.QVBoxLayout()
            prog["jsYAxisLayout_2"].setSpacing(0)
            prog["jsYAxisLayout_2"].setObjectName("jsYAxisLayout_2")
            prog["jsYAxisComboBox"] = QtWidgets.QComboBox(prog["joystickLayout"])
            prog["jsYAxisComboBox"].setObjectName("jsYAxisComboBox")
            prog["jsYAxisComboBox"].addItem("")
            prog["jsYAxisComboBox"].addItem("")
            prog["jsYAxisComboBox"].addItem("")
            prog["jsYAxisLayout_2"].addWidget(prog["jsYAxisComboBox"])
            prog["jsYWidget"] = QtWidgets.QWidget(prog["joystickLayout"])
            prog["jsYWidget"].setEnabled(False)
            prog["jsYWidget"].setObjectName("jsYWidget")
            prog["gridLayout_7"] = QtWidgets.QGridLayout(prog["jsYWidget"])
            prog["gridLayout_7"].setContentsMargins(0, 0, 0, 0)
            prog["gridLayout_7"].setSpacing(0)
            prog["gridLayout_7"].setObjectName("gridLayout_7")
            prog["jsYUpLabel"] = QtWidgets.QLabel(prog["jsYWidget"])
            prog["jsYUpLabel"].setObjectName("jsYUpLabel")
            prog["gridLayout_7"].addWidget(prog["jsYUpLabel"], 0, 0, 1, 1)
            prog["jsYUpSpinBox"] = QtWidgets.QSpinBox(prog["jsYWidget"])
            prog["jsYUpSpinBox"].setMaximum(127)
            prog["jsYUpSpinBox"].setObjectName("jsYUpSpinBox")
            prog["gridLayout_7"].addWidget(prog["jsYUpSpinBox"], 0, 1, 1, 1)
            prog["jsYDownLabel"] = QtWidgets.QLabel(prog["jsYWidget"])
            prog["jsYDownLabel"].setObjectName("jsYDownLabel")
            prog["gridLayout_7"].addWidget(prog["jsYDownLabel"], 1, 0, 1, 1)
            prog["jsYDownSpinBox"] = QtWidgets.QSpinBox(prog["jsYWidget"])
            prog["jsYDownSpinBox"].setMaximum(127)
            prog["jsYDownSpinBox"].setObjectName("jsYDownSpinBox")
            prog["gridLayout_7"].addWidget(prog["jsYDownSpinBox"], 1, 1, 1, 1)
            prog["jsYAxisLayout_2"].addWidget(prog["jsYWidget"])
            prog["jsYAxisLayout"].addLayout(prog["jsYAxisLayout_2"])
            prog["verticalLayout"].addLayout(prog["jsYAxisLayout"])
            prog["miscLayout"].addWidget(prog["joystickLayout"])
            prog["arpegGroupBox"] = QtWidgets.QGroupBox(prog["prog1"])
            prog["arpegGroupBox"].setObjectName("arpegGroupBox")
            prog["verticalLayout_3"] = QtWidgets.QVBoxLayout(prog["arpegGroupBox"])
            prog["verticalLayout_3"].setContentsMargins(0, 0, 0, 0)
            prog["verticalLayout_3"].setSpacing(0)
            prog["verticalLayout_3"].setObjectName("verticalLayout_3")
            prog["tempoLayout"] = QtWidgets.QHBoxLayout()
            prog["tempoLayout"].setObjectName("tempoLayout")
            prog["tempoLabel"] = QtWidgets.QLabel(prog["arpegGroupBox"])
            prog["tempoLabel"].setObjectName("tempoLabel")
            prog["tempoLayout"].addWidget(prog["tempoLabel"])
            prog["tempoSpinBox"] = QtWidgets.QSpinBox(prog["arpegGroupBox"])
            prog["tempoSpinBox"].setMinimum(30)
            prog["tempoSpinBox"].setMaximum(240)
            prog["tempoSpinBox"].setProperty("value", 120)
            prog["tempoSpinBox"].setObjectName("tempoSpinBox")
            prog["tempoLayout"].addWidget(prog["tempoSpinBox"])
            prog["verticalLayout_3"].addLayout(prog["tempoLayout"])
            prog["timeDivLayout"] = QtWidgets.QHBoxLayout()
            prog["timeDivLayout"].setObjectName("timeDivLayout")
            prog["timeDivLabel"] = QtWidgets.QLabel(prog["arpegGroupBox"])
            prog["timeDivLabel"].setObjectName("timeDivLabel")
            prog["timeDivLayout"].addWidget(prog["timeDivLabel"])
            prog["timeDivComboBox"] = QtWidgets.QComboBox(prog["arpegGroupBox"])
            prog["timeDivComboBox"].setObjectName("timeDivComboBox")
            prog["timeDivComboBox"].addItem("")
            prog["timeDivComboBox"].addItem("")
            prog["timeDivComboBox"].addItem("")
            prog["timeDivComboBox"].addItem("")
            prog["timeDivComboBox"].addItem("")
            prog["timeDivComboBox"].addItem("")
            prog["timeDivComboBox"].addItem("")
            prog["timeDivComboBox"].addItem("")
            prog["timeDivLayout"].addWidget(prog["timeDivComboBox"])
            prog["verticalLayout_3"].addLayout(prog["timeDivLayout"])
            prog["swingLayout"] = QtWidgets.QHBoxLayout()
            prog["swingLayout"].setObjectName("swingLayout")
            prog["swingLabel"] = QtWidgets.QLabel(prog["arpegGroupBox"])
            prog["swingLabel"].setObjectName("swingLabel")
            prog["swingLayout"].addWidget(prog["swingLabel"])
            prog["swingComboBox"] = QtWidgets.QComboBox(prog["arpegGroupBox"])
            prog["swingComboBox"].setObjectName("swingComboBox")
            prog["swingComboBox"].addItem("")
            prog["swingComboBox"].addItem("")
            prog["swingComboBox"].addItem("")
            prog["swingComboBox"].addItem("")
            prog["swingComboBox"].addItem("")
            prog["swingComboBox"].addItem("")
            prog["swingLayout"].addWidget(prog["swingComboBox"])
            prog["verticalLayout_3"].addLayout(prog["swingLayout"])
            prog["arpOctaveLayout"] = QtWidgets.QHBoxLayout()
            prog["arpOctaveLayout"].setObjectName("arpOctaveLayout")
            prog["arpOctaveLabel"] = QtWidgets.QLabel(prog["arpegGroupBox"])
            prog["arpOctaveLabel"].setObjectName("arpOctaveLabel")
            prog["arpOctaveLayout"].addWidget(prog["arpOctaveLabel"])
            prog["arpOctaveSpinBox"] = QtWidgets.QSpinBox(prog["arpegGroupBox"])
            prog["arpOctaveSpinBox"].setMinimum(0)
            prog["arpOctaveSpinBox"].setMaximum(4)
            prog["arpOctaveSpinBox"].setProperty("value", 0)
            prog["arpOctaveSpinBox"].setObjectName("arpOctaveSpinBox")
            prog["arpOctaveLayout"].addWidget(prog["arpOctaveSpinBox"])
            prog["verticalLayout_3"].addLayout(prog["arpOctaveLayout"])
            prog["modeLayout"] = QtWidgets.QHBoxLayout()
            prog["modeLayout"].setObjectName("modeLayout")
            prog["modeLabel"] = QtWidgets.QLabel(prog["arpegGroupBox"])
            prog["modeLabel"].setObjectName("modeLabel")
            prog["modeLayout"].addWidget(prog["modeLabel"])
            prog["modeComboBox"] = QtWidgets.QComboBox(prog["arpegGroupBox"])
            prog["modeComboBox"].setObjectName("modeComboBox")
            prog["modeComboBox"].addItem("")
            prog["modeComboBox"].addItem("")
            prog["modeComboBox"].addItem("")
            prog["modeComboBox"].addItem("")
            prog["modeComboBox"].addItem("")
            prog["modeComboBox"].addItem("")
            prog["modeLayout"].addWidget(prog["modeComboBox"])
            prog["verticalLayout_3"].addLayout(prog["modeLayout"])
            prog["tempoTapsLayout"] = QtWidgets.QHBoxLayout()
            prog["tempoTapsLayout"].setObjectName("tempoTapsLayout")
            prog["tempoTapsLabel"] = QtWidgets.QLabel(prog["arpegGroupBox"])
            prog["tempoTapsLabel"].setObjectName("tempoTapsLabel")
            prog["tempoTapsLayout"].addWidget(prog["tempoTapsLabel"])
            prog["tempoTapsSpinBox"] = QtWidgets.QSpinBox(prog["arpegGroupBox"])
            prog["tempoTapsSpinBox"].setMinimum(2)
            prog["tempoTapsSpinBox"].setMaximum(4)
            prog["tempoTapsSpinBox"].setProperty("value", 2)
            prog["tempoTapsSpinBox"].setObjectName("tempoTapsSpinBox")
            prog["tempoTapsLayout"].addWidget(prog["tempoTapsSpinBox"])
            prog["verticalLayout_3"].addLayout(prog["tempoTapsLayout"])
            prog["clockLayout"] = QtWidgets.QHBoxLayout()
            prog["clockLayout"].setObjectName("clockLayout")
            prog["clockLabel"] = QtWidgets.QLabel(prog["arpegGroupBox"])
            prog["clockLabel"].setObjectName("clockLabel")
            prog["clockLayout"].addWidget(prog["clockLabel"])
            prog["clockComboBox"] = QtWidgets.QComboBox(prog["arpegGroupBox"])
            prog["clockComboBox"].setObjectName("clockComboBox")
            prog["clockComboBox"].addItem("")
            prog["clockComboBox"].addItem("")
            prog["clockLayout"].addWidget(prog["clockComboBox"])
            prog["verticalLayout_3"].addLayout(prog["clockLayout"])
            prog["arpCheckBox"] = QtWidgets.QCheckBox(prog["arpegGroupBox"])
            prog["arpCheckBox"].setObjectName("arpCheckBox")
            prog["verticalLayout_3"].addWidget(prog["arpCheckBox"])
            prog["miscLayout"].addWidget(prog["arpegGroupBox"])
            prog["chanKeysLayout"] = QtWidgets.QVBoxLayout()
            prog["chanKeysLayout"].setObjectName("chanKeysLayout")
            prog["channelsGroupBox"] = QtWidgets.QGroupBox(prog["prog1"])
            prog["channelsGroupBox"].setObjectName("channelsGroupBox")
            prog["verticalLayout_5"] = QtWidgets.QVBoxLayout(prog["channelsGroupBox"])
            prog["verticalLayout_5"].setObjectName("verticalLayout_5")
            prog["padLayout"] = QtWidgets.QHBoxLayout()
            prog["padLayout"].setObjectName("padLayout")
            prog["padLabel"] = QtWidgets.QLabel(prog["channelsGroupBox"])
            prog["padLabel"].setObjectName("padLabel")
            prog["padLayout"].addWidget(prog["padLabel"])
            prog["padSpinBox"] = QtWidgets.QSpinBox(prog["channelsGroupBox"])
            prog["padSpinBox"].setMinimum(1)
            prog["padSpinBox"].setMaximum(16)
            prog["padSpinBox"].setObjectName("padSpinBox")
            prog["padLayout"].addWidget(prog["padSpinBox"])
            prog["verticalLayout_5"].addLayout(prog["padLayout"])
            prog["keysLayout"] = QtWidgets.QHBoxLayout()
            prog["keysLayout"].setObjectName("keysLayout")
            prog["keysLabel"] = QtWidgets.QLabel(prog["channelsGroupBox"])
            prog["keysLabel"].setObjectName("keysLabel")
            prog["keysLayout"].addWidget(prog["keysLabel"])
            prog["keySpinBox"] = QtWidgets.QSpinBox(prog["channelsGroupBox"])
            prog["keySpinBox"].setMinimum(1)
            prog["keySpinBox"].setMaximum(16)
            prog["keySpinBox"].setObjectName("keySpinBox")
            prog["keysLayout"].addWidget(prog["keySpinBox"])
            prog["verticalLayout_5"].addLayout(prog["keysLayout"])
            prog["chanKeysLayout"].addWidget(prog["channelsGroupBox"])
            prog["keyboardGroupBox"] = QtWidgets.QGroupBox(prog["prog1"])
            prog["keyboardGroupBox"].setObjectName("keyboardGroupBox")
            prog["verticalLayout_4"] = QtWidgets.QVBoxLayout(prog["keyboardGroupBox"])
            prog["verticalLayout_4"].setObjectName("verticalLayout_4")
            prog["transposeLayout"] = QtWidgets.QHBoxLayout()
            prog["transposeLayout"].setObjectName("transposeLayout")
            prog["transposeLabel"] = QtWidgets.QLabel(prog["keyboardGroupBox"])
            prog["transposeLabel"].setObjectName("transposeLabel")
            prog["transposeLayout"].addWidget(prog["transposeLabel"])
            prog["transposeSpinBox"] = QtWidgets.QSpinBox(prog["keyboardGroupBox"])
            prog["transposeSpinBox"].setMinimum(-12)
            prog["transposeSpinBox"].setMaximum(12)
            prog["transposeSpinBox"].setObjectName("transposeSpinBox")
            prog["transposeLayout"].addWidget(prog["transposeSpinBox"])
            prog["verticalLayout_4"].addLayout(prog["transposeLayout"])
            prog["octaveLayout"] = QtWidgets.QHBoxLayout()
            prog["octaveLayout"].setObjectName("octaveLayout")
            prog["octaveLabel"] = QtWidgets.QLabel(prog["keyboardGroupBox"])
            prog["octaveLabel"].setObjectName("octaveLabel")
            prog["octaveLayout"].addWidget(prog["octaveLabel"])
            prog["octaveSpinBox"] = QtWidgets.QSpinBox(prog["keyboardGroupBox"])
            prog["octaveSpinBox"].setMinimum(-4)
            prog["octaveSpinBox"].setMaximum(4)
            prog["octaveSpinBox"].setObjectName("octaveSpinBox")
            prog["octaveLayout"].addWidget(prog["octaveSpinBox"])
            prog["verticalLayout_4"].addLayout(prog["octaveLayout"])
            prog["chanKeysLayout"].addWidget(prog["keyboardGroupBox"])
            prog["miscLayout"].addLayout(prog["chanKeysLayout"])
            prog["gridLayout_2"].addLayout(prog["miscLayout"], 1, 1, 1, 1)

            # Banks
            prog["banks"] = []
            for bank_i in range(2):
                bank = {}
                bank["bankGroupBox"] = QtWidgets.QGroupBox(prog["prog1"])
                bank["bankGroupBox"].setObjectName("bankAGroupBox")
                bank["gridLayout_6"] = QtWidgets.QGridLayout(bank["bankGroupBox"])
                bank["gridLayout_6"].setContentsMargins(2, 2, 2, 2)
                bank["gridLayout_6"].setSpacing(2)
                bank["gridLayout_6"].setObjectName("gridLayout_6")

                # Pads
                bank["pads"] = []
                for pad_i in range(8):
                    pad = {}
                    pad["padGroupBox"] = QtWidgets.QGroupBox(bank["bankGroupBox"])
                    pad["padGroupBox"].setObjectName("padGroupBox")
                    pad["gridLayout_43"] = QtWidgets.QGridLayout(pad["padGroupBox"])
                    pad["gridLayout_43"].setContentsMargins(0, 0, 0, 0)
                    pad["gridLayout_43"].setSpacing(0)
                    pad["gridLayout_43"].setObjectName("gridLayout_43")
                    pad["padNoteLayout"] = QtWidgets.QHBoxLayout()
                    pad["padNoteLayout"].setObjectName("padNoteLayout")
                    pad["padNoteLabel"] = QtWidgets.QLabel(pad["padGroupBox"])
                    pad["padNoteLabel"].setObjectName("padNoteLabel")
                    pad["padNoteLayout"].addWidget(pad["padNoteLabel"])
                    pad["padNoteComboBox"] = QtWidgets.QComboBox(pad["padGroupBox"])
                    pad["padNoteComboBox"].setObjectName("padNoteComboBox")
                    pad["padNoteComboBox"].addItem("")
                    pad["padNoteComboBox"].addItem("")
                    pad["padNoteComboBox"].addItem("")
                    pad["padNoteComboBox"].addItem("")
                    pad["padNoteComboBox"].addItem("")
                    pad["padNoteComboBox"].addItem("")
                    pad["padNoteComboBox"].addItem("")
                    pad["padNoteComboBox"].addItem("")
                    pad["padNoteComboBox"].addItem("")
                    pad["padNoteComboBox"].addItem("")
                    pad["padNoteComboBox"].addItem("")
                    pad["padNoteComboBox"].addItem("")
                    pad["padNoteLayout"].addWidget(pad["padNoteComboBox"])
                    pad["padNoteSpinBox"] = QtWidgets.QSpinBox(pad["padGroupBox"])
                    pad["padNoteSpinBox"].setMinimum(-1)
                    pad["padNoteSpinBox"].setMaximum(9)
                    pad["padNoteSpinBox"].setProperty("value", 4)
                    pad["padNoteSpinBox"].setObjectName("padNoteSpinBox")
                    pad["padNoteLayout"].addWidget(pad["padNoteSpinBox"])
                    pad["gridLayout_43"].addLayout(pad["padNoteLayout"], 0, 0, 1, 1)
                    pad["padCCLayout"] = QtWidgets.QHBoxLayout()
                    pad["padCCLayout"].setObjectName("padCCLayout")
                    pad["padCCLabel"] = QtWidgets.QLabel(pad["padGroupBox"])
                    pad["padCCLabel"].setObjectName("padCCLabel")
                    pad["padCCLayout"].addWidget(pad["padCCLabel"])
                    pad["padCCSpinBox"] = QtWidgets.QSpinBox(pad["padGroupBox"])
                    pad["padCCSpinBox"].setMaximum(127)
                    pad["padCCSpinBox"].setProperty("value", 0)
                    pad["padCCSpinBox"].setObjectName("padCCSpinBox")
                    pad["padCCLayout"].addWidget(pad["padCCSpinBox"])
                    pad["gridLayout_43"].addLayout(pad["padCCLayout"], 2, 0, 1, 1)
                    pad["padPCLayout"] = QtWidgets.QHBoxLayout()
                    pad["padPCLayout"].setObjectName("padPCLayout")
                    pad["padPCLabel"] = QtWidgets.QLabel(pad["padGroupBox"])
                    pad["padPCLabel"].setObjectName("padPCLabel")
                    pad["padPCLayout"].addWidget(pad["padPCLabel"])
                    pad["padPCSpinBox"] = QtWidgets.QSpinBox(pad["padGroupBox"])
                    pad["padPCSpinBox"].setMaximum(127)
                    pad["padPCSpinBox"].setProperty("value", 0)
                    pad["padPCSpinBox"].setObjectName("padPCSpinBox")
                    pad["padPCLayout"].addWidget(pad["padPCSpinBox"])
                    pad["gridLayout_43"].addLayout(pad["padPCLayout"], 3, 0, 1, 1)
                    pad["padTypeComboBox"] = QtWidgets.QComboBox(pad["padGroupBox"])
                    pad["padTypeComboBox"].setObjectName("padTypeComboBox")
                    pad["padTypeComboBox"].addItem("")
                    pad["padTypeComboBox"].addItem("")
                    pad["gridLayout_43"].addWidget(pad["padTypeComboBox"], 4, 0, 1, 1)
                    bank["gridLayout_6"].addWidget(pad["padGroupBox"], 1-(pad_i//4), pad_i % 4, 1, 1)
                    bank["pads"].append(pad)
                prog["gridLayout_2"].addWidget(bank["bankGroupBox"], bank_i%2, 0, 1, 1)
                prog["banks"].append(bank)
            self.programmes.addTab(prog["prog1"], "")
            self.progs.append(prog)

        self.gridLayout.addWidget(self.programmes, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1032, 18))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuFile_2 = QtWidgets.QMenu(self.menubar)
        self.menuFile_2.setObjectName("menuFile_2")
        MainWindow.setMenuBar(self.menubar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_as = QtWidgets.QAction(MainWindow)
        self.actionSave_as.setObjectName("actionSave_as")
        self.actionSave_as_2 = QtWidgets.QAction(MainWindow)
        self.actionSave_as_2.setObjectName("actionSave_as_2")
        self.actionFactory_preset = QtWidgets.QAction(MainWindow)
        self.actionFactory_preset.setObjectName("actionFactory_preset")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_as_2)
        self.menuFile.addAction(self.actionFactory_preset)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuFile_2.menuAction())

        self.retranslateUi(MainWindow)
        self.programmes.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def get_active_tab_index(self):
        return self.programmes.currentIndex()

    def fill_active_tab(self, config):
        p_i = config[7]-1
        # for i, k in enumerate(self.midi_config.keys()):
        prog = self.progs[p_i]
        for k_i, knob in enumerate(prog["knobs"]):
            knob["knobCCSpinBox"].setValue(config[91 + k_i*3])
            knob["knobMinSpinBox"].setValue(config[91 + 1 + k_i*3])
            knob["knobMaxSpinBox"].setValue(config[91 + 2 + k_i*3])

        for b_i, bank in enumerate(prog["banks"]):
            for pad_i, pad in enumerate(bank["pads"]):
                note = config[27 + b_i*4*8 + pad_i*4]
                print(note)
                pad["padNoteComboBox"].setCurrentIndex(note % 12)
                pad["padNoteSpinBox"].setValue(note // 12 - 1)
                pad["padPCSpinBox"].setValue(config[27 + b_i*4*8 + 1 + pad_i*4])
                pad["padCCSpinBox"].setValue(config[27 + b_i*4*8 + 2 + pad_i*4])
                # pad_type = "Toggle" if config[27 + b_i*4*8 + 3 + pad_i*4] else "Momentary"
                pad["padTypeComboBox"].setCurrentIndex(config[27 + b_i*4*8 + 3 + pad_i*4])

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.getAllPushButton.setText(_translate("MainWindow", "Get all"))
        self.getCurrentPushButton.setText(_translate("MainWindow", "Get current"))
        self.sendCurrentPushButton.setText(_translate("MainWindow", "Send current"))
        self.sendAllPushButton.setText(_translate("MainWindow", "Send all"))
        self.liveUpdateCheckBox.setText(_translate("MainWindow", "Live update"))
        for p_i, prog in enumerate(self.progs):
            prog["knobsGroupBox"].setTitle(_translate("MainWindow", "Knobs"))
            for k_i, knob in enumerate(prog["knobs"]):
                knob["knobGroupBox"].setTitle(_translate("MainWindow", "Knob %s" % (k_i+1)))
                knob["knobMinLabel"].setText(_translate("MainWindow", "Min"))
                knob["knobMaxLabel"].setText(_translate("MainWindow", "Max"))
                knob["knobCCLabel"].setText(_translate("MainWindow", "CC"))
            prog["joystickLayout"].setTitle(_translate("MainWindow", "Joystick"))
            prog["jsXAxisLabel"].setText(_translate("MainWindow", "X Axis"))
            prog["jsXAxisComboBox"].setItemText(0, _translate("MainWindow", "Pitchbend"))
            prog["jsXAxisComboBox"].setItemText(1, _translate("MainWindow", "CC 1"))
            prog["jsXAxisComboBox"].setItemText(2, _translate("MainWindow", "CC 2"))
            prog["jsXLeftLabel"].setText(_translate("MainWindow", "Left"))
            prog["jsXRightLabel"].setText(_translate("MainWindow", "Right"))
            prog["jsYAxisLabel"].setText(_translate("MainWindow", "Y Axis"))
            prog["jsYAxisComboBox"].setItemText(0, _translate("MainWindow", "Pitchbend"))
            prog["jsYAxisComboBox"].setItemText(1, _translate("MainWindow", "CC 1"))
            prog["jsYAxisComboBox"].setItemText(2, _translate("MainWindow", "CC 2"))
            prog["jsYUpLabel"].setText(_translate("MainWindow", "Up"))
            prog["jsYDownLabel"].setText(_translate("MainWindow", "Down"))
            prog["arpegGroupBox"].setTitle(_translate("MainWindow", "Arpeggiator"))
            prog["tempoLabel"].setText(_translate("MainWindow", "Tempo"))
            prog["timeDivLabel"].setText(_translate("MainWindow", "Time div"))
            prog["timeDivComboBox"].setItemText(0, _translate("MainWindow", "1/4"))
            prog["timeDivComboBox"].setItemText(1, _translate("MainWindow", "1/4T"))
            prog["timeDivComboBox"].setItemText(2, _translate("MainWindow", "1/8"))
            prog["timeDivComboBox"].setItemText(3, _translate("MainWindow", "1/8T"))
            prog["timeDivComboBox"].setItemText(4, _translate("MainWindow", "1/16"))
            prog["timeDivComboBox"].setItemText(5, _translate("MainWindow", "1/16T"))
            prog["timeDivComboBox"].setItemText(6, _translate("MainWindow", "1/32"))
            prog["timeDivComboBox"].setItemText(7, _translate("MainWindow", "1/32T"))
            prog["swingLabel"].setText(_translate("MainWindow", "Swing"))
            prog["swingComboBox"].setItemText(0, _translate("MainWindow", "50%"))
            prog["swingComboBox"].setItemText(1, _translate("MainWindow", "55%"))
            prog["swingComboBox"].setItemText(2, _translate("MainWindow", "57%"))
            prog["swingComboBox"].setItemText(3, _translate("MainWindow", "59%"))
            prog["swingComboBox"].setItemText(4, _translate("MainWindow", "61%"))
            prog["swingComboBox"].setItemText(5, _translate("MainWindow", "64%"))
            prog["arpOctaveLabel"].setText(_translate("MainWindow", "Octave"))
            prog["modeLabel"].setText(_translate("MainWindow", "Mode"))
            prog["modeComboBox"].setItemText(0, _translate("MainWindow", "UP"))
            prog["modeComboBox"].setItemText(1, _translate("MainWindow", "DOWN"))
            prog["modeComboBox"].setItemText(2, _translate("MainWindow", "EXCLUSIVE"))
            prog["modeComboBox"].setItemText(3, _translate("MainWindow", "INCLUSIVE"))
            prog["modeComboBox"].setItemText(4, _translate("MainWindow", "ORDER"))
            prog["modeComboBox"].setItemText(5, _translate("MainWindow", "RANDOM"))
            prog["tempoTapsLabel"].setText(_translate("MainWindow", "Tempo taps"))
            prog["clockLabel"].setText(_translate("MainWindow", "Clock"))
            prog["clockComboBox"].setItemText(0, _translate("MainWindow", "Internal"))
            prog["clockComboBox"].setItemText(1, _translate("MainWindow", "External"))
            prog["arpCheckBox"].setToolTip(_translate("MainWindow", "<html><head/><body><p>Activate arpeggiator</p></body></html>"))
            prog["arpCheckBox"].setText(_translate("MainWindow", "ON/OFF"))
            prog["channelsGroupBox"].setTitle(_translate("MainWindow", "Channels"))
            prog["padLabel"].setText(_translate("MainWindow", "Pad"))
            prog["keysLabel"].setText(_translate("MainWindow", "Keys/CC"))
            prog["keyboardGroupBox"].setTitle(_translate("MainWindow", "Keyboard"))
            prog["transposeLabel"].setText(_translate("MainWindow", "Transpose"))
            prog["octaveLabel"].setText(_translate("MainWindow", "Octave"))
            for b_i, bank in enumerate(prog["banks"]):
                bank_name = "Bank B" if b_i else "Bank A"
                bank["bankGroupBox"].setTitle(_translate("MainWindow", bank_name))
                for pa_i, pad in enumerate(bank["pads"]):
                    pad["padGroupBox"].setTitle(_translate("MainWindow", "Pad %s"%(pa_i+1)))
                    pad["padCCLabel"].setText(_translate("MainWindow", "CC"))
                    pad["padTypeComboBox"].setItemText(0, _translate("MainWindow", "Toggle"))
                    pad["padTypeComboBox"].setItemText(1, _translate("MainWindow", "Momentary"))
                    pad["padNoteLabel"].setText(_translate("MainWindow", "Note"))
                    pad["padNoteComboBox"].setItemText(0, _translate("MainWindow", "C"))
                    pad["padNoteComboBox"].setItemText(1, _translate("MainWindow", "C#"))
                    pad["padNoteComboBox"].setItemText(2, _translate("MainWindow", "D"))
                    pad["padNoteComboBox"].setItemText(3, _translate("MainWindow", "D#"))
                    pad["padNoteComboBox"].setItemText(4, _translate("MainWindow", "E"))
                    pad["padNoteComboBox"].setItemText(5, _translate("MainWindow", "F"))
                    pad["padNoteComboBox"].setItemText(6, _translate("MainWindow", "F#"))
                    pad["padNoteComboBox"].setItemText(7, _translate("MainWindow", "G"))
                    pad["padNoteComboBox"].setItemText(8, _translate("MainWindow", "G#"))
                    pad["padNoteComboBox"].setItemText(9, _translate("MainWindow", "A"))
                    pad["padNoteComboBox"].setItemText(10, _translate("MainWindow", "A#"))
                    pad["padNoteComboBox"].setItemText(11, _translate("MainWindow", "B"))
                    pad["padPCLabel"].setText(_translate("MainWindow", "PC"))
            self.programmes.setTabText(self.programmes.indexOf(prog["prog1"]), _translate("MainWindow", "PROG %s"%(p_i+1)))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuFile_2.setTitle(_translate("MainWindow", "Edit"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave_as.setText(_translate("MainWindow", "Save as..."))
        self.actionSave_as_2.setText(_translate("MainWindow", "Save as..."))
        self.actionFactory_preset.setText(_translate("MainWindow", "Factory preset"))
