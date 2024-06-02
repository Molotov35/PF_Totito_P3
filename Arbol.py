import json
import random
import graphviz

class nodoArbol:
    def __init__(self, valor, poscision, nombre, profundidad, anterior=None):
        self.anterior = anterior
        self.siguiente = []
        self.nombre= nombre
        self.valor = valor
        self.poscision = poscision 
        self.profundidad = profundidad

class ARBOL:
    def __init__(self):
        self.raiz = nodoArbol(0,0,"0",0)
        self.ubicacion = self.raiz
        self.busqueda= self.raiz

    def ubicaciones(self):
        print("\n")
        print("ubicacion: " + str(self.ubicacion.poscision)+ " - " + str(self.ubicacion.valor))
        print("nombre: " + str(self.ubicacion.nombre))
        if not self.ubicacion.anterior==None:
            print("anterior: " + str(self.ubicacion.anterior.valor))
        else:
            print("SIN VALOR ANTERIOR")
            
        print("valores siguientes: ")
        for x in self.ubicacion.siguiente:
            print(str(x.poscision)+"\t" +str(x.valor))
        print()
        
    def asignarValores(self, ganador=None):
        if self.ubicacion.siguiente==[] :
            if ganador:
                self.ubicacion.valor=1
            else:
                self.ubicacion.valor=0
            if ganador==None:
                self.ubicacion.valor=0.5
            self.ubicacion=self.ubicacion.anterior
            self.asignarValores(ganador)
        else:
            if self.ubicacion.anterior is not None:
                self.ubicacion.valor=self.evaluarArbol()
                self.ubicacion=self.ubicacion.anterior
                self.asignarValores(ganador)

    def sumValores(self):
        valor=0
        for x in self.ubicacion.siguiente:
            valor=valor+x.valor
        return valor

    def insert(self, valor, poscision):
        self.busqueda=self.ubicacion
        nombre=self.generarNombre(poscision)
        self.ubicacion=nodoArbol(valor, poscision, nombre, self.ubicacion.profundidad+1,  self.ubicacion)
        self.ubicacion.anterior.siguiente.append(self.ubicacion)
    

    def generarNombre(self,poscision):
        if self.busqueda.anterior is not None:
            ant=self.busqueda.poscision
            self.busqueda=self.busqueda.anterior
            return (str(self.generarNombre(ant)) + str(poscision))  
        return ("0" + str(poscision))  
            
    

    def volver(self):
        self.ubicacion=self.ubicacion.anterior 
        
    def avanzar(self, poscision):
        for x in self.ubicacion.siguiente:
            if int(x.poscision)==int(poscision):
                self.ubicacion=x
                return True
        return False
    
    def eliminar(self, poscision):
        cont=0
        for x in self.ubicacion.siguiente:
            if int(x.poscision)==int(poscision):
                self.ubicacion.siguiente.pop(cont)
            cont=cont+1
        return 0
            
    def existe(self, poscision):
        for x in self.ubicacion.siguiente:
            if int(x.poscision)==int(poscision):
                return x.poscision
        return 0
    
    def buscaOpc(self):
        posicion=0
        div=0
        max=0.75
        # max=100-100/self.ubicacion.profundidad
        probabilidades=[]
        disponibles=[]
        cantSig=len(self.ubicacion.siguiente)
        for x in range(1,10):
            for y in self.ubicacion.nombre:
                if x==int(y):
                    break
            else:
                disponibles.append(x)
        if cantSig<9-self.ubicacion.profundidad:
            for x in disponibles:
                if self.existe(x)==0:
                    posicion=x
                    break  
            else:
                posicion=random.randint(1,9)
        else:
            if int(self.ubicacion.profundidad==0):
               div=1 
            else:
                div=int(self.ubicacion.profundidad)
                
            if div==1 :
            # if or random.randint(1,100)<=(8) :
                posicion=random.choice(disponibles)
                print("aleatorio")
            else:
                # for x in self.ubicacion.siguiente:
                #     if x.valor>max:
                #         # max=x.valor
                #         # posicion=x.poscision
                #         probabilidades.append(x.poscision)
                    contMax=0
                # if probabilidades==[]:
                    for x in self.ubicacion.siguiente:
                        if x.valor>contMax:
                            contMax=x.valor
                            posicion=x.poscision
                # else:
                #     posicion=random.choice(probabilidades)
            
        return posicion
    

  
    
    def  generar_arbol_grafico(self):
        dot = graphviz.Digraph()
        self._generar_arbol_grafico(self.ubicacion, dot)

        archivo_salida = "arbol"
        dot.render(archivo_salida, format='png', cleanup=True, view=True)

        

    def _generar_arbol_grafico(self, nodo, dot):
        if nodo is not None:
            dot.node(str(nodo.nombre), str(nodo.poscision)+"  -  "+str(nodo.valor) + "    -    "+str(nodo.profundidad))
            for x in nodo.siguiente:
                dot.node(str(x.nombre), str(x.poscision)+"  -  "+str(nodo.valor))
                dot.edge(str(nodo.nombre), str(x.nombre))
                self._generar_arbol_grafico(x, dot)
    
    def generarJson(self, nodo):
        self.busqueda=nodo
        array=[self.busqueda.valor, self.busqueda.poscision, self.busqueda.nombre, self.busqueda.profundidad, []]
        for x in nodo.siguiente:
            array[4].append(self.generarJson(x))
        return array
    
    def generarArbolDeJson(self):
        self.raiz.siguiente=[]
        self.ubicacion=self.raiz
        self.busqueda=self.raiz
        return self._generarArbolDeJson(json.load(open('arbol.json','r')))
    

    def _generarArbolDeJson(self, array, nodoAnt=False):
        if nodoAnt:
            if not self.avanzar(array[1]):
                self.insert(array[0],array[1])
            for x in array[4]:
                
                self._generarArbolDeJson(x, True)
                self.ubicacion=self.ubicacion.anterior
        else:
            self.raiz.valor=array[0]
            for x in array[4]:
                self._generarArbolDeJson(x, True)
                self.ubicacion=self.ubicacion.anterior

    def _asignarValores(self, nodo):
        self.ubicacion=nodo
        if not nodo.siguiente ==[]:
            self.ubicacion.valor=self.evaluarArbol()
            for x in nodo.siguiente:
                self._asignarValores(x)
    
    def  evaluarArbol(self):
        self.busqueda=self.ubicacion
        return 1-(self._evaluarArbol(self.busqueda)/self._evaluarHojas(self.busqueda))

    def _evaluarArbol(self, nodo):        
        cantidad=0
        if nodo.siguiente==[] and nodo.valor==0:
            return 1
        for x in nodo.siguiente:
            cantidad=cantidad+self._evaluarArbol(x)
        return cantidad
    
    def _evaluarHojas(self, nodo):
        cantidad=0
        if nodo.siguiente==[]:
            cantidad=cantidad+1
        else:
            for x in nodo.siguiente:
                cantidad=cantidad+self._evaluarHojas(x)
        return cantidad
    

