# app.py
import os
import io
import time
from datetime import datetime
import random
import json
from pathlib import Path

from flask import Flask, render_template, jsonify, send_from_directory, request
from flask_cors import CORS
import pandas as pd
import numpy as np
import pickle


import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
# -------------------------LOADING THE TRAINED MODELS -----------------------------------------------

gmail_list=[]
password_list=[]
gmail_list1=[]
password_list1=[]



app = Flask(__name__)
CORS(app)

# ---------- Config ----------
XTEST_CSV = "X_test.csv"
MODEL_PICKLE = "stacking_model.pkl"
REPORT_CSV = "report_log.csv"
NUM_NODES = 20
SAMPLE_SIZE = NUM_NODES  # how many random rows to draw each update
# ----------------------------



import joblib

# ------------------ LOAD MODEL ------------------ #
saved_data = joblib.load("stacking_model.joblib")

loaded_model = saved_data["model"]
loaded_le = saved_data["label_encoder"]
feature_columns = saved_data["feature_columns"]

print("\n✅ Model loaded successfully!")




# Load model and metadata from pickle
#if not Path(MODEL_PICKLE).exists():
#    raise FileNotFoundError(f"Model pickle not found at {MODEL_PICKLE}. Save your model first.")

#with open(MODEL_PICKLE, "rb") as f:
#    saved = pickle.load(f)
#    loaded_model = saved.get("model")
#    loaded_le = saved.get("label_encoder")
#    feature_columns = saved.get("feature_columns")
#    if loaded_model is None or loaded_le is None or feature_columns is None:
#        raise ValueError("Pickle must contain 'model', 'label_encoder', and 'feature_columns' keys.")

# Load X_test CSV
if not Path(XTEST_CSV).exists():
    raise FileNotFoundError(f"{XTEST_CSV} not found. Save X_test to CSV before running the app.")

x_test_df = pd.read_csv(XTEST_CSV)

# Ensure columns availability and order
missing_cols = [c for c in feature_columns if c not in x_test_df.columns]
if missing_cols:
    raise ValueError(f"The following feature columns are missing in {XTEST_CSV}: {missing_cols}")

# Report CSV header if not exists
if not Path(REPORT_CSV).exists():
    pd.DataFrame(columns=["timestamp", "node_id", "predicted_label", "predicted_encoded", "confidence"]).to_csv(REPORT_CSV, index=False)

# Helper: generate fixed node positions (circle layout)
def generate_node_positions(n):
    angles = np.linspace(0, 2 * np.pi, n, endpoint=False)
    positions = []
    for i, a in enumerate(angles):
        x = np.cos(a)
        y = np.sin(a)
        positions.append({"id": i, "x": float(x), "y": float(y)})
    return positions

NODE_POSITIONS = generate_node_positions(NUM_NODES)

@app.route("/")
def index():
    return render_template("login44.html")

@app.route('/register2',methods=['POST',"GET"])
def register2():
    return render_template('register44.html') 

    
import pickle
@app.route('/logedin',methods=['POST'])
def logedin():
    
    int_features3 = [str(x) for x in request.form.values()]
    print(int_features3)
    logu=int_features3[0]
    passw=int_features3[1]
    

    name =int_features3[0]

    # Save to a file
    with open("name.pkl", "wb") as f:
        pickle.dump(name, f)

   # if int_features2[0]==12345 and int_features2[1]==12345:

    import MySQLdb


# Open database connection
    db = MySQLdb.connect("localhost","root","","ddbb" )

# prepare a cursor object using cursor() method
    cursor = db.cursor()
    cursor.execute("SELECT user FROM user_register")
    result1=cursor.fetchall()
              #print(result1)
              #print(gmail1)
    for row1 in result1:
                      print(row1)
                      print(row1[0])
                      gmail_list.append(str(row1[0]))
                      
                      #gmail_list.append(row1[0])
                      #value1=row1
                      
    print(gmail_list)
    

    cursor1= db.cursor()
    cursor1.execute("SELECT password FROM user_register")
    result2=cursor1.fetchall()
              #print(result1)
              #print(gmail1)
    for row2 in result2:
                      print(row2)
                      print(row2[0])
                      password_list.append(str(row2[0]))
                      
                      #gmail_list.append(row1[0])
                      #value1=row1
                      
    print(password_list)
    print(gmail_list.index(logu))
    print(password_list.index(passw))
    
    if gmail_list.index(logu)==password_list.index(passw):
        return render_template('index.html')
    else:
        return jsonify({'result':'use proper  gmail and password'})
                  
                                      
