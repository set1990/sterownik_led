import wiringpi

OUTPUT = 1

PIN_TO_PWM = 10

wiringpi.wiringPiSetup()
wiringpi.pinMode(PIN_TO_PWM, OUTPUT)
wiringpi.softPwmCreate(PIN_TO_PWM,0,255) # Setup PWM using Pin, Initial Value and Range parameters

for time in range(0,4):
	for brightness in range(0,255): # Going from 0 to 100 will give us full off to full on
		wiringpi.softPwmWrite(PIN_TO_PWM,brightness) # Change PWM duty cycle
		wiringpi.delay(10) # Delay for 0.2 seconds
	for brightness in reversed(range(0,255)):
		wiringpi.softPwmWrite(PIN_TO_PWM,brightness)
		wiringpi.delay(10)
