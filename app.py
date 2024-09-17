from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/send', methods=['GET', 'POST'])
def send():
    print(request.files)
    if request.method == 'POST':
        from Client import upload
        filename = request.form.get('file')
        print(filename)
        upload(filename)

        return 'File is uploaded successfully!'

    # Handle GET requests by rendering the upload form
    return render_template('upload.html')

@app.route('/receive', methods=['GET', 'POST'])
def receive():
    if request.method == 'POST':
        from Client import download
        download()

        return 'File is downloaded successfully!'
    
    # Handle GET requests by rendering the upload form
    return render_template('download.html')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'send_button' in request.form:
            return redirect(url_for('send'))
        elif 'receive_button' in request.form:
            return redirect(url_for('receive'))
        print('heyy')
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
