# 🚀 Retail Sales Prediction --- End-to-End ML Project

Proyecto completo de Ciencia de Datos y MLOps que implementa un flujo
end-to-end para predicción de ventas futuras de clientes retail,
incluyendo:

✔ Exploración de datos (EDA)\
✔ Ingeniería de variables\
✔ Entrenamiento de modelo ML\
✔ API de predicción con FastAPI\
✔ Contenerización con Docker\
✔ Preparado para automatización con Airflow

Este proyecto demuestra habilidades prácticas en:

-   Data Science
-   Machine Learning
-   Data Engineering
-   API deployment
-   Arquitectura de pipelines de datos

------------------------------------------------------------------------

## 📊 Flujo del proyecto

    Datos crudos
          ↓
    EDA
          ↓
    Feature Engineering
          ↓
    Entrenamiento modelo
          ↓
    Modelo guardado
          ↓
    API FastAPI
          ↓
    Docker
          ↓
    Pipeline automático (Airflow)

------------------------------------------------------------------------

## 📁 Estructura del proyecto

    kranio-data-science-project/
    │
    ├── data/                    # Datos de entrada
    ├── notebooks/
    │   ├── 01_eda_retail_sales.ipynb
    │   ├── 02_feature_engineering.ipynb
    │   └── 03_model_training.ipynb
    │
    ├── outputs/
    │   └── models/
    │       └── retail_model.joblib
    │
    ├── src/
    │   └── api.py               # API de predicción
    │
    ├── Dockerfile
    ├── requirements.txt
    ├── requirements-api.txt
    └── README.md

------------------------------------------------------------------------

## 🧠 Modelo utilizado

Se entrenó un modelo de Machine Learning para estimar:

    Ventas futuras de clientes

Utilizando variables como:

-   Edad
-   Ingreso
-   Frecuencia de compra
-   Ticket promedio
-   Recencia de compra
-   Ratio online
-   Engagement del cliente
-   Score digital y actividad

------------------------------------------------------------------------

## ⚙️ Ejecutar API localmente

Instalar dependencias:

``` bash
pip install -r requirements-api.txt
```

Ejecutar API:

``` bash
uvicorn src.api:app --reload
```

Documentación automática:

    http://127.0.0.1:8000/docs

------------------------------------------------------------------------

## 🐳 Ejecutar con Docker

Construir imagen:

``` bash
docker build -t retail-ml-api .
```

Ejecutar contenedor:

``` bash
docker run -p 8000:8000 retail-ml-api
```

------------------------------------------------------------------------

## 📈 Próximo paso

Automatización completa con:

    Airflow pipeline

Permitirá:

-   Procesar nuevos datos
-   Generar features
-   Reentrenar modelo
-   Actualizar API automáticamente

------------------------------------------------------------------------

## 👤 Autor

**Fabián Díaz**\
Data Scientist \| Data Engineer \| Analytics Engineer
