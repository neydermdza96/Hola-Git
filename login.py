print("Login v2")
# -----------------------------------------------------
# 1. Definición de credenciales de prueba
# -----------------------------------------------------
USUARIO_CORRECTO = "sena_aprendiz"
CONTRASENA_CORRECTA = "clave123"

def verificar_credenciales(usuario, contrasena):
    """Verifica si el usuario y la contraseña son correctos."""
    if usuario == USUARIO_CORRECTO and contrasena == CONTRASENA_CORRECTA:
        return True
    else:
        return False

# -----------------------------------------------------
# 2. Función principal del Login
# -----------------------------------------------------
def ejecutar_login():
    """Ejecuta el proceso de solicitud y verificación de login."""
    print("--- Sistema de Login ---")

    # Solicitud de datos al usuario
    usuario_ingresado = input("Ingrese su usuario: ")
    contrasena_ingresada = input("Ingrese su contraseña: ")

    # Verificación
    if verificar_credenciales(usuario_ingresado, contrasena_ingresada):
        print("\n✅ ¡Inicio de sesión exitoso! Bienvenido.")
        # Aquí iría el código para entrar a la aplicación
    else:
        print("\n❌ Error: Usuario o contraseña incorrectos.")
        print("Intente de nuevo.")

# -----------------------------------------------------
# 3. Ejecución del programa
# -----------------------------------------------------
if __name__ == "__main__":
    ejecutar_login()