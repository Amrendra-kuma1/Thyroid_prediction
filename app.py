from flask import Flask, request, render_template

import pickle

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=["GET", "POST"])
def predict():
    # Load the model inside the predict function
    print("Loading model...")
    model1 = pickle.load(open('modelLogisticReg.pkl', 'rb'))
    print("Model loaded successfully!")

    if request.method == 'POST':
        Age = int(request.form.get("age"))
        T3 = float(request.form.get("T3"))
        TT4 = float(request.form.get("TT4"))
        FTI = float(request.form.get("FTI"))
        T4U = float(request.form.get("T4U"))
        sex = request.form.get("sex")
        if sex == 'sex_M':
            sex_M = 1
        else:
            sex_M = 0

        sick = request.form.get("sick")
        if sick == 'sick_t':
            sick_t = 1
        else:
            sick_t = 0

        pregnant = request.form.get("pregnant")
        if pregnant == 'pregnant_t':
            pregnant_t = 1
        else:
            pregnant_t = 0

        tumor = request.form.get("tumor")
        if tumor == 'tumor_t':
            tumor_t = 1
        else:
            tumor_t = 0

        i131_treatment = request.form.get("i131_treatment")
        if i131_treatment == 'i131_treatment_t':
            i131_treatment_t = 1
        else:
            i131_treatment_t = 0

        # Rest of your code for handling form data

        # Use the loaded model for prediction
        prediction = model1.predict(
            [[Age, T3, TT4, FTI, sex_M, sick_t, pregnant_t, tumor_t, i131_treatment_t, T4U]])

        output = prediction[0]
        print("Output value:", output, "Type:", type(output))
        if output == 0:
            return render_template('index.html', prediction_text='Thyroid_Result : Hyperthyroid')
        elif output == 1:
            return render_template('index.html', prediction_text='Thyroid_Result : Hypothyroid')
        elif output == 2:
            return render_template('index.html', prediction_text='Thyroid_Result : Negative')
        else:
            return render_template('index.html', prediction_text='Thyroid_Result : Sick')


if __name__ == '__main__':
    app.run(debug=True)
