from fastapi import FastAPI, APIRouter
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
from starlette.middleware.cors import CORSMiddleware
import os
import logging
from pathlib import Path
from pydantic import BaseModel
from typing import Dict, Any

# Importar módulos de métodos y gráficas
import metodos
import graficas

ROOT_DIR = Path(__file__).parent
load_dotenv(ROOT_DIR / '.env')

# Create the main app
app = FastAPI()

# Create a router with the /api prefix
api_router = APIRouter(prefix="/api")

# Modelo para respuesta
class MetodoResponse(BaseModel):
    titulo: str
    formula: str
    resultados: list
    grafica_base64: str
    excel: str
    valor_exacto: Any = None
    error_porcentual: float = None

@api_router.get("/")
async def root():
    return {"message": "API de Métodos Numéricos - 18 Métodos Disponibles"}

# CAPÍTULO 3: ERRORES DE REDONDEO (7 métodos)
@api_router.get("/metodo/3/1")
async def metodo_3_1():
    try:
        resultado = metodos.cap3_1_cifras_significativas()
        grafica = graficas.generar_grafica(resultado['datos_grafica'], resultado['titulo'])
        
        return JSONResponse({
            'titulo': resultado['titulo'],
            'formula': resultado['formula'],
            'valor_exacto': resultado['valor_exacto'],
            'resultados': resultado['resultados'],
            'grafica_base64': grafica,
            'excel': resultado['excel']
        })
    except Exception as e:
        return JSONResponse({'error': str(e)}, status_code=500)

@api_router.get("/metodo/3/2")
async def metodo_3_2():
    try:
        resultado = metodos.cap3_2_exactitud_precision()
        grafica = graficas.generar_grafica(resultado['datos_grafica'], resultado['titulo'])
        
        return JSONResponse({
            'titulo': resultado['titulo'],
            'formula': resultado['formula'],
            'valor_exacto': resultado['valor_exacto'],
            'resultados': resultado['resultados'],
            'grafica_base64': grafica,
            'excel': resultado['excel']
        })
    except Exception as e:
        return JSONResponse({'error': str(e)}, status_code=500)

@api_router.get("/metodo/3/3")
async def metodo_3_3():
    try:
        resultado = metodos.cap3_3_error_absoluto()
        grafica = graficas.generar_grafica(resultado['datos_grafica'], resultado['titulo'])
        
        return JSONResponse({
            'titulo': resultado['titulo'],
            'formula': resultado['formula'],
            'valor_exacto': resultado['valor_exacto'],
            'resultados': resultado['resultados'],
            'grafica_base64': grafica,
            'excel': resultado['excel']
        })
    except Exception as e:
        return JSONResponse({'error': str(e)}, status_code=500)

@api_router.get("/metodo/3/4")
async def metodo_3_4():
    try:
        resultado = metodos.cap3_4_error_relativo()
        grafica = graficas.generar_grafica(resultado['datos_grafica'], resultado['titulo'])
        
        return JSONResponse({
            'titulo': resultado['titulo'],
            'formula': resultado['formula'],
            'valor_exacto': resultado['valor_exacto'],
            'resultados': resultado['resultados'],
            'grafica_base64': grafica,
            'excel': resultado['excel']
        })
    except Exception as e:
        return JSONResponse({'error': str(e)}, status_code=500)

@api_router.get("/metodo/3/5")
async def metodo_3_5():
    try:
        resultado = metodos.cap3_5_error_porcentual()
        grafica = graficas.generar_grafica(resultado['datos_grafica'], resultado['titulo'])
        
        return JSONResponse({
            'titulo': resultado['titulo'],
            'formula': resultado['formula'],
            'valor_exacto': resultado['valor_exacto'],
            'resultados': resultado['resultados'],
            'grafica_base64': grafica,
            'excel': resultado['excel']
        })
    except Exception as e:
        return JSONResponse({'error': str(e)}, status_code=500)

@api_router.get("/metodo/3/6")
async def metodo_3_6():
    try:
        resultado = metodos.cap3_6_comparativa_errores()
        grafica = graficas.generar_grafica(resultado['datos_grafica'], resultado['titulo'])
        
        return JSONResponse({
            'titulo': resultado['titulo'],
            'formula': resultado['formula'],
            'valor_exacto': resultado['valor_exacto'],
            'resultados': resultado['resultados'],
            'grafica_base64': grafica,
            'excel': resultado['excel']
        })
    except Exception as e:
        return JSONResponse({'error': str(e)}, status_code=500)

