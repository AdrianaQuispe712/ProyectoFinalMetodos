import matplotlib
matplotlib.use('Agg')  # Backend sin GUI
import matplotlib.pyplot as plt
import numpy as np
import io
import base64
from mpl_toolkits.mplot3d import Axes3D

def generar_grafica(datos: dict, titulo: str) -> str:
    """Genera gráfica según tipo y retorna imagen en base64"""
    
    plt.figure(figsize=(10, 6))
    tipo = datos.get('tipo', 'linea')
    
    if tipo == 'linea':
        plt.plot(datos['x'], datos['y'], marker='o', linewidth=2, markersize=8)
        plt.xlabel(datos.get('xlabel', 'X'))
        plt.ylabel(datos.get('ylabel', 'Y'))
        plt.grid(True, alpha=0.3)
        
    elif tipo == 'bar':
        plt.bar(datos['x'], datos['y'], color='steelblue', alpha=0.7, edgecolor='black')
        plt.xlabel(datos.get('xlabel', 'X'))
        plt.ylabel(datos.get('ylabel', 'Y'))
        plt.grid(True, alpha=0.3, axis='y')
        
    elif tipo == 'scatter':
        plt.scatter(datos['x'], datos['y'], s=100, alpha=0.6, edgecolors='black')
        # Línea de referencia y=x
        min_val = min(min(datos['x']), min(datos['y']))
        max_val = max(max(datos['x']), max(datos['y']))
        plt.plot([min_val, max_val], [min_val, max_val], 'r--', alpha=0.5, label='Valor ideal')
        plt.xlabel(datos.get('xlabel', 'X'))
        plt.ylabel(datos.get('ylabel', 'Y'))
        plt.legend()
        plt.grid(True, alpha=0.3)
        
    elif tipo in ['regresion', 'regresion_poli', 'exponencial']:
        plt.scatter(datos['x'], datos['y_real'], label='Datos reales', s=100, alpha=0.7, edgecolors='black')
        plt.plot(datos['x'], datos['y_pred'], 'r-', label='Ajuste', linewidth=2)
        plt.xlabel(datos.get('xlabel', 'X'))
        plt.ylabel(datos.get('ylabel', 'Y'))
        plt.legend()
        plt.grid(True, alpha=0.3)
        
    elif tipo == 'multiple':
        plt.plot(datos['x'], datos['y1'], marker='o', label='Error Absoluto', linewidth=2)
        plt.plot(datos['x'], datos['y2'], marker='s', label='Error Relativo', linewidth=2)
        plt.plot(datos['x'], datos['y3'], marker='^', label='Error %', linewidth=2)
        plt.xlabel(datos.get('xlabel', 'X'))
        plt.ylabel(datos.get('ylabel', 'Y'))
        plt.legend()
        plt.grid(True, alpha=0.3)
        
    elif tipo in ['trapecio', 'simpson13', 'simpson38', 'desigual', 'comparacion']:
        # Gráfica de la función
        plt.plot(datos['x'], datos['y'], 'b-', linewidth=2, label='f(t)')
        plt.fill_between(datos['x'], datos['y'], alpha=0.3, label='Área integrada')
        
        # Líneas verticales para mostrar los segmentos
        for x_val in datos['x']:
            plt.axvline(x=x_val, color='gray', linestyle='--', alpha=0.3, linewidth=0.5)
        
        plt.xlabel(datos.get('xlabel', 'X'))
        plt.ylabel(datos.get('ylabel', 'Y'))
        plt.legend()
        plt.grid(True, alpha=0.3)
        
    elif tipo == '3d' or tipo == '3d_integral':
        fig = plt.figure(figsize=(10, 8))
        ax = fig.add_subplot(111, projection='3d')
        
        if tipo == '3d':
            ax.scatter(datos['x'], datos['y'], datos['z'], c='blue', marker='o', s=100)
            ax.set_xlabel(datos.get('xlabel', 'X'))
            ax.set_ylabel(datos.get('ylabel', 'Y'))
            ax.set_zlabel(datos.get('zlabel', 'Z'))
        else:
            ax.plot(datos['x'], datos['y'], datos['z'], 'b-', linewidth=2)
            ax.scatter(datos['x'], datos['y'], datos['z'], c='red', marker='o', s=50)
            ax.set_xlabel(datos.get('xlabel', 'X'))
            ax.set_ylabel(datos.get('ylabel', 'Y'))
            ax.set_zlabel(datos.get('zlabel', 'Z'))
        
        plt.tight_layout()
        # Convertir a base64
        buf = io.BytesIO()
        plt.savefig(buf, format='png', dpi=100, bbox_inches='tight')
        buf.seek(0)
        img_base64 = base64.b64encode(buf.read()).decode('utf-8')
        plt.close()
        return img_base64
    
    plt.title(titulo, fontsize=14, fontweight='bold')
    plt.tight_layout()
    
    # Convertir a base64
    buf = io.BytesIO()
    plt.savefig(buf, format='png', dpi=100, bbox_inches='tight')
    buf.seek(0)
    img_base64 = base64.b64encode(buf.read()).decode('utf-8')
    plt.close()
    
    return img_base64
