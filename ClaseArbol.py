from collections import defaultdict
from Nodo import Nodo

class Arbol:
    def __init__(self):
        self.raiz = None
        self.traversal = []

    def agregar_recursivo(self, nodo:Nodo, valor):
        if self.raiz == None:
            self.raiz = Nodo(valor)
        elif valor < nodo.valor:
            if nodo.izquierda == None:
                nodo.izquierda = Nodo(valor)
            else:
                self.agregar_recursivo(nodo.izquierda, valor)
        else:
            if nodo.derecha == None:
                nodo.derecha = Nodo(valor)
            else:
                self.agregar_recursivo(nodo.derecha, valor)
    
    def buscar_nodo(self, nodo:Nodo, valor_buscado):
        if nodo == None:
            return
        elif nodo.valor == valor_buscado:
            return nodo
        if valor_buscado < nodo.valor:
            return self.buscar_nodo(nodo.izquierda, valor_buscado)
        else:
            return self.buscar_nodo(nodo.derecha, valor_buscado)
    
    def agregar(self, valor):
        self.agregar_recursivo(self.raiz, valor)
        
    def inorder(self):
        inorder = []
        def traversal(node: Nodo):
            if node != None:
                traversal(node.izquierda)
                inorder.append(node.valor)
                traversal(node.derecha)
        traversal(self.raiz)
        self.traversal = inorder

    def preorder(self):
        preorder = []
        def traversal(node: Nodo):
            if node != None:
                preorder.append(node.valor)
                traversal(node.izquierda)
                traversal(node.derecha)
        traversal(self.raiz)
        self.traversal = preorder

    def postorder(self):
        postorder = []
        def traversal(node: Nodo):
            if node != None:
                traversal(node.izquierda)
                traversal(node.derecha)
                postorder.append(node.valor)
        traversal(self.raiz)
        self.traversal = postorder
            
    def amplitud(self):
        route = defaultdict(list) # Crea el manejador de datos
        
        def dfs(node:Nodo, level): # Funcion encargada de añadir los valores al manejador
            route[level].append(node.valor) 
            # LLamado recursivo por cada hijo
            if node.izquierda != None:
                dfs(node.izquierda,level+1)
            if node.derecha != None: 
                dfs(node.derecha, level+1)
    
        dfs(self.raiz, 0) # Primer llamado
        self.traversal = [ans for k,ans in sorted(route.items())]
        return [ans for k,ans in sorted(route.items())] 

    