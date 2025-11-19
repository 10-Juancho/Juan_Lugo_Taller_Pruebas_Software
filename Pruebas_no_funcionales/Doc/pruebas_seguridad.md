# 🛡️ PRUEBAS DE SEGURIDAD API REST.

Este documento describe el proceso, la lógica y los resultados de las pruebas de seguridad implementadas para una API REST encargada de gestionar usuarios. El objetivo principal es garantizar que el sistema sea capaz de identificar y rechazar entradas maliciosas, tales como:
- Inyecciones SQL (SQL Injection)
- Ataques XSS (Cross-Site Scripting)
- Entrada de código HTML o JavaScript no permitido

Estas pruebas se ejecutaron utilizando pytest, verificando que el sistema actúe de forma segura al validar los datos de entrada.

## 📌 OBETIVOS DE SEGURIDAD.
Las  pruebas buscan validar que el API cumpla con los siguientes principios:

- Validación de Entradas : Garantizar que solo se acepten datos seguros y adecuados.
- Prevención de Inyeción SQL: Bloquear comandos maliciosos que intenten manipular la base de datos.
- Prevención de Ataques XSS: Evitar que scripts o etiquetas HTML sean procesadas por el servidor.

## IMPLEMENTACIÓN DEL SERVICIO:
> USerService

EL servicio cuenta con un mecanismo de validación basado en expreseiones regulares para detectar patrones maliciosos.
```Python
import re


class UserService:
def __init__(self):
self.users = []


def add_user(self, username):
# Detectar patrones maliciosos: SQL Injection y XSS
if re.search(r"('|;|--|<script>|</script>|<|>)", username):
raise ValueError("Input contains invalid characters.")


self.users.append(username)
``` 
### 🧠 EXPLICACÓN DE LA LOGICA DE SEGURIDAD.
- ' → detecta intentos de cerrar cadenas SQL.

- ; → separadores usados en comandos de inyección.

- -- → comentarios SQL utilizados en ataques.

- → inicio de un ataque XSS.

- → cierre de script.

- < > → manejo de cualquier etiqueta HTML.

El método lanza una excepción ValueError cuando detecta contenido sospechoso, impidiendo añadir el usuario.

## 📌 PRUEBAS DE SEGURIDAD.
Las pruebas se diseñaron para evaluar que el sistema detecte diferentes formas de ataque.
1. PRUEBA - PREVENCIÓN DE SQL INTECTION .

``` Python
with pytest.raises(ValueError):
user_service.add_user("user'; DROP TABLE users; --")

``` 
> Resultado esperado: EL sistema rechaza la entrada maliciosa.

2. PPRUEBA  - PREVENCIÓN DE XSS ETIQUETAS "Script".
``` Python
with pytest.raises(ValueError):
user_service.add_user("<script>alert('XSS')</script>")
``` 
> Resultado esperado:EL servicio bloque cualqueir etiqueta "script".

3. PRUEBA - PREVENCIÓN DE XSSS - HTML con JavaScript.
``` Python
with pytest.raises(ValueError):
user_service.add_user("<img src=x onerror=alert('XSS')>")
``` 
> Resultado esperado: Se rechaza cualquier elemento HTML.

4. USUARIO VALIDO.
``` Python 
user_service.add_user("usuario_normal")
assert "usuario_normal" in user_service.users
``` 
> Resultado esperado: Entradas limpias son aceptadas correctamente.

## EJECUCIÓN DE LAS PRUEBAS.
Las pruebas se ejecutan con el siguiete comando.
> pytest pruebas_no_funcionales/test_segurity.py -v