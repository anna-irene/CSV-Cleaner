from flask import Flask, request, send_file, render_template
import pandas as pd
from io import StringIO, BytesIO
from cleaner import clean_csv

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')    

@app.route('/clean', methods=['POST'])
def clean_file():
    if 'file' not in request.files:
        return "No file uploaded", 400

    file = request.files['file']
    if not file.filename.endswith('.csv'):
        return "Please upload a CSV file", 400

    try:
        df = pd.read_csv(file)
    except Exception as e:
        return f"Error reading CSV file: {e}", 400

    cleaned_df = clean_csv(df)

    output = StringIO()
    cleaned_df.to_csv(output, index=False)
    output.seek(0)

    return send_file(
        BytesIO(output.getvalue().encode()),
        mimetype="text/csv",
        as_attachment=True,
        download_name="cleaned_file.csv"
    )

if __name__ == '__main__':
    app.run(debug=True)
