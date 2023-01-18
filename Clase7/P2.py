# Time Module
import time

# initialize
hour = time.strftime('%H') 
min = time.strftime('%M') 

# Verify
if int(hour) >= 19:
	print ("Ya es tiempo de volver a casa") 
else:
    new_hour = 18 - int(hour)
    new_min = 59 - int(min)
    print(f"Aun quedan {new_hour} y {new_min} para regresar a casa, se debe continuar trabajando")