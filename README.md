# 🛒 Retail Sales ML Pipeline

Proyecto end-to-end de **Data Science + Data Engineering** que simula,
procesa y predice ventas futuras de clientes retail mediante un pipeline
reproducible.

Este proyecto demuestra construcción de pipelines reales utilizados en
entornos productivos.

------------------------------------------------------------------------

## 🎯 Objetivo del proyecto

Construir un sistema que:

1.  Genere datos simulados de clientes retail.
2.  Limpie y valide datos.
3.  Construya features de negocio.
4.  Entrene un modelo de Machine Learning.
5.  Genere predicciones para nuevos clientes.
6.  Produzca outputs listos para análisis comercial.

------------------------------------------------------------------------

## ⚙️ Pipeline completo

El flujo ejecutado es:

    generate_data
          ↓
    clean_data
          ↓
    feature_engineering
          ↓
    model_training
          ↓
    batch_prediction

Todo el pipeline puede ejecutarse en un solo comando.

------------------------------------------------------------------------

## 🚀 Ejecución rápida

Desde la raíz del proyecto:

### Ejecutar pipeline completo

``` bash
python src/pipeline.py run-all
```

### Entrenar modelo

``` bash
python src/pipeline.py train
```

### Generar predicciones

``` bash
python src/pipeline.py predict --input data/nuevos_clientes.csv
```

------------------------------------------------------------------------

## 📁 Estructura del proyecto

    kranio-data-science-project
    │
    ├── data/                  # datasets base
    ├── outputs/
    │   ├── datasets/          # datasets generados
    │   ├── models/            # modelos entrenados
    │   └── predictions/       # resultados finales
    │
    ├── notebooks/             # análisis exploratorio
    │
    ├── src/
    │   ├── generate_data.py
    │   ├── clean.py
    │   ├── features.py
    │   ├── train.py
    │   ├── predict.py
    │   └── pipeline.py
    │
    └── README.md

------------------------------------------------------------------------

## 📊 Resultado final

El pipeline genera:

-   Modelo entrenado reutilizable
-   Predicción de ventas futuras
-   Dataset listo para CRM, BI o campañas comerciales

------------------------------------------------------------------------

## 🧠 Tecnologías utilizadas

-   Python
-   Pandas
-   Scikit-learn
-   Joblib
-   CLI modular con argparse
-   Pipeline reproducible

------------------------------------------------------------------------

## 🏢 Aplicaciones reales

Este sistema puede utilizarse para:

-   Customer Lifetime Value estimation
-   Segmentación comercial
-   Predicción de compras
-   Marketing dirigido
-   Optimización de campañas

------------------------------------------------------------------------

## 👨‍💻 Autor

Proyecto desarrollado como parte del portafolio profesional orientado a
roles de:

-   Data Scientist
-   Data Engineer
-   Analytics Engineer
