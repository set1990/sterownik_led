import wiringpi

OUTPUT = 1

PIN_RED = 10
PIN_GREEN = 1
PIN_BLUE = 3

wiringpi.wiringPiSetup()
wiringpi.pinMode(PIN_RED, OUTPUT)
wiringpi.pinMode(PIN_GREEN, OUTPUT)
wiringpi.pinMode(PIN_BLUE, OUTPUT)
wiringpi.softPwmCreate(PIN_RED,0,255) # Setup PWM using Pin, Initial Value and Range parameters
wiringpi.softPwmCreate(PIN_GREEN,0,255) # Setup PWM using Pin, Initial Value and Range parameters
wiringpi.softPwmCreate(PIN_BLUE,0,255) # Setup PWM using Pin, Initial Value and Range parameters

for time in range(0,4):
	for brightness in range(0,255): # Going from 0 to 100 will give us full off to full on
		wiringpi.softPwmWrite(PIN_RED,brightness) # Change PWM duty cycle
		wiringpi.delay(10) # Delay for 0.2 seconds
	for brightness in reversed(range(0,255)):
		wiringpi.softPwmWrite(PIN_RED,brightness)
		wiringpi.delay(10)

	for brightness in range(0,255): # Going from 0 to 100 will give us full off to full on
		wiringpi.softPwmWrite(PIN_GREEN,brightness) # Change PWM duty cycle
		wiringpi.delay(10) # Delay for 0.2 seconds
	for brightness in reversed(range(0,255)):
		wiringpi.softPwmWrite(PIN_GREEN,brightness)
		wiringpi.delay(10)

	for brightness in range(0,255): # Going from 0 to 100 will give us full off to full on
		wiringpi.softPwmWrite(PIN_BLUE,brightness) # Change PWM duty cycle
		wiringpi.delay(10) # Delay for 0.2 seconds
	for brightness in reversed(range(0,255)):
		wiringpi.softPwmWrite(PIN_BLUE,brightness)
		wiringpi.delay(10)