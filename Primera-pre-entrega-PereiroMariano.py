# Función para registrar un nuevo usuario
def registrar_usuario():
  usuarios = {}
  nombre = input("Ingrese su nombre de usuario: ")
  contraseña = input("Ingrese su contraseña: ")
  usuarios[nombre] = contraseña
  return usuarios

# Función para mostrar los usuarios registrados
def mostrar_usuarios(usuarios):
  if not usuarios:
    print("No hay usuarios registrados, Ingrese uno ")
  else:
    for nombre, contraseña in usuarios.items():
      print(f"Nombre de usuario: {nombre}, Contraseña: {contraseña}")

# Función para verificar si el usuario ya está registrado
def usuario_registrado(usuarios, nombre):
  return nombre in usuarios

# Función para verificar si una contraseña es correcta para el usuario
def contraseña_correcta(usuarios, nombre, contraseña):
  if nombre in usuarios and usuarios[nombre] == contraseña:
    return True
  else:
    return False

# Función para registrar un nuevo usuario o muestra un mensaje si el usuario ya está registrado
def registrar_o_mostrar_error(usuarios):
  nombre = input("Ingrese su nombre de usuario: ")
  if usuario_registrado(usuarios, nombre):
    print("El usuario ya está registrado")
    print("Ingrese otro nombre de usuario")
  else:
    contraseña = input("Ingrese su contraseña: ")
    usuarios[nombre] = contraseña
    print("Usuario registrado")

def ejecutar_programa():
  usuarios = {}
  while True:
    opcion = input("Ingrese una opción (1 para registrar un usuario, 2 para mostrar los usuarios registrados, 3 para salir): ")
    if opcion == "1":
      registrar_o_mostrar_error(usuarios)
    elif opcion == "2":
      mostrar_usuarios(usuarios)
    elif opcion == "3":
      print("Hasta la proxima!")
      break
    else:
      print("Opción inválida")

ejecutar_programa()