import numpy as np
import math
from typing import Dict, List, Tuple

# CAPÍTULO 3: ERRORES DE REDONDEO

def cap3_1_cifras_significativas() -> Dict:
    """3.1 Cifras significativas - R_eq con diferentes niveles de precisión"""
    R1, R2 = 100, 220
    valor_exacto = (R1 * R2) / (R1 + R2)
    
    resultados = []
    cifras_list = [1, 2, 3, 4, 5]
    
    for cifras in cifras_list:
        R_eq = round(valor_exacto, cifras)
        error = abs((R_eq - valor_exacto) / valor_exacto * 100)
        resultados.append({
            'cifras': cifras,
            'R_eq': R_eq,
            'error': error
        })
    
    return {
        'titulo': '3.1 Cifras Significativas',
        'formula': 'R_eq = (R1×R2)/(R1+R2)',
        'valor_exacto': valor_exacto,
        'resultados': resultados,
        'datos_grafica': {
            'x': [r['cifras'] for r in resultados],
            'y': [r['error'] for r in resultados],
            'xlabel': 'Número de Cifras',
            'ylabel': 'Error (%)',
            'tipo': 'linea'
        },
        'excel': '=ROUND((100*220)/(100+220), cifras)'
    }

def cap3_2_exactitud_precision() -> Dict:
    """3.2 Exactitud vs Precisión - Mediciones repetidas"""
    valor_real = 68.75  # R_eq exacto
    mediciones = [68.2, 68.9, 68.3, 68.7, 68.4, 68.8, 68.5, 68.6, 68.7, 68.5]
    
    resultados = []
    for i, medicion in enumerate(mediciones, 1):
        error = abs(medicion - valor_real)
        resultados.append({
            'iteracion': i,
            'medido': medicion,
            'real': valor_real,
            'error': error
        })
    
    return {
        'titulo': '3.2 Exactitud vs Precisión',
        'formula': 'Error = |Valor_medido - Valor_real|',
        'valor_exacto': valor_real,
        'resultados': resultados,
        'datos_grafica': {
            'x': [r['medido'] for r in resultados],
            'y': [r['real'] for r in resultados],
            'xlabel': 'Valor Medido (Ω)',
            'ylabel': 'Valor Real (Ω)',
            'tipo': 'scatter'
        },
        'excel': '=ABS(medido - real)'
    }

def cap3_3_error_absoluto() -> Dict:
    """3.3 Error Absoluto - Iteraciones de cálculo"""
    valor_exacto = 68.75
    aproximaciones = [70, 69, 68.8, 68.76, 68.751, 68.7501]
    
    resultados = []
    for i, aprox in enumerate(aproximaciones, 1):
        error_abs = abs(aprox - valor_exacto)
        resultados.append({
            'iteracion': i,
            'aproximacion': aprox,
            'error_absoluto': error_abs
        })
    
    return {
        'titulo': '3.3 Error Absoluto',
        'formula': 'Error_absoluto = |Aproximación - Valor_exacto|',
        'valor_exacto': valor_exacto,
        'resultados': resultados,
        'datos_grafica': {
            'x': [r['iteracion'] for r in resultados],
            'y': [r['error_absoluto'] for r in resultados],
            'xlabel': 'Iteración',
            'ylabel': 'Error Absoluto',
            'tipo': 'bar'
        },
        'excel': '=ABS(aproximacion - valor_exacto)'
    }

def cap3_4_error_relativo() -> Dict:
    """3.4 Error Relativo"""
    valor_exacto = 68.75
    aproximaciones = [70, 69, 68.8, 68.76, 68.751, 68.7501]
    
    resultados = []
    for i, aprox in enumerate(aproximaciones, 1):
        error_rel = abs((aprox - valor_exacto) / valor_exacto)
        resultados.append({
            'iteracion': i,
            'aproximacion': aprox,
            'error_relativo': error_rel
        })
    
    return {
        'titulo': '3.4 Error Relativo',
        'formula': 'Error_relativo = |Aproximación - Valor_exacto| / Valor_exacto',
        'valor_exacto': valor_exacto,
        'resultados': resultados,
        'datos_grafica': {
            'x': [r['iteracion'] for r in resultados],
            'y': [r['error_relativo'] for r in resultados],
            'xlabel': 'Iteración',
            'ylabel': 'Error Relativo',
            'tipo': 'linea'
        },
        'excel': '=ABS((aproximacion - valor_exacto) / valor_exacto)'
    }

