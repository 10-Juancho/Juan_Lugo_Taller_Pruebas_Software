class FileSystem:
    # Clase FileSystem que representa un sistema simple para manejar archivos

    def __init__(self):

        # Constructor de la clase
        # Inicializa una lista vacía donde se almacenarán los archivos

        self.files = []

    def add_file(self, file):
        
        # Método para agregar un archivo al sistema
        # 'file' representa el archivo que se desea guardar
        # El archivo se añade a la lista 'files'

        self.files.append(file)