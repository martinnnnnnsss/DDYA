def PromedioEstudiantes():
    estudiantes = [
    ( "Martin", 5.0 ),
    ( "Isabella", 1.0 ),
    ( "Juan", 2.5 ),
    ( "Felipe", 4.0 ),
    ( "Dana", 3.5 ),
    ( "Daniel", 2.9 ),
    ( "Mateo", 3.3 ),
    ( "Juana", 5.0 ),
    ( "Sara", 1.5 ),
    ( "Santiago", 3.8 ),
    ( "Luis", 4.1 )
    ]

    a = len(estudiantes)
    suma = 0

    for estudiante in estudiantes:
        suma += estudiante[1]
    promedio = suma / a

    print ("Este fue el promedio de los estudiantes:", promedio)
    print (" Estos son los estudiantes que tuvieron un promedio positivo:" )

    for estudiante in estudiantes:
        if estudiante[1] > promedio:
            print( estudiante [0] )

PromedioEstudiantes ()