def cap3_5_error_porcentual() -> Dict:
    """3.5 Error Porcentual"""
    valor_exacto = 68.75
    aproximaciones = [70, 69, 68.8, 68.76, 68.751, 68.7501]
    
    resultados = []
    for i, aprox in enumerate(aproximaciones, 1):
        error_pct = abs((aprox - valor_exacto) / valor_exacto * 100)
        resultados.append({
            'iteracion': i,
            'aproximacion': aprox,
            'error_porcentual': error_pct
        })
    
    return {
        'titulo': '3.5 Error Porcentual',
        'formula': 'Error_% = |Aproximación - Valor_exacto| / Valor_exacto × 100',
        'valor_exacto': valor_exacto,
        'resultados': resultados,
        'datos_grafica': {
            'x': [r['iteracion'] for r in resultados],
            'y': [r['error_porcentual'] for r in resultados],
            'xlabel': 'Iteración',
            'ylabel': 'Error (%)',
            'tipo': 'linea'
        },
        'excel': '=ABS((aproximacion - valor_exacto) / valor_exacto * 100)'
    }

def cap3_6_comparativa_errores() -> Dict:
    """3.6 Comparativa de tipos de errores"""
    valor_exacto = 68.75
    aproximaciones = [70, 69, 68.8, 68.76, 68.751, 68.7501]
    
    resultados = []
    for i, aprox in enumerate(aproximaciones, 1):
        error_abs = abs(aprox - valor_exacto)
        error_rel = abs((aprox - valor_exacto) / valor_exacto)
        error_pct = error_rel * 100
        
        resultados.append({
            'iteracion': i,
            'aproximacion': aprox,
            'error_absoluto': error_abs,
            'error_relativo': error_rel,
            'error_porcentual': error_pct
        })
    
    return {
        'titulo': '3.6 Comparativa de Errores',
        'formula': 'Comparación de error absoluto, relativo y porcentual',
        'valor_exacto': valor_exacto,
        'resultados': resultados,
        'datos_grafica': {
            'x': [r['iteracion'] for r in resultados],
            'y1': [r['error_absoluto'] for r in resultados],
            'y2': [r['error_relativo'] for r in resultados],
            'y3': [r['error_porcentual'] for r in resultados],
            'xlabel': 'Iteración',
            'ylabel': 'Valor del Error',
            'tipo': 'multiple'
        },
        'excel': 'Ver métodos 3.3, 3.4 y 3.5'
    }

def cap3_7_error_redondeo() -> Dict:
    """3.7 Error de Redondeo Acumulado"""
    # Operaciones sucesivas con redondeo
    operaciones = [
        {'nombre': 'Inicio', 'valor': 100.0},
        {'nombre': '÷ 3', 'valor': 100.0 / 3},
        {'nombre': '× 3', 'valor': (100.0 / 3) * 3},
        {'nombre': '÷ 7', 'valor': ((100.0 / 3) * 3) / 7},
        {'nombre': '× 7', 'valor': (((100.0 / 3) * 3) / 7) * 7},
    ]
    
    resultados = []
    for i, op in enumerate(operaciones):
        if i == 0:
            error_acum = 0
        else:
            error_acum = abs(op['valor'] - operaciones[0]['valor'])
        
        resultados.append({
            'operacion': op['nombre'],
            'valor': round(op['valor'], 6),
            'error_acumulado': error_acum
        })
    
    return {
        'titulo': '3.7 Error de Redondeo Acumulado',
        'formula': 'Error acumulado en operaciones sucesivas',
        'valor_exacto': 100.0,
        'resultados': resultados,
        'datos_grafica': {
            'x': [r['operacion'] for r in resultados],
            'y': [r['error_acumulado'] for r in resultados],
            'xlabel': 'Operación',
            'ylabel': 'Error Acumulado',
            'tipo': 'bar'
        },
        'excel': '=ABS(valor_actual - valor_inicial)'
    }

