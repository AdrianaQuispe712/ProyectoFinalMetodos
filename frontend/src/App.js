import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

const BACKEND_URL = process.env.REACT_APP_BACKEND_URL;
const API = `${BACKEND_URL}/api`;

const CAPITULOS = {
  3: {
    titulo: 'Capítulo 3: Errores de Redondeo',
    enunciado: {
      titulo: 'Problema: Propagación de Error en Resistencia Equivalente',
      descripcion: 'Cálculo de resistencia equivalente en paralelo con incertidumbre en las mediciones.',
      formula: 'R_eq = (R₁ × R₂) / (R₁ + R₂)',
      datos: 'R₁ = 100±5Ω, R₂ = 220±10Ω',
      valorExacto: 'R_eq = 68.75Ω'
    },
    metodos: [
      { id: 1, nombre: '3.1 Cifras Significativas' },
      { id: 2, nombre: '3.2 Exactitud vs Precisión' },
      { id: 3, nombre: '3.3 Error Absoluto' },
      { id: 4, nombre: '3.4 Error Relativo' },
      { id: 5, nombre: '3.5 Error Porcentual' },
      { id: 6, nombre: '3.6 Comparativa de Errores' },
      { id: 7, nombre: '3.7 Error de Redondeo Acumulado' }
    ]
  },
  17: {
    titulo: 'Capítulo 17: Regresión por Mínimos Cuadrados',
    enunciado: {
      titulo: 'Problema: Modelado de Presión vs Temperatura en Reactor Químico',
      descripcion: 'Ajuste de modelos matemáticos a datos experimentales de presión y temperatura.',
      datos: 'Temperatura (°C): [20, 30, 40, 50, 60]',
      datos2: 'Presión (bar): [2.1, 2.8, 3.5, 4.2, 4.9]',
      objetivo: 'Encontrar la relación funcional entre presión y temperatura'
    },
    metodos: [
      { id: 1, nombre: '17.1 Regresión Lineal' },
      { id: 2, nombre: '17.2 Regresión Polinomial Grado 2' },
      { id: 3, nombre: '17.3 Regresión Polinomial Grado 3' },
      { id: 4, nombre: '17.4 Regresión Múltiple (3D)' },
      { id: 5, nombre: '17.5 Regresión No Lineal Exponencial' }
    ]
  },
  21: {
    titulo: 'Capítulo 21: Integración Newton-Cotes',
    enunciado: {
      titulo: 'Problema: Cálculo de Energía Disipada en Circuito Eléctrico',
      descripcion: 'Calcular la energía disipada por una resistencia con corriente variable en el tiempo.',
      formula: 'E = ∫₀¹⁰ I(t)² × R dt',
      corriente: 'I(t) = 2sin(0.5t) + 0.3t (amperios)',
      resistencia: 'R = 10Ω',
      intervalo: 't ∈ [0, 10] segundos',
      valorExacto: 'E ≈ 205.5 J (valor de referencia numérico)'
    },
    metodos: [
      { id: 1, nombre: '21.1 Regla del Trapecio' },
      { id: 2, nombre: '21.2 Regla de Simpson 1/3' },
      { id: 3, nombre: '21.3 Regla de Simpson 3/8' },
      { id: 4, nombre: '21.4 Segmentos Desiguales' },
      { id: 5, nombre: '21.5 Fórmulas Abiertas vs Cerradas' },
      { id: 6, nombre: '21.6 Integración Múltiple 3D' }
    ]
  }
};

