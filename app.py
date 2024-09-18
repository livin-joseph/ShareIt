from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/send', methods=['GET', 'POST'])
def send():
    if request.method == 'POST':
        file = request.files['file']
        passwd = request.form['passwd']
        from Client import upload
        try:
            upload(file, passwd)
        except Exception as e:
            message = {'title': 'Upload failed', 'msg': 'Server is offline<br>You will be redirected to homepage in 5 seconds...'}
            return render_template('redirect.html', **message)

        message = {'title': 'Upload successful', 'msg': 'You will be redirected to homepage in 5 seconds...'}
        return render_template('redirect.html', **message)

    # Handle GET requests by rendering the upload page
    return render_template('upload.html')

@app.route('/receive', methods=['GET', 'POST'])
def receive():
    if request.method == 'POST':
        filename = request.form['filename']
        passwd = request.form['passwd']
        from Client import download
        from Exceptions import FileNotFoundException, WrongPasswordException
        try:
            download(filename, passwd)
        except FileNotFoundException as e:
            message = {'title': 'Download failed', 'msg': 'The file is not found the server<br>You will be redirected to homepage in 5 seconds...'}
            return render_template('redirect.html', **message)
        except WrongPasswordException as e:
            message = {'title': 'Download failed', 'msg': 'The password to access the file is incorrect<br>You will be redirected to homepage in 5 seconds...'}
            return render_template('redirect.html', **message)
        except Exception as e:
            message = {'title': 'Download failed', 'msg': 'Server is offline<br>You will be redirected to homepage in 5 seconds...'}
            return render_template('redirect.html', **message)
    
        message = {'title': 'Download successful', 'msg': 'You will be redirected to homepage in 5 seconds...'}
        return render_template('redirect.html', **message)

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
