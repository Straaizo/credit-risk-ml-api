# 📊 Credit Risk ML FASTAPI

**Proyecto:** API de Machine Learning para predicción / Análisis de riesgo crediticio.

**Integrantes:** Enzo Sabattini, Cristopher Silva


# 🧠 Contexto

Una institución financiera busca mejorar su proceso de evaluación de solicitudes de crédito. Actualmente, el análisis de riesgo se realiza de forma manual o con métodos poco eficientes, 
lo que genera pérdidas económicas por incumplimientos y decisiones de aprobación subóptimas. 
El objetivo del proyecto es automatizar y optimizar la predicción de riesgo de incumplimiento, ofreciendo información confiable para respaldar decisiones de crédito más seguras y rápidas.

# 🎯 Objetivo del Proyecto

El objetivo principal de este proyecto es desarrollar una API de Machine Learning capaz de predecir la probabilidad de incumplimiento de un cliente, a partir de información financiera y demográfica, permitiendo:

- Automatizar el análisis de riesgo crediticio
- Reducir decisiones manuales
- Apoyar la toma de decisiones mediante reglas de negocio

# 🛠️ Herramientas

- Python 3
- Pandas / NumPy 
- Scikit-learn 
- LightGBM 
- Joblib 
- FastAPI 
- Pydantic
- Uvicorn

# 📁 Estructura del repositorio

```text
├── 01_data_understanding/        # Exploración y análisis de datos
├── 02_data_preparation/          # Limpieza y preprocesamiento
├── 03_modeling/                  # Entrenamiento de modelos
├── 04_evaluation/                # Evaluación y métricas
├── 05_deployment/                # Código para servir la API
├── artifacts/                    # Modelos / vectores / artefactos generados
├── requirements.txt              # Dependencias del proyecto
└── README.md                     # Este documento
