# 🫀 Predictor de Problemas Cardiacos

Aplicación desarrollada en **Streamlit** que predice si una persona sufrirá o no de problemas cardíacos, utilizando un modelo de **Máquina de Vectores de Soporte (SVC)** previamente entrenado con datos de **edad** y **colesterol**.  

---

## 📌 Descripción

- El modelo fue entrenado con:
  - **Edad** (entre 25 y 80 años).  
  - **Colesterol** (entre 120 y 600).  
  - **Etiqueta (`problema_cardiaco`)**:  
    - `0` → El paciente **sufrirá del corazón**.  
    - `1` → El paciente **no sufrirá del corazón**.  

- Los datos fueron normalizados con **MinMaxScaler**.  
- El modelo y el scaler están guardados en archivos `.jb` usando **joblib**.  

La aplicación muestra:
- Una **imagen de riesgo cardiaco** si la predicción es `0`.  
- Una **imagen feliz** si la predicción es `1`.  

---

## 🚀 Instalación y ejecución

1. Clona el repositorio o descarga los archivos.
2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
