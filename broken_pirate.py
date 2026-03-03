greeting = input("Hello, possible pirate! What's the password? ") # Missing colon at the end of this line
if greeting in ["Arrr!"]: # NG replaced ) by ]
	print("Go away, pirate.")
else: # We do not use elif here, we can just use 'else'. We can also remove the rest of the condition
	print("Greetings, hater of pirates!")
