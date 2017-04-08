#!/usr/bin/env python3

# TODO
## get programmes
## send programmes
##     single
#     all
# get ram
# send ram
# interface
#     tabs for progs
#     autofill
# load/save config
#     single program
#     multi  programs
#     .mk2
#     mk1
#     human readable
# live update
# factory reset
# package
# PyPI?

import sys
import rtmidi
import time
from collections import OrderedDict
from pprint import pprint

from PyQt5 import QtCore, QtGui, QtWidgets
from ui.qt_ui import Ui_MainWindow

# [240, 71, 0, 38, 102, 0, 1, 1, 247]


class Akai_MPK_Mini(Ui_MainWindow):

    GET_CONFIG = [240, 71, 0, 38, 102, 0, 1, 1, 247]

    def __init__(self):
        self.midi_config = OrderedDict((
            ("sysex_0", 240),  # [240]
            ("sysex_1", 71),  # [71]
            ("sysex_2", 0),  # [0]
            ("sysex_3", 38),  # [38]
            ("sysex_4", 103),  # [103]
            ("sysex_5", 0),  # [0]
            ("sysex_6", 109),  # [109]

            ("programme", 1),  # [1,4]

            ("pad_channel", 15),  # [0,15]
            ("key_channel", 14),  # [0,15]

            ("key_octave", 3),  # [0,8] (-4,4)

            ("arp_on", 1),  # [0=OFF; 1=ON] no effect on programmes...?
            ("arp_mode", 5),  # [0=UP; 1=DOWN; 2=EXCLUSIVE; 3=INCLUSIVE; 4=ORDER; 5=RANDOM]
            ("arp_time", 5),  # div [0=1/4; 1=1/4T;  2=1/8;  3=1/8T;  4=1/16;  5=1/16T;  6=1/32;  7=1/32T]
            ("arp_clock", 0),  # [0=INTERNAL; 1=EXTERNAL]
            ("arp_latch", 1),  # [0=OFF; 1=ON]
            ("arp_swing", 4),  # [0=50%; 1=55%; 2=57%; 3=59%; 4=61%; 5=64%]
            ("arp_taps", 3),  # [2,4]

            # The arpeggiator tempo is encoded using 2 bytes
            # the first one may be 0 or 1
            # if the first one is 0
            #    then the second one is in [30,127]
            # if the first one is 1
            #    then the second one is in [0,112] (128,240)
            ("arp_tempo", 0),  # 0 [0,1]
            ("arp_tempo", 79),  # 1 [30,127; 0,112]

            ("arp_octave", 1),  # [0,3]

            ("x_axis_type", 2),  # [0=PITCHBEND; 1=CC1; 2=CC2]
            ("x_axis_L", 80),  # [0,127]
            ("x_axis_R", 81),  # [0,127]

            ("y_axis_type", 2),
            ("y_axis_D", 83),
            ("y_axis_U", 82),

            # Bank A
            ("b1_p1_NT", 0),  # [0,127]
            ("b1_p1_PC", 15),  # [0,127]
            ("b1_p1_CC", 31),  # [0,127]
            ("b1_p1_TP", 1),  # [0=TOGGLE; 1=MOMENTARY]

            ("b1_p2_NT", 1),
            ("b1_p2_PC", 16),
            ("b1_p2_CC", 32),
            ("b1_p2_TP", 1),

            ("b1_p3_NT", 2),
            ("b1_p3_PC", 17),
            ("b1_p3_CC", 33),
            ("b1_p3_TP", 1),

            ("b1_p4_NT", 3),
            ("b1_p4_PC", 18),
            ("b1_p4_CC", 34),
            ("b1_p4_TP", 1),

            ("b1_p5_NT", 4),
            ("b1_p5_PC", 19),
            ("b1_p5_CC", 35),
            ("b1_p5_TP", 1),

            ("b1_p6_NT", 5),
            ("b1_p6_PC", 20),
            ("b1_p6_CC", 36),
            ("b1_p6_TP", 1),

            ("b1_p7_NT", 6),
            ("b1_p7_PC", 21),
            ("b1_p7_CC", 37),
            ("b1_p7_TP", 1),

            ("b1_p8_NT", 7),
            ("b1_p8_PC", 22),
            ("b1_p8_CC", 38),
            ("b1_p8_TP", 1),

            # Bank B
            ("b2_p1_NT", 8),
            ("b2_p1_PC", 23),
            ("b2_p1_CC", 39),
            ("b2_p1_TP", 0),

            ("b2_p2_NT", 9),
            ("b2_p2_PC", 24),
            ("b2_p2_CC", 40),
            ("b2_p2_TP", 0),

            ("b2_p3_NT", 10),
            ("b2_p3_PC", 25),
            ("b2_p3_CC", 41),
            ("b2_p3_TP", 0),

            ("b2_p4_NT", 11),
            ("b2_p4_PC", 26),
            ("b2_p4_CC", 42),
            ("b2_p4_TP", 0),

            ("b2_p5_NT", 12),
            ("b2_p5_PC", 27),
            ("b2_p5_CC", 43),
            ("b2_p5_TP", 0),

            ("b2_p6_NT", 13),
            ("b2_p6_PC", 28),
            ("b2_p6_CC", 44),
            ("b2_p6_TP", 0),

            ("b2_p7_NT", 14),
            ("b2_p7_PC", 29),
            ("b2_p7_CC", 45),
            ("b2_p7_TP", 0),

            ("b2_p8_NT", 15),
            ("b2_p8_PC", 30),
            ("b2_p8_CC", 46),
            ("b2_p8_TP", 0),

            # Knobs
            ("k1_CC", 47),  # [0,127]
            ("k1_LO", 63),  # [0,127]
            ("k1_HI", 71),  # [0,127]

            ("k2_CC", 48),
            ("k2_LO", 64),
            ("k2_HI", 72),

            ("k3_CC", 49),
            ("k3_LO", 65),
            ("k3_HI", 73),

            ("k4_CC", 50),
            ("k4_LO", 66),
            ("k4_HI", 74),

            ("k5_CC", 59),
            ("k5_LO", 67),
            ("k5_HI", 75),

            ("k6_CC", 60),
            ("k6_LO", 68),
            ("k6_HI", 76),

            ("k7_CC", 61),
            ("k7_LO", 69),
            ("k7_HI", 77),

            ("k8_CC", 62),
            ("k8_LO", 70),
            ("k8_HI", 78),

            ("key_transpose", 3),  # [0,24]
            ("sysex_end", 247)  # [247]
            ))
        self.midi_setup()

    def midi_setup(self):
        self.mo = rtmidi.MidiOut()
        try:
            self.mo.open_port(1)
        except RuntimeError:
            print("Please connect controller")
            sys.exit()
        self.mi = rtmidi.MidiIn()
        self.mi.open_port(1)
        self.mi.ignore_types(sysex=False)

    def get_all_programmes(self):
        for p_i in range(1, 5):
            self.get_programme(p_i)

    def get_active_programme(self):
        p_i = self.get_active_tab_index()+1
        self.get_programme(p_i)

    def get_programme(self, p_i):
        print(p_i)
        message = [[]]
        self.GET_CONFIG[7] = p_i
        self.mo.send_message(self.GET_CONFIG)
        time.sleep(0.05)
        while message is None or len(message[0]) != 117:
            message = self.mi.get_message()
        message = message[0]  # strip midi time
        print(message)
        self.fill_active_tab(message)


        # self.progs[0]["knobs"][0]["knobCCSpinBox"].setValue(20)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Akai_MPK_Mini()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.get_all_programmes()
    sys.exit(app.exec_())
