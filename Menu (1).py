import getpass

# Base de datos de usuarios
usuarios = {
    'Narciso': '111',
    'Pablo': '222',
    'David': '333',
    'Juan Cruz': '444',
    'Nicolas': '555',
    'Nahuel': '666'
}

# Base de datos de notas
notas = {
    'Juan Cruz': {'Matematicas': 8, 'Historia': 6, 'Ciencias': 5},
    'Nicolas': {'Matematicas': 2, 'Historia': 10, 'Ciencias': 7},
    'Nahuel': {'Matematicas': 5, 'Historia': 7, 'Ciencias': 3}
}

# Función para verificar las credenciales de usuario
def verificar_credenciales():
    usuario = input('Ingrese su nombre de usuario: ')
    contraseña = getpass.getpass('Ingrese su contraseña: ')
    if usuario in usuarios and usuarios[usuario] == contraseña:
        return usuario
    else:
        print('Credenciales inválidas. Inténtelo de nuevo.')
        return None

# Función para el rol de alumno
def rol_alumno(usuario):
    if usuario in notas:
        print(f'Notas de {usuario}:')
        for materia, nota in notas[usuario].items():
            print(f'{materia}: {nota}')
    else:
        print('Usuario no válido.')

# Función para el rol de preceptor
def rol_preceptor(usuario):
    if usuario.startswith('alumno'):
        print(f'El usuario {usuario} no tiene permisos de preceptor.')
    else:
        print('Funcionalidad de preceptor.')

# Función para el rol de profesor
def rol_profesor(usuario):
    if usuario.startswith('alumno'):
        print(f'El usuario {usuario} no tiene permisos de profesor.')
    else:
        print('Funcionalidad de profesor.')

# Historia de usuario: Ver notas (alumno)
def historia_usuario_1():
    usuario = verificar_credenciales()
    if usuario:
        rol_alumno(usuario)

# Historia de usuario: Cargar y modificar notas (profesor)
def historia_usuario_2():
    usuario = verificar_credenciales()
    if usuario:
        rol_profesor(usuario)

# Historia de usuario: Ver y cargar notas (preceptor)
def historia_usuario_3():
    usuario = verificar_credenciales()
    if usuario:
        rol_preceptor(usuario)

# Menú principal
def menu_principal():
    print('Bienvenido al sistema de gestión de notas.')
    print('Seleccione una opción:')
    print('1. Ver notas (alumno)')
    print('2. Cargar y modificar notas (profesor)')
    print('3. Ver y cargar notas (preceptor)')
    print('4. Salir')

    opcion = input('Ingrese el número de opción: ')
    if opcion == '1':
        historia_usuario_1()
    elif opcion == '2':
        historia_usuario_2()
    elif opcion == '3':
        historia_usuario_3()
    elif opcion == '4':
        print('Gracias por utilizar el sistema. ¡Hasta luego!')
    else:
        print('Opción inválida. Inténtelo de nuevo.')

# Ejecutar el programa
menu_principal()