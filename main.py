from pydantic import BaseModel
import uvicorn
from fastapi import (
    Request,
    FastAPI
)
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlmodel import Session, create_engine

from core import DATABASE_URL
from models import Messages


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name='static')
templates = Jinja2Templates(directory="html")


class Mail(BaseModel):
    author: str = "Anonimous"
    message: str


engine = create_engine(DATABASE_URL, echo=False)


@app.put("/index.html", status_code=201)
async def message(payload: Mail):
    with Session(engine) as session:
        new_post = Messages(
            author=payload.author,
            text=payload.message
        )
        session.add(new_post)
        session.commit()
        session.refresh(new_post)
    return "Ok"


@app.get("/index.html", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=1717,
        server_header=False,
        proxy_headers=True,
        access_log=True,
        use_colors=True,

    )
