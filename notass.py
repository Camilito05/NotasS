##global para que se pueda acceder a la lista de registro de cualquier parte del codigo
listRegistro = [] ##lista de registro de usuarios

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
    print("--------Iniciar sesion--------")
    email = input("Ingrese su email:  ")
    password = input("Ingrese su contraseña: ")
   




    for usuario in listRegistro:
        if usuario["email"] == email  and usuario["contraseña"] == password:
            print(f"Bienvenido {usuario["nombre"]} {usuario["apellido"]}")
            2
            
            if usuario["rol"] == "profesor":
                print("----acesso al sistema de profesores ----- ")
                
            elif usuario["rol"] == "estudiante":   
                print("----acesso al sistema de estudiantes ----- ")
                 
        else:
            print("Usuario o contraseña incorrecta")
            




opcionMenu =0 ##inicializar la variable
rol=0
##creacion del sistema de notas 
while opcionMenu != 3:
    print("Por favor seleccione una opcion.")
    print("Bienvenido al sistema de notas.")
    print("-----------------------------")
    print("1. para registrarse.")
    print("2. para ingresar.")
    print("3. para salir.")
    opcionMenu = input("Ingrese la opcion:  ")
    
    ##menu para que ingrese i se registren

    if opcionMenu == "1":
        registro()
    elif opcionMenu == "2":
        ingresar()
        
    elif opcionMenu == "3":
        print("Gracias por usar el sistema de notas. Hata luego")     
    else:
        print("opcion incorrecta")    

            


    