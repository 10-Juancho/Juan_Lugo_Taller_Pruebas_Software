from sistema_compras import Product, ShoppingCart

#  Test Flujo 
def test_complete_purchase_systeam_flow():
    # Crea los productos 
    laptop = Product ("Laptop", 1000,10)
    mouse = Product ("Mouse",50,20)

    # Crea el carrito 
    cart = ShoppingCart ()

    # Agrega productos al carrito 
    assert cart.add_item (laptop, 1) is True
    assert cart.add_item (mouse, 2) is True

    # Verificar que el total sea corrrecto
    assert cart.total == 1100

    # Verifica que el stock de los productos se actualicen correctamente

    assert laptop.stock == 9
    assert mouse.stock == 18

# Test cuabdo no hay Stock
def test_cannot_add_iteam_with_zero_stock ():
    # Creando el producto
    book = Product ("book",20,0)

    #Creando el carrito     
    cart = ShoppingCart()

    #  Intentar agregar un producto sin stock
    assert cart.add_item (book,1) is False
    assert book.stock == 0 
    assert cart.total == 0

# Test Negativo

def test_cannot_add_more_than_stock ():
    # Creando el producto
    ps5 = Product ("ps5", 3000,5)

    # Crea el carrito
    cart = ShoppingCart ()

    # Intentar comprar más del stock 
    assert cart.add_item ( ps5, 6) is False

    # Stock debe mantenerse igual 
    assert ps5.stock == 5

    # Carrito no debe agregar items
    assert len(cart.items) == 0

    # Toal debe permanecer en cero
    assert cart.total == 0

# test total inicial carrito vacio 

def test_empty_cart_initial_state():
    # Crear una nueva instancia del carrito de compras.
    # Al iniciar, el carrito debe estar vacío.
    cart = ShoppingCart()

    # Verificar que el total inicial sea 0.
    # Esto confirma que no hay costos acumulados sin agregar productos.
    assert cart.total == 0 

    # Verificar que la lista de items esté vacía al inicio.
    # Esto asegura que no hay productos almacenados incorrectamente.
    assert cart.items == []