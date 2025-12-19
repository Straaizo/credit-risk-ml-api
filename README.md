# 📊 Credit Risk ML FASTAPI

**Proyecto:** API de Machine Learning para predicción / Análisis de riesgo crediticio.

**Integrantes:** Enzo Sabattini, Cristopher Silva


# 🧠 Contexto

Una institución financiera busca mejorar su proceso de evaluación de solicitudes de crédito. Actualmente, el análisis de riesgo se realiza de forma manual o con métodos poco eficientes, 
lo que genera pérdidas económicas por incumplimientos y decisiones de aprobación subóptimas. 

# 🎯 Objetivo del Proyecto

El objetivo principal de este proyecto es desarrollar una API de Machine Learning capaz de predecir la probabilidad de incumplimiento de un cliente, a partir de información financiera y demográfica, permitiendo:

- Automatizar el análisis de riesgo crediticio
- Reducir decisiones manuales
- Apoyar la toma de decisiones mediante reglas de negocio

# 🛠️ Tecnologias Utilizadas.

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
```
# ⚙️ Flujo del Proyecto

📁 01_data_understanding/

Contiene data_understanding_eda.py, donde se realiza el análisis exploratorio de los datos: comprensión de las variables, distribución del target, valores nulos y primeras observaciones sobre los datasets.

📁 02_data_preparation/

Incluye data_preparation.py, encargado de la limpieza, integración de múltiples fuentes y la generación del dataset final que será utilizado para el entrenamiento del modelo.

📁 03_modeling/

En modeling.py se carga el dataset preparado, se entrena el modelo de machine learning, y se guardan los artefactos necesarios para su uso posterior.

📁 04_evaluation/

El archivo evaluation.py evalúa el modelo entrenado utilizando métricas adecuadas, permitiendo validar su desempeño antes del despliegue.

📁 05_deployment/

Contiene el código de la API desarrollada con FastAPI:

app.py: define los endpoints de predicción.

schema.py: define el esquema de entrada de datos.

utils.py: maneja el preprocesamiento necesario antes de la inferencia.

init.py: permite que la carpeta sea reconocida como módulo.

📁 artifacts/

Almacena los resultados persistentes del proyecto:

model.pkl: modelo entrenado.

columns.json: esquema de variables esperado por el modelo.

📄 requirements.txt

Lista las dependencias necesarias para ejecutar el proyecto y la API.

Esta estructura refleja un flujo completo de CRISP-DM, separando claramente análisis, preparación, modelado, evaluación y despliegue.

