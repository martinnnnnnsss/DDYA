def maximizar_rendimiento_estudiantes(n, valores_por_tama):
    dp = [0.0] * (n + 1)
    
    for i in range(1, n + 1):
        max_rendimiento = 0.0
        
        for j in range(1, i + 1):
            
            rendimiento_actual = valores_por_tama[j] + dp[i - j]
            if rendimiento_actual > max_rendimiento:
                max_rendimiento = rendimiento_actual        
        
        dp[i] = max_rendimiento
        
    return dp[n], dp
total_estudiantes = 5

rendimientos_V = [0.0, 1.5, 4.2, 5.8, 7.5, 8.1] 

rendimiento_maximo, tabla_dp = maximizar_rendimiento_estudiantes(total_estudiantes, rendimientos_V)

print(f"Rendimiento maximo posible para {total_estudiantes} estudiantes: {rendimiento_maximo}")
print(f"Tabla de estados DP calculados: {tabla_dp}")

import unittest

# Tu función original
def maximizar_rendimiento_estudiantes(n, valores_por_tamano):
    dp = [0.0] * (n + 1)
    for i in range(1, n + 1):
        max_rendimiento = 0.0
        for j in range(1, i + 1):
            rendimiento_actual = valores_por_tamano[j] + dp[i - j]
            if rendimiento_actual > max_rendimiento:
                max_rendimiento = rendimiento_actual        
        dp[i] = max_rendimiento
    return dp[n], dp


class TestMaximizarRendimiento(unittest.TestCase):

    def test_01_ejemplo_original(self):
        # El caso que pusiste de ejemplo. La mejor combinación es 2 + 2 + 1 (4.2 + 4.2 + 1.5 = 9.9)
        n = 5
        valores = [0.0, 1.5, 4.2, 5.8, 7.5, 8.1]
        max_rend, dp = maximizar_rendimiento_estudiantes(n, valores)
        self.assertAlmostEqual(max_rend, 9.9)

    def test_02_mejor_individuales(self):
        # Los grupos de 1 son los más eficientes. 4 estudiantes = 4 * 3.0 = 12.0
        n = 4
        valores = [0.0, 3.0, 5.0, 7.0, 9.0]
        max_rend, dp = maximizar_rendimiento_estudiantes(n, valores)
        self.assertEqual(max_rend, 12.0)

    def test_03_mejor_todos_juntos(self):
        # Hay un bono masivo si los 3 están juntos.
        n = 3
        valores = [0.0, 1.0, 2.0, 10.0]
        max_rend, dp = maximizar_rendimiento_estudiantes(n, valores)
        self.assertEqual(max_rend, 10.0)

    def test_04_cero_estudiantes(self):
        # Caso límite: 0 estudiantes debe retornar rendimiento 0.0.
        n = 0
        valores = [0.0]
        max_rend, dp = maximizar_rendimiento_estudiantes(n, valores)
        self.assertEqual(max_rend, 0.0)

    def test_05_un_solo_estudiante(self):
        # Caso límite mínimo de estudiantes viables.
        n = 1
        valores = [0.0, 5.5]
        max_rend, dp = maximizar_rendimiento_estudiantes(n, valores)
        self.assertEqual(max_rend, 5.5)

    def test_06_rendimientos_nulos(self):
        # Si por alguna razón ninguna configuración da rendimiento.
        n = 3
        valores = [0.0, 0.0, 0.0, 0.0]
        max_rend, dp = maximizar_rendimiento_estudiantes(n, valores)
        self.assertEqual(max_rend, 0.0)

    def test_07_pico_en_grupo_intermedio(self):
        # El grupo de 2 es extremadamente bueno. Para 5 estudiantes: 2 + 2 + 1 = 100 + 100 + 1 = 201
        n = 5
        valores = [0.0, 1.0, 100.0, 1.0, 1.0, 1.0]
        max_rend, dp = maximizar_rendimiento_estudiantes(n, valores)
        self.assertEqual(max_rend, 201.0)

    def test_08_multiplos_exactos(self):
        # Grupos de 3 dan 10.0. Seis estudiantes deberían formar dos grupos de 3 (20.0).
        n = 6
        valores = [0.0, 2.0, 5.0, 10.0, 11.0, 12.0, 14.0]
        max_rend, dp = maximizar_rendimiento_estudiantes(n, valores)
        self.assertEqual(max_rend, 20.0)

    def test_09_rendimientos_decrecientes(self):
        # Mientras más grande el grupo, menor es el aumento marginal. Mejor todos de 1.
        n = 4
        valores = [0.0, 10.0, 15.0, 18.0, 20.0]
        max_rend, dp = maximizar_rendimiento_estudiantes(n, valores)
        self.assertEqual(max_rend, 40.0)

    def test_10_lista_valores_mas_larga_que_n(self):
        # Si pasamos una tabla de rendimientos más larga que 'n', el código no debe fallar 
        # y debe usar solo hasta el índice necesario.
        n = 2
        valores = [0.0, 2.0, 6.0, 20.0, 50.0] # 20 y 50 deben ser ignorados
        max_rend, dp = maximizar_rendimiento_estudiantes(n, valores)
        self.assertEqual(max_rend, 6.0)

unittest.main()