# CAPÍTULO 17: REGRESIÓN

def cap17_1_regresion_lineal() -> Dict:
    """17.1 Regresión Lineal - Presión vs Temperatura"""
    # Datos de presión vs temperatura en reactor
    temperatura = np.array([20, 40, 60, 80, 100, 120, 140])
    presion = np.array([2.1, 3.8, 5.9, 8.2, 10.7, 13.1, 15.8])
    
    # Regresión lineal: y = mx + b
    n = len(temperatura)
    m = (n * np.sum(temperatura * presion) - np.sum(temperatura) * np.sum(presion)) / \
        (n * np.sum(temperatura**2) - np.sum(temperatura)**2)
    b = (np.sum(presion) - m * np.sum(temperatura)) / n
    
    presion_pred = m * temperatura + b
    error = np.sqrt(np.mean((presion - presion_pred)**2))
    r2 = 1 - (np.sum((presion - presion_pred)**2) / np.sum((presion - np.mean(presion))**2))
    
    resultados = []
    for i in range(len(temperatura)):
        resultados.append({
            'temperatura': float(temperatura[i]),
            'presion_real': float(presion[i]),
            'presion_pred': round(float(presion_pred[i]), 2),
            'error': float(abs(presion[i] - presion_pred[i]))
        })
    
    return {
        'titulo': '17.1 Regresión Lineal',
        'formula': f'P = {m:.4f}T + {b:.4f}',
        'valor_exacto': f'R² = {r2:.4f}',
        'parametros': {'pendiente': float(m), 'intercepto': float(b)},
        'resultados': resultados,
        'datos_grafica': {
            'x': temperatura.tolist(),
            'y_real': presion.tolist(),
            'y_pred': presion_pred.tolist(),
            'xlabel': 'Temperatura (°C)',
            'ylabel': 'Presión (bar)',
            'tipo': 'regresion'
        },
        'excel': f'=({m:.4f}*A2)+{b:.4f}'
    }

def cap17_2_regresion_polinomial_2() -> Dict:
    """17.2 Regresión Polinomial Grado 2"""
    temperatura = np.array([20, 40, 60, 80, 100, 120, 140])
    presion = np.array([2.1, 3.8, 5.9, 8.2, 10.7, 13.1, 15.8])
    
    # Ajuste polinomial grado 2
    coef = np.polyfit(temperatura, presion, 2)
    presion_pred = np.polyval(coef, temperatura)
    
    error = np.sqrt(np.mean((presion - presion_pred)**2))
    r2 = 1 - (np.sum((presion - presion_pred)**2) / np.sum((presion - np.mean(presion))**2))
    
    resultados = []
    for i in range(len(temperatura)):
        resultados.append({
            'temperatura': float(temperatura[i]),
            'presion_real': float(presion[i]),
            'presion_pred': round(float(presion_pred[i]), 2),
            'error': float(abs(presion[i] - presion_pred[i]))
        })
    
    return {
        'titulo': '17.2 Regresión Polinomial Grado 2',
        'formula': f'P = {coef[0]:.6f}T² + {coef[1]:.4f}T + {coef[2]:.4f}',
        'valor_exacto': f'R² = {r2:.4f}',
        'parametros': {'a': float(coef[0]), 'b': float(coef[1]), 'c': float(coef[2])},
        'resultados': resultados,
        'datos_grafica': {
            'x': temperatura.tolist(),
            'y_real': presion.tolist(),
            'y_pred': presion_pred.tolist(),
            'xlabel': 'Temperatura (°C)',
            'ylabel': 'Presión (bar)',
            'tipo': 'regresion_poli'
        },
        'excel': f'=({coef[0]:.6f}*A2^2)+({coef[1]:.4f}*A2)+{coef[2]:.4f}'
    }