@api_router.get("/metodo/3/7")
async def metodo_3_7():
    try:
        resultado = metodos.cap3_7_error_redondeo()
        grafica = graficas.generar_grafica(resultado['datos_grafica'], resultado['titulo'])
        
        return JSONResponse({
            'titulo': resultado['titulo'],
            'formula': resultado['formula'],
            'valor_exacto': resultado['valor_exacto'],
            'resultados': resultado['resultados'],
            'grafica_base64': grafica,
            'excel': resultado['excel']
        })
    except Exception as e:
        return JSONResponse({'error': str(e)}, status_code=500)

# CAPÍTULO 17: REGRESIÓN (5 métodos)
@api_router.get("/metodo/17/1")
async def metodo_17_1():
    try:
        resultado = metodos.cap17_1_regresion_lineal()
        grafica = graficas.generar_grafica(resultado['datos_grafica'], resultado['titulo'])
        
        return JSONResponse({
            'titulo': resultado['titulo'],
            'formula': resultado['formula'],
            'valor_exacto': resultado['valor_exacto'],
            'resultados': resultado['resultados'],
            'grafica_base64': grafica,
            'excel': resultado['excel']
        })
    except Exception as e:
        return JSONResponse({'error': str(e)}, status_code=500)

@api_router.get("/metodo/17/2")
async def metodo_17_2():
    try:
        resultado = metodos.cap17_2_regresion_polinomial_2()
        grafica = graficas.generar_grafica(resultado['datos_grafica'], resultado['titulo'])
        
        return JSONResponse({
            'titulo': resultado['titulo'],
            'formula': resultado['formula'],
            'valor_exacto': resultado['valor_exacto'],
            'resultados': resultado['resultados'],
            'grafica_base64': grafica,
            'excel': resultado['excel']
        })
    except Exception as e:
        return JSONResponse({'error': str(e)}, status_code=500)

@api_router.get("/metodo/17/3")
async def metodo_17_3():
    try:
        resultado = metodos.cap17_3_regresion_polinomial_3()
        grafica = graficas.generar_grafica(resultado['datos_grafica'], resultado['titulo'])
        
        return JSONResponse({
            'titulo': resultado['titulo'],
            'formula': resultado['formula'],
            'valor_exacto': resultado['valor_exacto'],
            'resultados': resultado['resultados'],
            'grafica_base64': grafica,
            'excel': resultado['excel']
        })
    except Exception as e:
        return JSONResponse({'error': str(e)}, status_code=500)

@api_router.get("/metodo/17/4")
async def metodo_17_4():
    try:
        resultado = metodos.cap17_4_regresion_multiple()
        grafica = graficas.generar_grafica(resultado['datos_grafica'], resultado['titulo'])
        
        return JSONResponse({
            'titulo': resultado['titulo'],
            'formula': resultado['formula'],
            'valor_exacto': resultado['valor_exacto'],
            'resultados': resultado['resultados'],
            'grafica_base64': grafica,
            'excel': resultado['excel']
        })
    except Exception as e:
        return JSONResponse({'error': str(e)}, status_code=500)

@api_router.get("/metodo/17/5")
async def metodo_17_5():
    try:
        resultado = metodos.cap17_5_regresion_no_lineal()
        grafica = graficas.generar_grafica(resultado['datos_grafica'], resultado['titulo'])
        
        return JSONResponse({
            'titulo': resultado['titulo'],
            'formula': resultado['formula'],
            'valor_exacto': resultado['valor_exacto'],
            'resultados': resultado['resultados'],
            'grafica_base64': grafica,
            'excel': resultado['excel']
        })
    except Exception as e:
        return JSONResponse({'error': str(e)}, status_code=500)

