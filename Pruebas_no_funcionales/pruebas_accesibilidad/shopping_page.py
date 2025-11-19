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