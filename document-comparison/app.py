from flask import Flask, render_template, request, redirect, url_for
import os
import difflib

app = Flask(__name__)

SAMPLE_PATH = os.path.join(os.getcwd(), 'sample')
UPLOAD_PATH = os.path.join(os.getcwd(), 'uploads')

if not os.path.exists(UPLOAD_PATH):
    os.makedirs(UPLOAD_PATH)

def compare_texts(sample_text_path, uploaded_text_path):
    with open(sample_text_path, 'r') as sample_file:
        sample_text = sample_file.read()
    with open(uploaded_text_path, 'r') as uploaded_file:
        uploaded_text = uploaded_file.read()
    
    diff = difflib.unified_diff(
        sample_text.splitlines(),
        uploaded_text.splitlines(),
        fromfile='Sample',
        tofile='Uploaded',
    )
    return '\n'.join(diff)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)
    
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)

    document_type = request.form['document_type']
    sample_text_path = os.path.join(SAMPLE_PATH, f'sample_{document_type.lower()}.txt')

    file_path = os.path.join(UPLOAD_PATH, file.filename)
    file.save(file_path)

    if file.filename.endswith('.txt'):
        diff_result = compare_texts(sample_text_path, file_path)
    else:
        return "Please upload a valid text file (.txt)."

    return render_template('result.html', diff_result=diff_result)

# Add this block at the end of the file:
print("Starting Flask app...")

if __name__ == '__main__':
    print("Running app on http://127.0.0.1:5000/")
    app.run(debug=True)



