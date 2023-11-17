from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

home = APIRouter()
templates = Jinja2Templates(directory="core/templates")


@home.get("/v1/dashboard/{asset}", response_class=HTMLResponse)
async def get_asset_history_data(request: Request, asset: str):
    return templates.TemplateResponse(
        'dashboard.html', {
            'request': request, 'asset': asset
        }
    )

@home.get("/v1/dashboard/{asset}/predict", response_class=HTMLResponse)
async def get_asset_prediction_data(request: Request, asset: str):
    return templates.TemplateResponse(
        'dashboard.html', {
            'request': request, 'asset': asset
        }
    )