def cap17_3_regresion_polinomial_3() -> Dict:
    """17.3 Regresión Polinomial Grado 3"""
    temperatura = np.array([20, 40, 60, 80, 100, 120, 140])
    presion = np.array([2.1, 3.8, 5.9, 8.2, 10.7, 13.1, 15.8])
    
    # Ajuste polinomial grado 3
    coef = np.polyfit(temperatura, presion, 3)
    presion_pred = np.polyval(coef, temperatura)
    
    error = np.sqrt(np.mean((presion - presion_pred)**2))
    r2 = 1 - (np.sum((presion - presion_pred)**2) / np.sum((presion - np.mean(presion))**2))
    
    resultados = []
    for i in range(len(temperatura)):
        resultados.append({
            'temperatura': float(temperatura[i]),
            'presion_real': float(presion[i]),
            'presion_pred': round(float(presion_pred[i]), 2),
            'error': float(abs(presion[i] - presion_pred[i]))
        })
    
    return {
        'titulo': '17.3 Regresión Polinomial Grado 3',
        'formula': f'P = {coef[0]:.8f}T³ + {coef[1]:.6f}T² + {coef[2]:.4f}T + {coef[3]:.4f}',
        'valor_exacto': f'R² = {r2:.4f}',
        'parametros': {'a': float(coef[0]), 'b': float(coef[1]), 'c': float(coef[2]), 'd': float(coef[3])},
        'resultados': resultados,
        'datos_grafica': {
            'x': temperatura.tolist(),
            'y_real': presion.tolist(),
            'y_pred': presion_pred.tolist(),
            'xlabel': 'Temperatura (°C)',
            'ylabel': 'Presión (bar)',
            'tipo': 'regresion_poli'
        },
        'excel': f'=({coef[0]:.8f}*A2^3)+({coef[1]:.6f}*A2^2)+({coef[2]:.4f}*A2)+{coef[3]:.4f}'
    }

def cap17_4_regresion_multiple() -> Dict:
    """17.4 Regresión Múltiple (3D) - Presión vs Temp y Tiempo"""
    temperatura = np.array([20, 40, 60, 80, 100, 120, 140])
    tiempo = np.array([1, 2, 3, 4, 5, 6, 7])
    presion = np.array([2.1, 3.8, 5.9, 8.2, 10.7, 13.1, 15.8])
    
    # Regresión múltiple: P = a*T + b*t + c
    X = np.column_stack([temperatura, tiempo, np.ones(len(temperatura))])
    coef = np.linalg.lstsq(X, presion, rcond=None)[0]
    
    presion_pred = X @ coef
    r2 = 1 - (np.sum((presion - presion_pred)**2) / np.sum((presion - np.mean(presion))**2))
    
    resultados = []
    for i in range(len(temperatura)):
        resultados.append({
            'temperatura': float(temperatura[i]),
            'tiempo': float(tiempo[i]),
            'presion_real': float(presion[i]),
            'presion_pred': round(float(presion_pred[i]), 2),
            'error': float(abs(presion[i] - presion_pred[i]))
        })
    
    return {
        'titulo': '17.4 Regresión Múltiple',
        'formula': f'P = {coef[0]:.4f}T + {coef[1]:.4f}t + {coef[2]:.4f}',
        'valor_exacto': f'R² = {r2:.4f}',
        'parametros': {'a_temp': float(coef[0]), 'b_tiempo': float(coef[1]), 'c': float(coef[2])},
        'resultados': resultados,
        'datos_grafica': {
            'x': temperatura.tolist(),
            'y': tiempo.tolist(),
            'z': presion.tolist(),
            'xlabel': 'Temperatura (°C)',
            'ylabel': 'Tiempo (h)',
            'zlabel': 'Presión (bar)',
            'tipo': '3d'
        },
        'excel': f'=({coef[0]:.4f}*A2)+({coef[1]:.4f}*B2)+{coef[2]:.4f}'
    }

