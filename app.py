from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>Student Flask App</title>
        </head>
        <body>
            <h1>Student Flask App</h1>
            <p>Application deployed successfully!</p>
            <p>Automated using GitHub, Jenkins and Docker.</p>
        </body>
    </html>
    """

@app.route("/health")
def health():
    return {"status": "healthy"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)