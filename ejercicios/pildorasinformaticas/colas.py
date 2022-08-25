import queue

miCola = queue.Queue()

miCola.put("Madrid")
miCola.put("Bogota")
miCola.put("Mexico")

print(miCola.get())
print("A continuacion se imprimen los elementos restantes en la cola")

for elemento in miCola.queue:

    print(elemento)


#.queue entra primero sale primero
#.LifoQueue entra primero sale ultimo
#.PriorityQuere() sale la prioridad, se le debe asignarla prioridad al elemento al ingresarlo