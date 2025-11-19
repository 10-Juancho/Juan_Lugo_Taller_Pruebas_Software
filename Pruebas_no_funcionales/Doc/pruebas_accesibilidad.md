# 🛒 PRUEBA DE ACCESIBILIDAD - TIENDA EN LINEA.
Se desarrolló una página de tienda en línea que contiene una lista de productos.
Con el objetivo de garantizar que el sitio sea accesible para personas con discapacidades visuales, se realizaron pruebas de accesibilidad, enfocadas en:

- Verificar que los elementos tengan texto alternativo (alt)

- Confirmar que esa información sea válida para lectores de pantalla

Estas pruebas simulan cómo un usuario con lector de pantalla interactuaría con los elementos de la página.

## 💻 IMPLEMENTACIÓN.
``` Python
class ShoppingPage:
    # Clase que representa la página de una tienda en línea

    def __init__(self):
        # Constructor de la clase
        # Se inicializa una lista de productos disponibles en la tienda.
        # Cada producto contiene:
        # - name: nombre del producto
        # - price: precio
        # - alt: texto alternativo para accesibilidad (por ejemplo, usado por lectores de pantalla)
        self.items = [
            {"name": "Laptop", "price": 1000, "alt": "Imagen de una laptop"},
            {"name": "Mouse", "price": 50, "alt": "Imagen de un mouse"}
        ]
    
    def get_item(self, name):
        # Método para obtener un producto según su nombre
        # Se utiliza 'next' con una expresión generadora para recorrer la lista
        # Si encuentra un producto cuyo nombre coincida, lo retorna
        # Si no encuentra ninguno, retorna None
        return next((item for item in self.items if item["name"] == name), None)
``` 
En este modelo, cada producto contiene:
- name: nombre del producto
- price: precio
- alt: descripción alternativa para asistentes visuales

## 🧪 PRUEBA (PYTEST).
``` Python
from shopping_page import ShoppingPage
def test_accessibility():
    shopping_page = ShoppingPage()
    
    # Recuperar el producto como lo haría un lector de pantalla
    item = shopping_page.get_item("Laptop")
    
    # Pruebas básicas de accesibilidad
    assert item is not None
    assert "alt" in item               # Debe tener texto alternativo
    assert item["alt"] != ""           # No puede estar vacío
``` 

### 🎯 OBJETIVO DE LA PRUEBA.
La prueba asegura que:

- El elemento buscado existe en la página.

- El producto incluye texto alternativo.

- El texto alternativo no está vacío, lo que lo hace apto para lectores de pantalla.

#### 🔍  PORQUE ES IMPORTANTE.

Las personas con discapacidad visual dependen de lectores de pantalla para interpretar imágenes.
Si un producto no tiene alt, el lector:

❌ No podrá describir lo que se muestra <br>

❌ El usuario no entenderá el contenido <br>

✔ La accesibilidad se deteriora <br>

Con estas pruebas:

- Se aumenta la inclusión del sistema

- Se reduce barreras digitales

- Se comprueba el cumplimiento de buenas prácticas como WCAG


Como ejecutarla.

>pytest Pruebas_no_funcionales/pruebas_accesibilidad/test_shopping_page.py -v