# CAPÍTULO 21: INTEGRACIÓN NEWTON-COTES (6 métodos)
@api_router.get("/metodo/21/1")
async def metodo_21_1():
    try:
        resultado = metodos.cap21_1_trapecio()
        grafica = graficas.generar_grafica(resultado['datos_grafica'], resultado['titulo'])
        
        return JSONResponse({
            'titulo': resultado['titulo'],
            'formula': resultado['formula'],
            'valor_calculado': resultado['valor_calculado'],
            'valor_exacto': resultado['valor_exacto'],
            'error_porcentual': resultado['error_porcentual'],
            'resultados': resultado['resultados'],
            'grafica_base64': grafica,
            'excel': resultado['excel']
        })
    except Exception as e:
        return JSONResponse({'error': str(e)}, status_code=500)

@api_router.get("/metodo/21/2")
async def metodo_21_2():
    try:
        resultado = metodos.cap21_2_simpson_1_3()
        grafica = graficas.generar_grafica(resultado['datos_grafica'], resultado['titulo'])
        
        return JSONResponse({
            'titulo': resultado['titulo'],
            'formula': resultado['formula'],
            'valor_calculado': resultado['valor_calculado'],
            'valor_exacto': resultado['valor_exacto'],
            'error_porcentual': resultado['error_porcentual'],
            'resultados': resultado['resultados'],
            'grafica_base64': grafica,
            'excel': resultado['excel']
        })
    except Exception as e:
        return JSONResponse({'error': str(e)}, status_code=500)

@api_router.get("/metodo/21/3")
async def metodo_21_3():
    try:
        resultado = metodos.cap21_3_simpson_3_8()
        grafica = graficas.generar_grafica(resultado['datos_grafica'], resultado['titulo'])
        
        return JSONResponse({
            'titulo': resultado['titulo'],
            'formula': resultado['formula'],
            'valor_calculado': resultado['valor_calculado'],
            'valor_exacto': resultado['valor_exacto'],
            'error_porcentual': resultado['error_porcentual'],
            'resultados': resultado['resultados'],
            'grafica_base64': grafica,
            'excel': resultado['excel']
        })
    except Exception as e:
        return JSONResponse({'error': str(e)}, status_code=500)

@api_router.get("/metodo/21/4")
async def metodo_21_4():
    try:
        resultado = metodos.cap21_4_segmentos_desiguales()
        grafica = graficas.generar_grafica(resultado['datos_grafica'], resultado['titulo'])
        
        return JSONResponse({
            'titulo': resultado['titulo'],
            'formula': resultado['formula'],
            'valor_calculado': resultado['valor_calculado'],
            'valor_exacto': resultado['valor_exacto'],
            'error_porcentual': resultado['error_porcentual'],
            'resultados': resultado['resultados'],
            'grafica_base64': grafica,
            'excel': resultado['excel']
        })
    except Exception as e:
        return JSONResponse({'error': str(e)}, status_code=500)

@api_router.get("/metodo/21/5")
async def metodo_21_5():
    try:
        resultado = metodos.cap21_5_abierta_vs_cerrada()
        grafica = graficas.generar_grafica(resultado['datos_grafica'], resultado['titulo'])
        
        return JSONResponse({
            'titulo': resultado['titulo'],
            'formula': resultado['formula'],
            'valor_cerrada': resultado['valor_cerrada'],
            'valor_abierta': resultado['valor_abierta'],
            'valor_exacto': resultado['valor_exacto'],
            'error_cerrada': resultado['error_cerrada'],
            'error_abierta': resultado['error_abierta'],
            'resultados': resultado['resultados'],
            'grafica_base64': grafica,
            'excel': resultado['excel']
        })
    except Exception as e:
        return JSONResponse({'error': str(e)}, status_code=500)

@api_router.get("/metodo/21/6")
async def metodo_21_6():
    try:
        resultado = metodos.cap21_6_multiple_3d()
        grafica = graficas.generar_grafica(resultado['datos_grafica'], resultado['titulo'])
        
        return JSONResponse({
            'titulo': resultado['titulo'],
            'formula': resultado['formula'],
            'valor_calculado': resultado['valor_calculado'],
            'valor_exacto': resultado['valor_exacto'],
            'error_porcentual': resultado['error_porcentual'],
            'resultados': resultado['resultados'],
            'grafica_base64': grafica,
            'excel': resultado['excel']
        })
    except Exception as e:
        return JSONResponse({'error': str(e)}, status_code=500)

# Include the router in the main app
app.include_router(api_router)

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=os.environ.get('CORS_ORIGINS', '*').split(','),
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)
