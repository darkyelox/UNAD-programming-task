from .modules.utils.exceptions_logger import ExceptionsLoggerHandler

def raise_error(msg: str):
    raise ValueError(msg)

def test_should_write_logger_on_error():
    ex_handler = ExceptionsLoggerHandler('test-logger')

    ex_handler.handle(
        execute=lambda:
            1/0,
        onError=lambda:
            print('There was an error'),
        onSuccess=lambda:
            print('Ok')
    )

    ex_handler.handle(
        execute=lambda:
            raise_error('This should not pass'),
        onError=lambda:
            print('There was an error'),
        import re

from excepciones import *
from exceptions_logger import ExceptionsLogger


# =====================================
# CONFIGURAR LOGGER
# =====================================

ExceptionsLogger.configurar_logger()


# =====================================
# CLASE CLIENTE
# =====================================

class Cliente:

    def __init__(self, nombre, edad, correo, telefono):

        self.__nombre = None
        self.__edad = None
        self.__correo = None
        self.__telefono = None

        self.set_nombre(nombre)
        self.set_edad(edad)
        self.set_correo(correo)
        self.set_telefono(telefono)

    # =====================================
    # VALIDACIÓN NOMBRE
    # =====================================

    def set_nombre(self, nombre):

        try:

            if not nombre.strip():

                raise NombreInvalidoError(
                    "El nombre no puede estar vacío"
                )

            if len(nombre) < 3:

                raise NombreInvalidoError(
                    "El nombre debe tener mínimo 3 caracteres"
                )

            self.__nombre = nombre

        except Exception as e:

            ExceptionsLogger.registrar_error(e)
            raise

    # =====================================
    # VALIDACIÓN EDAD
    # =====================================

    def set_edad(self, edad):

        try:

            edad = int(edad)

            if edad < 18 or edad > 100:

                raise EdadInvalidaError(
                    "La edad debe estar entre 18 y 100 años"
                )

            self.__edad = edad

        except ValueError as e:

            ExceptionsLogger.registrar_error(e)

            raise EdadInvalidaError(
                "La edad debe ser un número"
            ) from e

        except Exception as e:

            ExceptionsLogger.registrar_error(e)
            raise

    # =====================================
    # VALIDACIÓN CORREO
    # =====================================

    def set_correo(self, correo):

        try:

            patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'

            if not re.match(patron, correo):

                raise CorreoInvalidoError(
                    "Correo inválido"
                )

            self.__correo = correo

        except Exception as e:

            ExceptionsLogger.registrar_error(e)
            raise

    # =====================================
    # VALIDACIÓN TELÉFONO
    # =====================================

    def set_telefono(self, telefono):

        try:

            telefono = str(telefono)

            if not telefono.isdigit():

                raise TelefonoInvalidoError(
                    "El teléfono solo debe tener números"
                )

            if len(telefono) != 10:

                raise TelefonoInvalidoError(
                    "El teléfono debe tener 10 dígitos"
                )

            self.__telefono = telefono

        except Exception as e:

            ExceptionsLogger.registrar_error(e)
            raise

    # =====================================
    # GETTERS
    # =====================================

    def get_nombre(self):
        return self.__nombre

    def get_edad(self):
        return self.__edad

    def get_correo(self):
        return self.__correo

    def get_telefono(self):
        return self.__telefono

    # =====================================
    # MOSTRAR INFO
    # =====================================

    def mostrar_info(self):

        return (
            f"\nCliente:"
            f"\nNombre: {self.__nombre}"
            f"\nEdad: {self.__edad}"
            f"\nCorreo: {self.__correo}"
            f"\nTeléfono: {self.__telefono}"
        )


# =====================================
# LISTA DE CLIENTES
# =====================================

lista_clientes = []


# =====================================
# FORMULARIO
# =====================================

def registrar_cliente():

    print("\n==============================")
    print("REGISTRO DE CLIENTE")
    print("==============================")

    try:

        nombre = input("Nombre: ")
        edad = input("Edad: ")
        correo = input("Correo: ")
        telefono = input("Teléfono: ")

        cliente = Cliente(
            nombre,
            edad,
            correo,
            telefono
        )

        lista_clientes.append(cliente)

    except ClienteError as e:

        print(f"\nError de validación: {e}")

    except Exception as e:

        print(f"\nError inesperado: {e}")

    else:

        print("\nCliente registrado correctamente")
        print(cliente.mostrar_info())

    finally:

        print("\nProceso finalizado")


# =====================================
# PRUEBAS
# =====================================

for i in range(3):

    registrar_cliente()


# =====================================
# MOSTRAR CLIENTES
# =====================================

print("\n=========== CLIENTES ===========")

for cliente in lista_clientes:

    print(cliente.mostrar_info())
    print("--------------------------------")
        onSuccess=lambda:
            print('Ok')
    )

    
test_should_write_logger_on_error()
