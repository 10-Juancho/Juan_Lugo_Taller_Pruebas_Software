from shopping_page import ShoppingPage
def test_accessibility():
    shopping_page = ShoppingPage()
    
    # Recuperar el producto como lo haría un lector de pantalla
    item = shopping_page.get_item("Laptop")
    
    # Pruebas básicas de accesibilidad
    assert item is not None
    assert "alt" in item               # Debe tener texto alternativo
    assert item["alt"] != ""           # No puede estar vacío