def cap17_5_regresion_no_lineal() -> Dict:
    """17.5 Regresión No Lineal Exponencial"""
    temperatura = np.array([20, 40, 60, 80, 100, 120, 140])
    presion = np.array([2.1, 3.8, 5.9, 8.2, 10.7, 13.1, 15.8])
    
    # Ajuste exponencial: P = a * exp(b*T)
    # Linearizar: ln(P) = ln(a) + b*T
    ln_presion = np.log(presion)
    coef = np.polyfit(temperatura, ln_presion, 1)
    b = coef[0]
    a = np.exp(coef[1])
    
    presion_pred = a * np.exp(b * temperatura)
    r2 = 1 - (np.sum((presion - presion_pred)**2) / np.sum((presion - np.mean(presion))**2))
    
    resultados = []
    for i in range(len(temperatura)):
        resultados.append({
            'temperatura': float(temperatura[i]),
            'presion_real': float(presion[i]),
            'presion_pred': round(float(presion_pred[i]), 2),
            'error': float(abs(presion[i] - presion_pred[i]))
        })
    
    return {
        'titulo': '17.5 Regresión No Lineal Exponencial',
        'formula': f'P = {a:.4f} × exp({b:.6f}T)',
        'valor_exacto': f'R² = {r2:.4f}',
        'parametros': {'a': float(a), 'b': float(b)},
        'resultados': resultados,
        'datos_grafica': {
            'x': temperatura.tolist(),
            'y_real': presion.tolist(),
            'y_pred': presion_pred.tolist(),
            'xlabel': 'Temperatura (°C)',
            'ylabel': 'Presión (bar)',
            'tipo': 'exponencial'
        },
        'excel': f'={a:.4f}*EXP({b:.6f}*A2)'
    }

# CAPÍTULO 21: INTEGRACIÓN NEWTON-COTES

def funcion_integral(t):
    """Función a integrar: I(t)²R = (2sin(0.5t)+0.3t)²×1"""
    I_t = 2 * np.sin(0.5 * t) + 0.3 * t
    return I_t ** 2

def cap21_1_trapecio() -> Dict:
    """21.1 Regla del Trapecio"""
    a, b = 0, 10
    n = 10
    h = (b - a) / n
    
    t_vals = np.linspace(a, b, n + 1)
    y_vals = funcion_integral(t_vals)
    
    # Regla del trapecio
    integral = h * (0.5 * y_vals[0] + np.sum(y_vals[1:-1]) + 0.5 * y_vals[-1])
    
    # Valor exacto (aproximado con alta precisión)
    from scipy.integrate import quad
    valor_exacto, _ = quad(funcion_integral, a, b)
    error = abs((integral - valor_exacto) / valor_exacto * 100)
    
    resultados = []
    for i in range(len(t_vals)):
        resultados.append({
            'i': i,
            't': round(t_vals[i], 2),
            'f(t)': round(y_vals[i], 4)
        })
    
    return {
        'titulo': '21.1 Regla del Trapecio',
        'formula': f'∫f(t)dt ≈ h/2[f(t₀) + 2∑f(tᵢ) + f(tₙ)], h = {h}',
        'valor_calculado': integral,
        'valor_exacto': valor_exacto,
        'error_porcentual': error,
        'resultados': resultados,
        'datos_grafica': {
            'x': t_vals.tolist(),
            'y': y_vals.tolist(),
            'xlabel': 't (segundos)',
            'ylabel': 'I(t)²R',
            'tipo': 'trapecio'
        },
        'excel': f'=(({h}/2)*(A2+2*SUM(B2:K2)+L2))'
    }

