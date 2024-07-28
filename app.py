from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from cards import Card, _DB

app = FastAPI()

@app.get("/")
def get_html():
    html_content = """<html>
        </head>
        <body>
            <h1 style='color: aqua'>Hello world!</h1>
        </body>
    </html>"""
    return HTMLResponse(html_content)
    # return _DB


@app.get("/get_cards")
def get_cards():
    return {'message': 'ok'}
