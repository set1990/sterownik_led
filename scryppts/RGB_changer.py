import wiringpi
import sys
from random import sample


def rgbSetup():
    wiringpi.wiringPiSetup()
    wiringpi.pinMode(PIN_RED, OUTPUT)
    wiringpi.pinMode(PIN_GREEN, OUTPUT)
    wiringpi.pinMode(PIN_BLUE, OUTPUT)
    wiringpi.softPwmCreate(PIN_RED, 0, 100)  # Setup PWM using Pin, Initial Value and Range parameters
    wiringpi.softPwmCreate(PIN_GREEN, 0, 100)  # Setup PWM using Pin, Initial Value and Range parameters
    wiringpi.softPwmCreate(PIN_BLUE, 0, 100)  # Setup PWM using Pin, Initial Value and Range parameters


def setColor(PIN, color, prev_color):
    if color > prev_color:
        for value in range(prev_color, color+1):
            wiringpi.softPwmWrite(PIN, value)  # Change PWM duty cycle
            wiringpi.delay(100)
    elif color < prev_color:
        for value in range(prev_color, color+1,-1):
            wiringpi.softPwmWrite(PIN, value)  # Change PWM duty cycle
            wiringpi.delay(100)


def tolalRandomColor():
    global RED_LED
    global GREEN_LED
    global BLUE_LED
    RED_LED = (sample(RedList, 1))[0]
    GREEN_LED = (sample(Greenlist, 1))[0]
    BLUE_LED = (sample(BlueList, 1))[0]


def onFromThreeColor():
    global RED_LED
    global GREEN_LED
    global BLUE_LED
    match = (sample(range(0, 3), 1))[0]
    if match == 0:
        RED_LED = 100
        GREEN_LED = 0
        BLUE_LED = 0
    elif match == 1:
        RED_LED = 0
        GREEN_LED = 100
        BLUE_LED = 0
    elif match == 2:
        RED_LED = 0
        GREEN_LED = 0
        BLUE_LED = 100


def setColorRandomQ():
    match = (sample(range(0, 4), 1))[0]
    if match == 0 :
        if RED_LED_PREV != 100:
            setColor(PIN_RED, RED_LED, RED_LED_PREV)
            setColor(PIN_GREEN, GREEN_LED, GREEN_LED_PREV)
            setColor(PIN_BLUE, BLUE_LED, BLUE_LED_PREV)
        else:
            match = 1
    if match == 1:
        if GREEN_LED_PREV != 100:
            setColor(PIN_GREEN, GREEN_LED, GREEN_LED_PREV)
            setColor(PIN_RED, RED_LED, RED_LED_PREV)
            setColor(PIN_BLUE, BLUE_LED, BLUE_LED_PREV)
        else:
            match = 2
    if match == 2:
        if BLUE_LED_PREV != 100:
            setColor(PIN_BLUE, BLUE_LED, BLUE_LED_PREV)
            setColor(PIN_RED, RED_LED, RED_LED_PREV)
            setColor(PIN_GREEN, GREEN_LED, GREEN_LED_PREV)
        else:
            match = 3
    if match == 3:
        if GREEN_LED_PREV != 100:
            setColor(PIN_GREEN, GREEN_LED, GREEN_LED_PREV)
            setColor(PIN_BLUE, BLUE_LED, BLUE_LED_PREV)
            setColor(PIN_RED, RED_LED, RED_LED_PREV)
        else:
            setColor(PIN_BLUE, BLUE_LED, BLUE_LED_PREV)
            setColor(PIN_RED, RED_LED, RED_LED_PREV)
            setColor(PIN_GREEN, GREEN_LED, GREEN_LED_PREV)


OUTPUT = 1
PIN_RED = int(sys.argv[1])
PIN_GREEN = int(sys.argv[2])
PIN_BLUE = int(sys.argv[3])
PAUSE_S = int(sys.argv[4]) * 1000
rgbSetup()

RedList = range(0, 100)
Greenlist = range(0, 100)
BlueList = range(0, 100)

RED_LED = 0
GREEN_LED = 0
BLUE_LED = 0

RED_LED_PREV = 0
RED_LED_PREV = 0
GREEN_LED_PREV = 0
BLUE_LED_PREV = 0

while (1):
    if sys.argv[5] == 'T':
        tolalRandomColor()
    else:
        onFromThreeColor()
    setColorRandomQ()
    RED_LED_PREV = RED_LED
    GREEN_LED_PREV = GREEN_LED
    BLUE_LED_PREV = BLUE_LED

    wiringpi.delay(PAUSE_S)