def cap21_2_simpson_1_3() -> Dict:
    """21.2 Regla de Simpson 1/3"""
    a, b = 0, 10
    n = 10  # debe ser par
    h = (b - a) / n
    
    t_vals = np.linspace(a, b, n + 1)
    y_vals = funcion_integral(t_vals)
    
    # Regla de Simpson 1/3
    suma_impares = np.sum(y_vals[1:-1:2])
    suma_pares = np.sum(y_vals[2:-1:2])
    integral = (h / 3) * (y_vals[0] + 4 * suma_impares + 2 * suma_pares + y_vals[-1])
    
    from scipy.integrate import quad
    valor_exacto, _ = quad(funcion_integral, a, b)
    error = abs((integral - valor_exacto) / valor_exacto * 100)
    
    resultados = []
    for i in range(len(t_vals)):
        resultados.append({
            'i': i,
            't': round(t_vals[i], 2),
            'f(t)': round(y_vals[i], 4)
        })
    
    return {
        'titulo': '21.2 Regla de Simpson 1/3',
        'formula': f'∫f(t)dt ≈ h/3[f(t₀) + 4∑f(impar) + 2∑f(par) + f(tₙ)], h = {h}',
        'valor_calculado': integral,
        'valor_exacto': valor_exacto,
        'error_porcentual': error,
        'resultados': resultados,
        'datos_grafica': {
            'x': t_vals.tolist(),
            'y': y_vals.tolist(),
            'xlabel': 't (segundos)',
            'ylabel': 'I(t)²R',
            'tipo': 'simpson13'
        },
        'excel': f'=(({h}/3)*(A2+4*SUM(impares)+2*SUM(pares)+L2))'
    }

def cap21_3_simpson_3_8() -> Dict:
    """21.3 Regla de Simpson 3/8"""
    a, b = 0, 10
    n = 9  # debe ser múltiplo de 3
    h = (b - a) / n
    
    t_vals = np.linspace(a, b, n + 1)
    y_vals = funcion_integral(t_vals)
    
    # Regla de Simpson 3/8
    integral = (3 * h / 8) * (y_vals[0] + 3 * np.sum(y_vals[1:-1:3]) + 
                               3 * np.sum(y_vals[2:-1:3]) + 2 * np.sum(y_vals[3:-1:3]) + y_vals[-1])
    
    from scipy.integrate import quad
    valor_exacto, _ = quad(funcion_integral, a, b)
    error = abs((integral - valor_exacto) / valor_exacto * 100)
    
    resultados = []
    for i in range(len(t_vals)):
        resultados.append({
            'i': i,
            't': round(t_vals[i], 2),
            'f(t)': round(y_vals[i], 4)
        })
    
    return {
        'titulo': '21.3 Regla de Simpson 3/8',
        'formula': f'∫f(t)dt ≈ 3h/8[f(t₀) + 3∑ + 3∑ + 2∑ + f(tₙ)], h = {h:.2f}',
        'valor_calculado': integral,
        'valor_exacto': valor_exacto,
        'error_porcentual': error,
        'resultados': resultados,
        'datos_grafica': {
            'x': t_vals.tolist(),
            'y': y_vals.tolist(),
            'xlabel': 't (segundos)',
            'ylabel': 'I(t)²R',
            'tipo': 'simpson38'
        },
        'excel': f'=((3*{h:.2f}/8)*(A2+3*SUM(...)+...+L2))'
    }

def cap21_4_segmentos_desiguales() -> Dict:
    """21.4 Integración con Segmentos Desiguales"""
    # Segmentos de diferente tamaño
    t_vals = np.array([0, 1, 3, 6, 8, 10])
    y_vals = funcion_integral(t_vals)
    
    # Trapecio con segmentos desiguales
    integral = 0
    for i in range(len(t_vals) - 1):
        h = t_vals[i + 1] - t_vals[i]
        integral += h * (y_vals[i] + y_vals[i + 1]) / 2
    
    from scipy.integrate import quad
    valor_exacto, _ = quad(funcion_integral, 0, 10)
    error = abs((integral - valor_exacto) / valor_exacto * 100)
    
    resultados = []
    for i in range(len(t_vals)):
        h_i = float(t_vals[i + 1] - t_vals[i]) if i < len(t_vals) - 1 else 0
        resultados.append({
            'i': int(i),
            't': round(float(t_vals[i]), 2),
            'f(t)': round(float(y_vals[i]), 4),
            'h': round(h_i, 2)
        })
    
    return {
        'titulo': '21.4 Segmentos Desiguales',
        'formula': '∫f(t)dt ≈ ∑[hᵢ/2(f(tᵢ) + f(tᵢ₊₁))]',
        'valor_calculado': float(integral),
        'valor_exacto': float(valor_exacto),
        'error_porcentual': float(error),
        'resultados': resultados,
        'datos_grafica': {
            'x': t_vals.tolist(),
            'y': y_vals.tolist(),
            'xlabel': 't (segundos)',
            'ylabel': 'I(t)²R',
            'tipo': 'desigual'
        },
        'excel': '=SUM((h_i/2)*(f(t_i)+f(t_i+1)))'
    }

