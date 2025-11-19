# 🛒 PRUEBA DE SISTEMA - SISTEMA DE COMPRAS.
Este documento describe las pruebas realizadas sobre el modulo de compras,cuyo objetivo es verificar el comportamiento completo del flujo de la compra:

- Agregar productos al carrito.
- Calcular el total.
- Actualizar el stock correctamente.
- Validar el  estado del carrito.

Estas pruebas se enfocan en evluar el **funcionamiento integrado** del sistema, asegurando que todos los componentes trabajen juntos de manera adecuada.

## 🧱 COMPONENTES DEL SISTEMA.

> class product -> Representa un producto disponible para la compra.

Atributos principales:
- **name** -> nombre del producto.
- **price** -> precio unitario.
- **stock** -> camtidad disponible.

> class ShoppingCart -> Representa el carrito de compras del usuario.

Métodos clave:
- **add_item(product, quantity)** -> Añade productos al carrito si hay stock disponible.
- **items** -> Lista de porductos agregados.
- **total** -> monto total acumulado.

## 🧪 PRUEBAS DEL SISTEMA IMPLEMENTADAS.

Test de flujo.
```Python
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
```

> Validando:<br>
- Se agregan los productos correctamente.
- El total se calcula correctamente.
- El Stock disminuye adecuadamente.

Test cuando no hay Stock suficiente.
```Python
def test_cannot_add_iteam_with_zero_stock ():
    # Creando el producto
    book = Product ("book",20,0)

    #Creando el carrito     
    cart = ShoppingCart()

    #  Intentar agregar un producto sin stock
    assert cart.add_item (book,1) is False
    assert book.stock == 0 
    assert cart.total == 0
```
> Validando: <br>
- El sistema no realiza compras con Stock insuficiente.

Test estado inicial del carrito.
```Python
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
```
> Validando : <br>
- El carrito inicia siempre en un estado limpio.

Test Negativo.
```Python
def test_cannot_add_more_than_stock ():
    # Creando el producto
    ps5 = Product ("ps5", 3000,5)

    # Crea el carrito
    cart = ShoppingCart ()

    # Intentar comprar más del stock 
    assert cart.add_item ( ps5, 6) is False

    # Stock debe mantenerse igual 
    assert ps5.stock == 5

    # Carrito no debe agregar ningun item
    assert len(cart.items) == 0

    # Toal debe permanecer en cero
    assert cart.total == 0
```
> Validacion: <br>
- El sistma rechaza compras mayores al stock.
- No se descuente el stock cuando la compra sea invalidada.
- El total no cambia.
- El carrito continue vacio despues del intento.

Con estas pruebas, es un paso para ver el comportamiento general del sistema de compras sea confiable y alineado a los requsitos funcionales.
