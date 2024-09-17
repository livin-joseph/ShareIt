from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/send', methods=['GET', 'POST'])
def send():
    if request.method == 'POST':
        file = request.files['file']
        from Client import upload
        try:
            upload(file)
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
        from Client import download
        from Exceptions import EmptyBufferException
        try:
            download()
        except EmptyBufferException as e:
            print(e)
            message = {'title': 'Download failed', 'msg': 'There is no file uploaded to the server<br>You will be redirected to homepage in 5 seconds...'}
            return render_template('redirect.html', **message)
        except Exception as e:
            print(type(e))
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

        elif 'start_button' in request.form:
            from Client import start
            try:
                start()
            except Exception as e:
                message = {'title': 'Server is online already', 'msg': 'You will be redirected to homepage in 5 seconds...'}
                return render_template('redirect.html', **message)

            message = {'title': 'Server is setup successfully', 'msg': 'You will be redirected to homepage in 5 seconds...'}

        elif 'stop_button' in request.form:
            from Client import stop
            try:
                stop()
            except Exception as e:
                message = {'title': 'Server is offline already', 'msg': 'You will be redirected to homepage in 5 seconds...'}
                return render_template('redirect.html', **message)

            message = {'title': 'Server is shutdown successfully', 'msg': 'You will be redirected to homepage in 5 seconds...'}

    # Handle GET requests by rendering the homepage
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
