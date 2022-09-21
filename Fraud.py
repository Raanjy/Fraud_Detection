from flask import Flask, render_template, request
import pickle

# creating Flask App
app = Flask(__name__, template_folder='Templates')
model = pickle.load(open('fraud_model.pkl', "rb"))


@app.route("/", methods=["GET"])
def home():
    return render_template("Fraud_input.html")


@app.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST":
        amount = float(request.form["amount"])
        oldbalanceOrg = float(request.form["oldbalanceOrg"])
        newbalanceOrig = float(request.form["newbalanceOrig"])
        oldbalanceDest = float(request.form["oldbalanceDest"])
        newbalanceDest = float(request.form["newbalanceDest"])
        oldbalanceOrg = float(request.form["oldbalanceOrg"])
        newbalanceOrig = float(request.form["newbalanceOrig"])
        oldbalanceDest = float(request.form["oldbalanceDest"])
        newbalanceDest = float(request.form["newbalanceDest"])


        prediction = model.predict([amount, oldbalanceOrg, newbalanceOrig, oldbalanceDest, newbalanceDest, ])
        if prediction == 1:
            return render_template("Fraud_output.html", Detection="Detection Fraud Transaction")
        else:
            return render_template("Fraud_output.html", Detection="Detection Not Fraudulent")
    else:
        return render_template("Fraud_input.html")


if __name__ == "__main__":

    app.run(debug=True)
