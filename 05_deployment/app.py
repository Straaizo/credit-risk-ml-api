from fastapi import FastAPI
import joblib
from pathlib import Path

from schema import CreditApplication
from utils import prepare_input

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "artifacts" / "model.pkl"
COLUMNS_PATH = BASE_DIR / "artifacts" / "columns.json"

# Iniciar api
app = FastAPI(
    title="Credit Risk API",
    description="Predicción de riesgo de incumplimiento",
    version="1.0"
)

# Carga del modelo al iniciar 
model = joblib.load(MODEL_PATH)
# Define decision crediticia
def run_prediction(application: CreditApplication):
    data = application.dict()

    X = prepare_input(data, columns_path=COLUMNS_PATH)
    prob = model.predict_proba(X)[0][1]

    if prob < 0.3:
        decision = "APROBAR"
    elif prob < 0.6:
        decision = "REVISION_MANUAL"
    else:
        decision = "RECHAZAR"
# Retorna respuesta en json
    return {
        "probabilidad_incumplimiento": round(float(prob), 4),
        "decision": decision

    }

# Aplicacion POST para poder ver en la URL /DOCS 

@app.post("/predict")
def predict(application: CreditApplication):
    return run_prediction(application)
