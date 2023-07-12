class Producto:
    #Constructor e inicializar atributos de la instancia
    def __init__(self, codigo, descripcion, cantidad, precio):
        self.codigo = codigo      
        self.descripcion = descripcion
        self.cantidad = cantidad
        self.precio = precio
    
    #Metodo para modificar productos
    def modificar(self, nueva_descripcion, nueva_cantidad, nuevo_precio):
        self.descripcion = nueva_descripcion
        self.cantidad = nueva_cantidad
        self.precio = nuevo_precio



#Programa Principal
producto = Producto (1, 'Teclado USB 101 teclas', 10, 4500)
#Mostrando los atributos del objeto
print(f'{producto.codigo} | {producto.descripcion} | {producto.cantidad} | {producto.precio}' )
#Modificar los datos
producto.modificar('Telclado Mécanico USB', 20, 4800)
print(f'{producto.codigo} | {producto.descripcion} | {producto.cantidad} | ')