function App() {
  const [capituloSeleccionado, setCapituloSeleccionado] = useState(null);
  const [resultado, setResultado] = useState(null);
  const [loading, setLoading] = useState(false);
  const [modalVisible, setModalVisible] = useState(false);
  const [todosResultados, setTodosResultados] = useState([]);
  const [vistaActual, setVistaActual] = useState('capitulos'); // 'capitulos', 'metodos', 'resultado', 'todos'

  const seleccionarCapitulo = (cap) => {
    setCapituloSeleccionado(cap);
    setVistaActual('metodos');
    setResultado(null);
  };

  const calcularMetodo = async (capitulo, metodo) => {
    setLoading(true);
    try {
      const response = await axios.get(`${API}/metodo/${capitulo}/${metodo}`);
      setResultado(response.data);
      setVistaActual('resultado');
    } catch (error) {
      console.error('Error al calcular:', error);
      alert('Error al calcular el método');
    }
    setLoading(false);
  };

  const calcularTodos = async () => {
    setLoading(true);
    const resultados = [];
    
    try {
      for (const [capNum, capData] of Object.entries(CAPITULOS)) {
        for (const metodo of capData.metodos) {
          const response = await axios.get(`${API}/metodo/${capNum}/${metodo.id}`);
          resultados.push({
            capitulo: capNum,
            metodo: metodo.id,
            nombre: metodo.nombre,
            ...response.data
          });
        }
      }
      setTodosResultados(resultados);
      setVistaActual('todos');
    } catch (error) {
      console.error('Error al calcular todos:', error);
      alert('Error al calcular todos los métodos');
    }
    setLoading(false);
  };

  const volverACapitulos = () => {
    setCapituloSeleccionado(null);
    setResultado(null);
    setVistaActual('capitulos');
  };

  const volverAMetodos = () => {
    setResultado(null);
    setVistaActual('metodos');
  };

  const abrirModal = (grafica) => {
    setModalVisible(grafica);
  };

  return (
    <div className="app-container">
      {/* Header */}
      <header className="header">
        <h1 data-testid="main-title">Métodos Numéricos - 18 Métodos</h1>
        <p>Análisis de Errores, Regresión e Integración</p>
      </header>

      {/* Navegación */}
      <div className="navigation">
        {vistaActual !== 'capitulos' && (
          <button data-testid="btn-volver-capitulos" onClick={volverACapitulos} className="btn-nav">
            ← Volver a Capítulos
          </button>
        )}
        {vistaActual === 'resultado' && (
          <button data-testid="btn-volver-metodos" onClick={volverAMetodos} className="btn-nav">
            ← Volver a Métodos
          </button>
        )}
        {vistaActual !== 'todos' && (
          <button data-testid="btn-calcular-todos" onClick={calcularTodos} className="btn-todos" disabled={loading}>
            {loading ? 'Calculando...' : 'Calcular TODOS los Métodos'}
          </button>
        )}
      </div>

      <main className="main-content">
        {/* Vista de Capítulos */}
        {vistaActual === 'capitulos' && (
          <div className="capitulos-grid" data-testid="capitulos-grid">
            {Object.entries(CAPITULOS).map(([num, data]) => (
              <div key={num} className="capitulo-card" data-testid={`capitulo-${num}`}>
                <h2>{data.titulo}</h2>
                <p className="metodos-count">{data.metodos.length} métodos disponibles</p>
                <button 
                  data-testid={`btn-capitulo-${num}`}
                  onClick={() => seleccionarCapitulo(num)} 
                  className="btn-primary"
                >
                  Seleccionar Capítulo
                </button>
              </div>
            ))}
          </div>
        )}

        {/* Vista de Métodos */}
        {vistaActual === 'metodos' && capituloSeleccionado && (
          <div className="metodos-container" data-testid="metodos-container">
            <h2 className="capitulo-titulo">{CAPITULOS[capituloSeleccionado].titulo}</h2>
            
            {/* Enunciado del Problema */}
            <div className="enunciado-box" data-testid="enunciado-box">
              <h3 className="enunciado-titulo">📋 {CAPITULOS[capituloSeleccionado].enunciado.titulo}</h3>
              <p className="enunciado-desc">{CAPITULOS[capituloSeleccionado].enunciado.descripcion}</p>
              
              <div className="enunciado-detalles">
                {CAPITULOS[capituloSeleccionado].enunciado.formula && (
                  <div className="enunciado-item">
                    <strong>Fórmula:</strong> <code>{CAPITULOS[capituloSeleccionado].enunciado.formula}</code>
                  </div>
                )}
                {CAPITULOS[capituloSeleccionado].enunciado.datos && (
                  <div className="enunciado-item">
                    <strong>Datos:</strong> {CAPITULOS[capituloSeleccionado].enunciado.datos}
                  </div>
                )}
                {CAPITULOS[capituloSeleccionado].enunciado.datos2 && (
                  <div className="enunciado-item">
                    <strong></strong> {CAPITULOS[capituloSeleccionado].enunciado.datos2}
                  </div>
                )}
                {CAPITULOS[capituloSeleccionado].enunciado.corriente && (
                  <div className="enunciado-item">
                    <strong>Corriente:</strong> <code>{CAPITULOS[capituloSeleccionado].enunciado.corriente}</code>
                  </div>
                )}
                {CAPITULOS[capituloSeleccionado].enunciado.resistencia && (
                  <div className="enunciado-item">
                    <strong>Resistencia:</strong> {CAPITULOS[capituloSeleccionado].enunciado.resistencia}
                  </div>
                )}
                {CAPITULOS[capituloSeleccionado].enunciado.intervalo && (
                  <div className="enunciado-item">
                    <strong>Intervalo:</strong> {CAPITULOS[capituloSeleccionado].enunciado.intervalo}
                  </div>
                )}
                {CAPITULOS[capituloSeleccionado].enunciado.valorExacto && (
                  <div className="enunciado-item valor-exacto-destacado">
                    <strong>Valor Exacto:</strong> {CAPITULOS[capituloSeleccionado].enunciado.valorExacto}
                  </div>
                )}
                {CAPITULOS[capituloSeleccionado].enunciado.objetivo && (
                  <div className="enunciado-item">
                    <strong>Objetivo:</strong> {CAPITULOS[capituloSeleccionado].enunciado.objetivo}
                  </div>
                )}
              </div>
            </div>

            <div className="metodos-list">
              {CAPITULOS[capituloSeleccionado].metodos.map((metodo) => (
                <div key={metodo.id} className="metodo-item" data-testid={`metodo-${capituloSeleccionado}-${metodo.id}`}>
                  <div className="metodo-info">
                    <h3>{metodo.nombre}</h3>
                  </div>
                  <button
                    data-testid={`btn-calcular-${capituloSeleccionado}-${metodo.id}`}
                    onClick={() => calcularMetodo(capituloSeleccionado, metodo.id)}
                    className="btn-calcular"
                    disabled={loading}
                  >
                    {loading ? 'Calculando...' : 'Calcular'}
                  </button>
                </div>
              ))}
            </div>
          </div>
        )}

        {/* Vista de Resultado Individual */}
        {vistaActual === 'resultado' && resultado && (
          <div className="resultado-container" data-testid="resultado-container">
            <h2 data-testid="resultado-titulo">{resultado.titulo}</h2>
            
            <div className="formula-box" data-testid="formula-box">
              <strong>Fórmula:</strong> {resultado.formula}
            </div>

            {resultado.valor_exacto && (
              <div className="valor-exacto" data-testid="valor-exacto">
                <strong>Valor de Referencia:</strong> {resultado.valor_exacto}
              </div>
            )}

            {resultado.error_porcentual !== undefined && (
              <div className="error-box" data-testid="error-box">
                <strong>Error Porcentual:</strong> {resultado.error_porcentual.toFixed(4)}%
              </div>
            )}

            {/* Gráfica */}
            <div className="grafica-container" data-testid="grafica-container">
              <h3>Gráfica</h3>
              <img 
                src={`data:image/png;base64,${resultado.grafica_base64}`}
                alt="Gráfica del método"
                className="grafica-img"
                onClick={() => abrirModal(resultado.grafica_base64)}
                data-testid="grafica-img"
              />
              <p className="grafica-hint">Haz clic en la imagen para ampliar</p>
            </div>

            {/* Tabla de Resultados */}
            <div className="tabla-container" data-testid="tabla-container">
              <h3>Tabla de Cálculos</h3>
              <div className="tabla-wrapper">
                <table className="tabla-resultados">
                  <thead>
                    <tr>
                      {resultado.resultados.length > 0 && 
                        Object.keys(resultado.resultados[0]).map((key) => (
                          <th key={key}>{key}</th>
                        ))
                      }
                    </tr>
                  </thead>
                  <tbody>
                    {resultado.resultados.map((fila, idx) => (
                      <tr key={idx}>
                        {Object.values(fila).map((valor, i) => (
                          <td key={i}>
                            {typeof valor === 'number' ? valor.toFixed(6) : valor}
                          </td>
                        ))}
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            </div>

            {/* Fórmula Excel */}
            <div className="excel-box" data-testid="excel-box">
              <strong>Fórmula Excel Equivalente:</strong>
              <code>{resultado.excel}</code>
            </div>
          </div>
        )}

        {/* Vista de Todos los Resultados */}
        {vistaActual === 'todos' && (
          <div className="todos-container" data-testid="todos-container">
            <h2>Todos los Métodos - Tabla Comparativa</h2>
            
            {/* Tabla Comparativa */}
            <div className="tabla-comparativa-container">
              <table className="tabla-comparativa">
                <thead>
                  <tr>
                    <th>Método</th>
                    <th>Fórmula</th>
                    <th>Resultado</th>
                    <th>Fórmula Excel</th>
                    <th>Gráfica</th>
                  </tr>
                </thead>
                <tbody>
                  {todosResultados.map((res, idx) => (
                    <tr key={idx}>
                      <td><strong>{res.nombre}</strong></td>
                      <td className="formula-cell">{res.formula}</td>
                      <td>
                        {res.valor_exacto && <div>Ref: {res.valor_exacto}</div>}
                        {res.error_porcentual !== undefined && (
                          <div>Error: {res.error_porcentual.toFixed(4)}%</div>
                        )}
                      </td>
                      <td className="excel-cell"><code>{res.excel}</code></td>
                      <td>
                        <button
                          data-testid={`btn-ver-grafica-${idx}`}
                          onClick={() => abrirModal(res.grafica_base64)}
                          className="btn-ver-grafica"
                        >
                          Ver Gráfica
                        </button>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>

            {/* Galería de Miniaturas */}
            <div className="galeria-container" data-testid="galeria-container">
              <h2>Galería de Gráficas</h2>
              <div className="galeria-grid">
                {todosResultados.map((res, idx) => (
                  <div key={idx} className="miniatura-card" data-testid={`miniatura-${idx}`}>
                    <h4>{res.nombre}</h4>
                    <img
                      src={`data:image/png;base64,${res.grafica_base64}`}
                      alt={res.nombre}
                      onClick={() => abrirModal(res.grafica_base64)}
                      className="miniatura-img"
                    />
                  </div>
                ))}
              </div>
            </div>
          </div>
        )}
      </main>

      {/* Modal para Gráfica Ampliada */}
      {modalVisible && (
        <div className="modal" onClick={() => setModalVisible(false)} data-testid="modal-grafica">
          <div className="modal-content" onClick={(e) => e.stopPropagation()}>
            <span className="modal-close" onClick={() => setModalVisible(false)} data-testid="modal-close">&times;</span>
            <img
              src={`data:image/png;base64,${modalVisible}`}
              alt="Gráfica ampliada"
              className="modal-img"
            />
          </div>
        </div>
      )}

      {/* Loading Overlay */}
      {loading && (
        <div className="loading-overlay" data-testid="loading-overlay">
          <div className="loading-spinner"></div>
          <p>Calculando...</p>
        </div>
      )}
    </div>
  );
}

export default App;