@app.route('/register',methods=['POST'])
def register():
    

    int_features2 = [str(x) for x in request.form.values()]
    #print(int_features2)
    #print(int_features2[0])
    #print(int_features2[1])
    r1=int_features2[0]
    print(r1)
    
    r2=int_features2[1]
    print(r2)
    logu1=int_features2[0]
    passw1=int_features2[1]
        
    

    

   # if int_features2[0]==12345 and int_features2[1]==12345:

    import MySQLdb


# Open database connection
    db = MySQLdb.connect("localhost","root",'',"ddbb" )

# prepare a cursor object using cursor() method
    cursor = db.cursor()
    cursor.execute("SELECT user FROM user_register")
    result1=cursor.fetchall()
              #print(result1)
              #print(gmail1)
    for row1 in result1:
                      print(row1)
                      print(row1[0])
                      gmail_list1.append(str(row1[0]))
                      
                      #gmail_list.append(row1[0])
                      #value1=row1
                      
    print(gmail_list1)
    if logu1 in gmail_list1:
                      return jsonify({'result':'this gmail is already in use '})  
    else:

                  #return jsonify({'result':'this  gmail is not registered'})
              

# Prepare SQL query to INSERT a record into the database.
                  sql = "INSERT INTO user_register(user,password) VALUES (%s,%s)"
                  val = (r1, r2)
   
                  try:
   # Execute the SQL command
                                       cursor.execute(sql,val)
   # Commit your changes in the database
                                       db.commit()
                  except:
   # Rollback in case there is any error
                                       db.rollback()

# disconnect from server
                  db.close()
                 # return jsonify({'result':'succesfully registered'})
                  return render_template('login44.html')



@app.route("/monitor")
def monitor():
    # initial data to draw the graph: node positions
    nodes = NODE_POSITIONS
    # optionally precompute some edges (simple ring + random edges)
    edges = []
    # ring edges
    for i in range(NUM_NODES):
        edges.append({"from": i, "to": (i+1) % NUM_NODES})
    # some random additional edges
    for _ in range(NUM_NODES // 2):
        a = random.randrange(NUM_NODES)
        b = random.randrange(NUM_NODES)
        if a != b:
            edges.append({"from": a, "to": b})
    return render_template("monitor.html", nodes=json.dumps(nodes), edges=json.dumps(edges))

@app.route("/api/get_update", methods=["GET"])
def get_update():
    """
    Returns prediction updates for all nodes.
    Behavior:
      - sample SAMPLE_SIZE rows from x_test_df
      - feed each sample row to model
      - return list with node_id, x,y, label, probability, threat(bool)
      - append to report CSV
    """
    # Sample rows
    sampled = x_test_df.sample(n=SAMPLE_SIZE, replace=True).reset_index(drop=True)

    updates = []
    log_rows = []
    for node_idx in range(NUM_NODES):
        row = sampled.iloc[node_idx]
        # ensure feature order
        features = row[feature_columns].values.reshape(1, -1).astype(float)
        # predict_proba and predicted label
        try:
            proba = loaded_model.predict_proba(features)[0]
        except Exception as e:
            # fallback to predict if predict_proba not allowed
            pred_enc = loaded_model.predict(features)[0]
            pred_label = loaded_le.inverse_transform([pred_enc])[0]
            confidence = 1.0
        else:
            top_idx = int(np.argmax(proba))
            pred_enc = top_idx
            pred_label = loaded_le.inverse_transform([pred_enc])[0]
            confidence = float(proba[top_idx])

        # decide threat: consider 'Benign' as non-threat
        is_threat = (str(pred_label).lower() != "benign")

        pos = NODE_POSITIONS[node_idx]
        updates.append({
            "node_id": node_idx,
            "x": pos["x"],
            "y": pos["y"],
            "predicted_label": str(pred_label),
            "predicted_encoded": int(pred_enc),
            "confidence": confidence,
            "is_threat": bool(is_threat)
        })

        log_rows.append({
            "timestamp": datetime.utcnow().isoformat(),
            "node_id": node_idx,
            "predicted_label": str(pred_label),
            "predicted_encoded": int(pred_enc),
            "confidence": confidence
        })

    # Append to report CSV
    try:
        df_log = pd.DataFrame(log_rows)
        df_log.to_csv(REPORT_CSV, mode="a", header=False, index=False)
    except Exception as e:
        app.logger.error("Failed to append to report CSV: %s", e)

    return jsonify({"updates": updates, "timestamp": datetime.utcnow().isoformat()})

@app.route("/api/get_report")
def get_report():
    """Return the whole report CSV as JSON (or send file)."""
    df = pd.read_csv(REPORT_CSV)
    return df.to_json(orient="records")

@app.route("/download_report")
def download_report():
    return send_from_directory(os.getcwd(), REPORT_CSV, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
