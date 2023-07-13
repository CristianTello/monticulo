class MonticuloMaximo:
    def __init__(self):
        self.monticulo = []

    def insertar(self, elemento):
        self.monticulo.append(elemento)
        self._subir_elemento(len(self.monticulo) - 1)

    def eliminar_elemento(self, elemento):
        if elemento in self.monticulo:
            indice = self.monticulo.index(elemento)
            ultimo_elemento = self.monticulo.pop()
            if indice < len(self.monticulo):
                self.monticulo[indice] = ultimo_elemento
                self._bajar_elemento(indice)
            return elemento
        else:
            return None

    def _subir_elemento(self, indice):
        padre = (indice - 1) // 2
        while indice > 0 and self.monticulo[indice] > self.monticulo[padre]:
            self.monticulo[indice], self.monticulo[padre] = self.monticulo[padre], self.monticulo[indice]
            indice = padre
            padre = (indice - 1) // 2

    def _bajar_elemento(self, indice):
        hijo_izquierdo = 2 * indice + 1
        hijo_derecho = 2 * indice + 2
        maximo = indice

        if hijo_izquierdo < len(self.monticulo) and self.monticulo[hijo_izquierdo] > self.monticulo[maximo]:
            maximo = hijo_izquierdo
        if hijo_derecho < len(self.monticulo) and self.monticulo[hijo_derecho] > self.monticulo[maximo]:
            maximo = hijo_derecho

        if maximo != indice:
            self.monticulo[indice], self.monticulo[maximo] = self.monticulo[maximo], self.monticulo[indice]
            self._bajar_elemento(maximo)

    def esta_vacio(self):
        return len(self.monticulo) == 0
    

    def recorrer_preorden(self):
        self._recorrer_preorden_aux(0)

    def _recorrer_preorden_aux(self, indice):
        if indice < len(self.monticulo):
            print(self.monticulo[indice], end=" ")
            self._recorrer_preorden_aux(2 * indice + 1)
            self._recorrer_preorden_aux(2 * indice + 2)

    def recorrer_por_niveles(self):
        for i in range(len(self.monticulo)):
            print(self.monticulo[i], end=" ")
        print()


new_monticulo=MonticuloMaximo()

new_monticulo.insertar(5)
new_monticulo.insertar(8)
new_monticulo.insertar(10)
new_monticulo.insertar(3)
new_monticulo.insertar(7)

print("Monticulo insertado: ",new_monticulo.monticulo)

new_monticulo.eliminar_elemento(8)

print("Elemento eliminado", new_monticulo.monticulo)

new_monticulo.insertar(6)
new_monticulo.insertar(9)

print("Monticulo agregado", new_monticulo.monticulo)

print("Recorrido en preorden:")
new_monticulo.recorrer_preorden()

print("\nRecorrido por niveles:")
new_monticulo.recorrer_por_niveles()