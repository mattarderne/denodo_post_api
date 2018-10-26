### app.py

from flask import Flask, request, jsonify #import main Flask class and request object

app = Flask(__name__) #create the Flask app

@app.route('/query-example')
def query_example():
    return 'Todo...'

@app.route('/form-example', methods=['GET', 'POST']) #allow both GET and POST requests
def form_example():
    if request.method == 'POST': #this block is only entered when the form is submitted
        language = request.form.get('language')
        framework = request.form['framework']
        return '''<h1>The language value is: {}</h1>
                      <h1>The framework value is: {}</h1>'''.format(language, framework)

    return '''<form method="POST">
                      Language: <input type="text" name="language"><br>
                      Framework: <input type="text" name="framework"><br>
                     <input type="submit" value="Submit"><br>
                   </form>'''

@app.route('/json-example', methods=['POST']) #GET requests will be blocked
def json_example():
        req_data = request.get_json()

        language = req_data['language']
        framework = req_data['framework']
        python_version = req_data['version_info']['python'] #two keys are needed because of the nested object
        example = req_data['examples'][0] #an index is needed because of the array
        boolean_test = req_data['boolean_test']

        return jsonify(req_data)

if __name__ == '__main__':
    app.run(debug=True, port=5000) #run app in debug mode on port 5000