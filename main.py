from fastapi import FastAPI
import uvicorn
from fastapi.responses import HTMLResponse
from cards import Card, _DB

app = FastAPI()

@app.get("/")
def get_html():
    html_content = """<html>
        </head>
        <body>
            <h1 style='color: blue'>Hello world!</h1>
        </body>
    </html>"""
    return HTMLResponse(html_content)


@app.get("/get_cards")
def get_cards():
    return _DB

if __name__ == "__main__":
    uvicorn.run(app=app,
                host='127.0.0.1',
                port=80
                )
