
while True:
  
 try:
    number = int(input("Digite su calificacion: "))
    
    if 0 <= number <=100:
       
        break
    else:
        print("por favor ingresa, un numero entre el 1 y el 100")
        
 except ValueError:
            print("Entrada no valida")
        
        