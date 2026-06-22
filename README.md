# Arquitectura escalable para el análisis y predicción de eventos cardíacos basada en apren-dizaje automático y profundo aplicado a señales ECG

## Descripción del proyecto

Este proyecto desarrolla una arquitectura escalable para el análisis predictivo de eventos clínicos utilizando señales de electrocardiograma (ECG). El sistema integra tecnologías de Big Data y técnicas de Machine Learning y Deep Learning, con el objetivo de identificar patrones relevantes en datos clínicos y predecir eventos adversos en pacientes.

## Objetivos

### Objetivo general
Desarrollar un sistema de análisis predictivo basado en tecnologías de Big Data y técnicas de Machine Learning para el análisis de datos clínicos, con el fin de identificar patrones relevantes y predecir eventos adversos en pacientes.

### Objetivos específicos
1. Diseñar una arquitectura de datos que permita la ingesta y almacenamiento de grandes volúmenes de datos clínicos.  
2. Implementar procesos de preparación y procesamiento de datos para su análisis mediante técnicas de Machine Learning.  
3. Desarrollar modelos predictivos capaces de identificar patrones asociados a eventos clínicos adversos.  
4. Evaluar el rendimiento de los modelos mediante métricas de validación adecuadas.  
5. Analizar los resultados obtenidos para valorar el potencial de los modelos predictivos en el apoyo a la toma de decisiones clínicas.

## Dataset

El dataset utilizado proviene de PhysioNet:

- ECG Arrhythmia Database  
- https://physionet.org/content/ecg-arrhythmia/1.0.0/

Incluye registros de señales ECG utilizados para la detección de arritmias y eventos cardíacos relevantes.


## Pipeline del proyecto

El flujo de trabajo seguido es el siguiente:

1. Exploración de datos (EDA)  
2. Preprocesamiento de señales ECG  
3. División del dataset (train/validation/test)  
4. Entrenamiento de modelos  
5. Evaluación de resultados  
6. Inferencia  
7. Visualización mediante dashboard  


## Modelos utilizados

Se han implementado y comparado los siguientes modelos:

- XGBoost  
- Random Forest  
- Multilayer Perceptron (MLP)  
- CNN-BiLSTM  
- Regresión Logística  

El mejor modelo obtenido ha sido XGBoost.

## Métricas de evaluación

Los modelos han sido evaluados utilizando:

- AUC-ROC  
- AUC-PR  
- F1-score  
- Precision  
- Recall  
- Matriz de confusión  

## Infraestructura

El proyecto se ha desarrollado utilizando una arquitectura híbrida:

- AWS (S3, procesamiento y almacenamiento de datos).
    - El pipeline podría ejecutarse completamente en AWS si se dispone de los recursos computacionales necesarios, incluyendo soporte GPU para modelos de Deep Learning.
- Google Colab (entrenamiento de modelos de deep learning debido a limitaciones de GPU en AWS).

## Ejecución del proyecto

El proyecto está estructurado en notebooks y módulos independientes.  
Para reproducir los experimentos:

1. Instalar dependencias:
```bash
pip install -r requirements.txt
