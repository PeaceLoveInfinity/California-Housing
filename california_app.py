import joblib
import numpy as np
import sklearn
from fastapi import FastAPI, UploadFile, File
import uvicorn # It is a server to run FastAPI

# Initialize app
app = FastAPI()

# Load model
obj=joblib.load('california_clean.joblib')
model=obj['model']
cols=obj['columns']                                

@app.get("/")
def greet():
    return('Welcome')

@app.get('/predict')
def predict(MedInc:float, HouseAge:float, AveRooms:float, 
            Population:float, AveOccup:float, Latitude:float):
    input_data = np.array([[MedInc, HouseAge, AveRooms, 
                            Population, AveOccup, Latitude]])
    prediction = model.predict(input_data)
    return {'Predicted House Price': float(prediction[0])}                                                                                      

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)