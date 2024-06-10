class TreeNode:
    # Definimos el constructor
    def __init__(self, node_name, weight):
        # Inicializamos el nodo con el nombre que le hayamos dado en Tree
        self.node_name = node_name
        # El nodo tendrá un array vacío de hijos por defecto
        self.children = []
        # Le añadimos un peso como objetivo del paso 1.2
        self.weight = weight

    # Para añadir a un hijo, declaramos el parámetro de sí mismo y el nuevo hijo a añadir
    def add_child(self, new_child):
        # Lo añadimos al array self.children
        self.children.append(new_child)

class Tree:
    # Inicializamos el árbol con un nodo raíz, añadiendo el peso del paso 1.2
    def __init__(self, root_name, root_weight):
        # Creamos el TreeNode, añadiendo aparte del nombre, el peso del paso 1.2 para que pueda aceptar los pesos para los nodos
        self.root = TreeNode(root_name, root_weight)
    
    # Intentamos encontrar el nodo en base a la clase Tree, el nodo a partir del cual se inicia la búsqueda y el nodo que buscamos
    def find_node(self, current_node, node_name):
        # Encontramos el nodo en base a un condicional
        if current_node.node_name == node_name:
            return current_node
        # En caso de que no coincida, iteramos sobre los hijos del nodo actual para tratar de encontrar el nodo que buscamos ahí
        for child in current_node.children:
            # Se llama de manera recursiva a find_node para ir pasando por todos los hijos para ver si coincide algún nombre ahí
            found_node = self.find_node(child, node_name)
            # En caso de que coincida el nodo que se está buscando con su nombre, se devuelve el nodo, por la contra se sigue iterando a los nodos y sus hijos
            if found_node:
                return found_node
        # En caso de que después de todas las iteraciones no se haya encontrado el nodo, se devolverá None
        return None
            

    # Para añadir el hijo, enfocamos a Tree, seleccionamos el TreeNode, y el hijo que queremos introducir, así como su peso para la parte 1.2
    def add_child(self, parent_name, child_name, child_weight):
        # Declaramos una variable para que busque el nodo parent_name desde el self.root, y en cuanto encuentre uno que coincida, lo guarde aquí
        node_parent = self.find_node(self.root, parent_name)
        # Si el nodo se ha encontrado y existe...
        if node_parent:
            # Guardamos en una variable el nuevo nodo a añadir que se ha recibido en el parámetro, creándolo como objeto. Actualizamos y añadimos el peso como parte de lo indicado en la sección 1.2
            new_child = TreeNode(child_name, child_weight)
            node_parent.add_child(new_child)
        # En el caso de no encontrar el nodo que le estamos pasando, imprimimos en la consola un mensaje de error
        else:
            print("Parent node not found.")

    # Muestra todo el contenido del árbol de manera jerárquica
    def display(self):
        # Configuración para que salga el árbol en la consola de manera adecuada. Node es el nodo actual que se imprime, level es el nivel de profundidad del nodo, que se refleja en la indentación
        def display_node(node, level):
            # Se establece un print con un espacio multiplicado por el nivel para generar la indentación correspondiente junto al nombre. Se debe de poner el print antes porque si no sale al revés
            print(" " * level + node.node_name)
            # Se iteran recursivamente todos los child del nodo actual para que la indentación sea un poco más profunda en función del nivel en el que están
            for child in node.children:
                display_node(child, level + 1)
        # Establecemos de forma predeterminada que el root debe de estar a nivel 0
        display_node(self.root, 0)

    # Función para encontrar la ruta con mayor peso, para cumplir el paso 1.2
    def find_heaviest_path(self):
        # Después de la llamada inicial a la función localizada más abajo con self.root, definimos una función auxiliar recursiva para poder iterar sobre los hijos de self.root
        def find_path(node):
            # Si el nodo no tiene hijos, devuelve un array con el valor del nodo y su peso
            if not node.children:
                return ([node.node_name], node.weight)
            # Antes de la recursión, definimos dos variables: la que guardará el camino más pesado y inicializamos una variable de peso máximo en 0 para guardar la acumulación del peso máximo
            heaviest_path = []
            max_weight = 0

            # En el caso de que sí que haya hijos, iteramos sobre los hijos del nodo actual, en este caso, root. Iteramos, según los parámetros, a child1 y child2
            for child in node.children:
                # Llamamos recursivamente a find_path() para cada hijo del hijo llamado justo arriba, obteniendo el path y el weight de cada child en desestructuración.
                path, weight = find_path(child)
                # Si el peso obtenido en el paso anterior es mayor que el max_weight actual, sobrescribimos tanto el max_weight como el array que representa el camino
                if weight > max_weight:
                    max_weight = weight
                    heaviest_path = path
            # Devolvemos un array con el nodo padre y los hijos guardados en el array de heaviest_path, y el peso del nodo padre sumado al peso de los hijos. Eso provoca un array unido al sumar strings y un solo número al sumar los números que devuelve el camino más pesado
            return ([node.node_name] + heaviest_path, node.weight + max_weight)

        # Llamada inicial a la función find_path() desde el root como parámetro buscando path y weight de manera desestructurada
        path, weight = find_path(self.root)
        # Devolvemos tanto el camino más pesado como su peso total en base a las variables que hemos conseguido arriba por desestructuración
        return path, weight 

# Prueba
tree = Tree("root", 10)
tree.add_child("root", "child1", 5)
tree.add_child("root", "child2", 15)
tree.add_child("child1", "child1_1", 10)
tree.add_child("child1", "child1_2", 5)
tree.add_child("child2", "child2_1", 10)
tree.add_child("child2", "child2_2", 20)

tree.display()
print("Heaviest Path:", tree.find_heaviest_path())