def cap21_5_abierta_vs_cerrada() -> Dict:
    """21.5 Fórmulas Abiertas vs Cerradas"""
    a, b = 0, 10
    n = 10
    h = (b - a) / n
    
    t_vals = np.linspace(a, b, n + 1)
    y_vals = funcion_integral(t_vals)
    
    # Fórmula cerrada (Trapecio)
    integral_cerrada = h * (0.5 * y_vals[0] + np.sum(y_vals[1:-1]) + 0.5 * y_vals[-1])
    
    # Fórmula abierta (Punto medio)
    t_medio = (t_vals[:-1] + t_vals[1:]) / 2
    y_medio = funcion_integral(t_medio)
    integral_abierta = h * np.sum(y_medio)
    
    from scipy.integrate import quad
    valor_exacto, _ = quad(funcion_integral, a, b)
    error_cerrada = abs((integral_cerrada - valor_exacto) / valor_exacto * 100)
    error_abierta = abs((integral_abierta - valor_exacto) / valor_exacto * 100)
    
    resultados = []
    for i in range(len(t_vals)):
        resultados.append({
            'i': i,
            't': round(t_vals[i], 2),
            'f(t)': round(y_vals[i], 4)
        })
    
    return {
        'titulo': '21.5 Fórmulas Abiertas vs Cerradas',
        'formula': 'Cerrada: usa extremos | Abierta: usa puntos medios',
        'valor_cerrada': integral_cerrada,
        'valor_abierta': integral_abierta,
        'valor_exacto': valor_exacto,
        'error_cerrada': error_cerrada,
        'error_abierta': error_abierta,
        'resultados': resultados,
        'datos_grafica': {
            'x': t_vals.tolist(),
            'y': y_vals.tolist(),
            'xlabel': 't (segundos)',
            'ylabel': 'I(t)²R',
            'tipo': 'comparacion'
        },
        'excel': 'Cerrada: ver 21.1 | Abierta: =h*SUM(puntos_medios)'
    }

def cap21_6_multiple_3d() -> Dict:
    """21.6 Integración Múltiple (visualización 3D)"""
    a, b = 0, 10
    n_steps = 20
    t_vals = np.linspace(a, b, n_steps + 1)
    y_vals = funcion_integral(t_vals)
    
    # Calcular integral acumulada
    from scipy.integrate import cumulative_trapezoid
    integral_acum = np.concatenate([[0], cumulative_trapezoid(y_vals, t_vals)])
    
    from scipy.integrate import quad
    valor_exacto, _ = quad(funcion_integral, a, b)
    valor_final = integral_acum[-1]
    error = abs((valor_final - valor_exacto) / valor_exacto * 100)
    
    resultados = []
    for i in range(len(t_vals)):
        resultados.append({
            'i': i,
            't': round(t_vals[i], 2),
            'f(t)': round(y_vals[i], 4),
            'integral_acum': round(integral_acum[i], 4)
        })
    
    return {
        'titulo': '21.6 Integración Múltiple 3D',
        'formula': 'Visualización 3D: t, f(t), integral acumulada',
        'valor_calculado': valor_final,
        'valor_exacto': valor_exacto,
        'error_porcentual': error,
        'resultados': resultados,
        'datos_grafica': {
            'x': t_vals.tolist(),
            'y': y_vals.tolist(),
            'z': integral_acum.tolist(),
            'xlabel': 't (segundos)',
            'ylabel': 'f(t)',
            'zlabel': 'Integral Acumulada',
            'tipo': '3d_integral'
        },
        'excel': '=TRAPZ(valores) acumulativo'
    }
