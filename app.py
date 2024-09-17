from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/send', methods=['GET', 'POST'])
def send():
    if request.method == 'POST':
        file = request.files['file']
        from Client import upload
        upload(file)

        return render_template('done_upload.html')

    # Handle GET requests by rendering the upload page
    return render_template('upload.html')

@app.route('/receive', methods=['GET', 'POST'])
def receive():
    if request.method == 'POST':
        from Client import download
        download()

        return render_template('done_download.html')
    
    # Handle GET requests by rendering the download page
    return render_template('download.html')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'send_button' in request.form:
            return redirect(url_for('send'))
        elif 'receive_button' in request.form:
            return redirect(url_for('receive'))

    # Handle GET requests by rendering the homepage
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
