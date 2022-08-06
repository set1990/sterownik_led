import wiringpi

OUTPUT = 1

PIN_TO_PWM = 10

wiringpi.wiringPiSetup()
wiringpi.pinMode(PIN_TO_PWM, OUTPUT)
wiringpi.digitalWrite(PIN_TO_PWM, 1)

for i in range(0, 4):
    for brightness in range(0, 255):
        for time in range(0, 100):
            wiringpi.digitalWrite(PIN_TO_PWM, 1)
            wiringpi.delayMicroseconds(brightness)
            wiringpi.digitalWrite(PIN_TO_PWM, 0)
            wiringpi.delayMicroseconds(255 - brightness)
    for brightness in reversed(range(0, 255)):
        for time in range(0, 100):
            wiringpi.digitalWrite(PIN_TO_PWM, 1)
            wiringpi.delayMicroseconds(brightness)
            wiringpi.digitalWrite(PIN_TO_PWM, 0)
            wiringpi.delayMicroseconds(255 - brightness)

#for time in range(0, 1):
#
#    for brightness in range(0, 1000):  # Going from 0 to 100 will give us full off to full on
#
#        wiringpi.digitalWrite(PIN_TO_PWM, 1)
#        wiringpi.delayMicroseconds (brightness)  # Delay for 0.2 seconds
#        wiringpi.digitalWrite(PIN_TO_PWM, 0)
#    for brightness in reversed(range(0, 1000)):
#        wiringpi.digitalWrite(PIN_TO_PWM, 1)
#        wiringpi.delayMicroseconds(brightness)
#        wiringpi.digitalWrite(PIN_TO_PWM, 0)
