##global para que se pueda acceder a la lista de registro de cualquier parte del codigo
listRegistro = [] ##lista de registro de usuarios
notasR = [] ##lista de notas
def registro():
    print("Por favor registrase ")
    
    nombre=input("ingrese su nombre ")
    
    lasName=input("ingrese su apellido:  ")
    email=input("ingrese su email:  ")
    password=input("ingrese su contraseña:  ")
    rol=input("ingrese su rol 1. profesor 2. estudiante:  ")
    

    usuario = {
        "nombre" : nombre,
        "apellido" : lasName,
        "email" : email,
        "contraseña" : password,
        "rol":rol
    }
    ##rol para el registro del profe o estudiante
    if rol == "1":
        usuario["rol"] = "profesor"
    elif rol=="2":
        usuario["rol"] = "estudiante"     
    else:
        print("Rol no valido")
        return
    ##agregar un un usuario a la lista de resgistro
    listRegistro.append(usuario)
    print(f"Usuario {nombre} {lasName} registrado con exito")

def ingresar():
    print("---------------------------")
    print("--------Iniciar sesion-----")
    print("---------------------------")
    email = input("Ingrese su email:  ")
    password = input("Ingrese su contraseña: ")
   




    for usuario in listRegistro:
        if usuario["email"] == email  and usuario["contraseña"] == password:
            print(f"Bienvenido {usuario["nombre"]} {usuario["apellido"]}")
            
            
            if usuario["rol"] == "profesor":
                print("-------------------------------------------")
                print("----acesso al sistema de profesores ----- ")
                print("-------------------------------------------")
                notasP()
            elif usuario["rol"] == "estudiante": 
                print("-------------------------------------------")  
                print("----acesso al sistema de estudiantes ----- ")
                print("-------------------------------------------") 
        else:
            print("Usuario o contraseña incorrecta")
            
def notasP():
  while True:  
    print("---------------------------")
    print("----Sistema de notas----")
    print("---------------------------")
    
    print("1. para ingresar notas")
    print("2. para ver notas")
    print("3. para salir")
    opcionMenu = input("Ingrese la opcion:  ")
   
   #menu para el ingreso de las notas 
    if opcionMenu == "1":
        cantidad=int(input("cuantas notas deseas ingresar"))
        for i in range(cantidad):
            nota=float(input("Ingrese la nota"))
            notasR.append(nota)
    
    elif opcionMenu == "2":
       if len(notasR)==0:
           print("no hay notas registradas")
       else:  
         print("notas registrada con exito")  
         for i,nota in enumerate(notasR , start=1): #enumera las notas 
            print(f" nota {i}=  {nota}")
    else:
        print("saliendo del sistema")
        break
       

       



opcionMenu =0 ##inicializar la variable
rol=0
##creacion del sistema de notas 
while opcionMenu != 3:
    print("Por favor seleccione una opcion.")
    print("Bienvenido al sistema de notas.")  
    print("-----------------------------")
    print("-----------------------------")
    print("1. para registrarse.")
    print("2. para ingresar.")
    print("3. para salir.")
       
    print("-----------------------------")
    opcionMenu = input("Ingrese la opcion:  ")  
    print("-----------------------------")
    ##menu para que ingrese i se registren

    if opcionMenu == "1":
        registro()
    elif opcionMenu == "2":
        if len(listRegistro) == 0:
            print("No hay usuarios registrados. Por favor, regístrese primero.")
        else:
            ingresar()
       
    elif opcionMenu == "3":
        print("Gracias por usar el sistema de notas. Hata luego")     
    else:
        print("opcion incorrecta")    

            


    