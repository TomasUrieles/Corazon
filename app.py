import streamlit as st
import joblib
import numpy as np

# Cargar el modelo y el scaler
model = joblib.load("svc_model.jb")
scaler = joblib.load("scaler.jb")

# Título y subtítulo
st.title("🫀 Predictor de problemas cardiacos")
st.subheader("Elaborado por marca registrada Unab 2025")

# Sliders para los datos de entrada
edad = st.slider("Edad", min_value=25, max_value=80, value=55, step=1)
colesterol = st.slider("Colesterol", min_value=120, max_value=600, value=242, step=2)

# Preparar los datos para el modelo
X = np.array([[edad, colesterol]])
X_scaled = scaler.transform(X)

# Predicción
prediccion = model.predict(X_scaled)[0]

# Mostrar resultado
if prediccion == 1:
    st.image("97203a9d-a0f0-46b4-847e-51c6de0238ac.png", caption="El paciente está sano y feliz 🎉")
    st.success("Resultado: No sufrirá del corazón ❤️")
else:
    st.image("ce515c92-d980-4b40-9df3-9711ecb13783.png", caption="El paciente tiene riesgo de problema cardiaco ⚠️")
    st.error("Resultado: Sufrirá del corazón 💔")
