import time
import sys

sys.path.append('../evobliss-software/api')
from evobot import EvoBot
from datalogger import DataLogger
from syringe import Syringe
from head import Head


def webControl(x,y):
    x=int(x)
    y=int(y)
    usrMsgLogger = DataLogger()
    evobot = EvoBot("/dev/tty.usbmodemfa131", usrMsgLogger)
    head = Head( evobot )
    syringe =  Syringe( evobot, 9)
    syringe.plungerSetConversion( 1 )
    evobot.home()
    
    
    head.move(x,y)
    #syringe.syringeMove( -30 )
    #syringe.plungerPullVol( 5 ) 
    #syringe.syringeMove( 0 )
    #head.move( 90, 100 )
    #syringe.plungerPushVol( 5 )
    
    #evobot.disconnect()



