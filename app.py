import numpy as np
import pickle
from flask import Flask, render_template_string, request

app = Flask(__name__)

# Load the trained model
with open("svm.pkl", "rb") as f:
    model = pickle.load(f)

# Embedded HTML & CSS string
HTML_LAYOUT = """



    
    
    Student Performance Prediction
