from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
from app.api import routes_auth, routes_predict, routes_home, routes_health
from app.middleware.logging_middleware import LoggingMiddleware
from app.core.exceptions import register_exception_handlers

app = FastAPI(title='Car Price Prediction API')

# Middleware
app.add_middleware(LoggingMiddleware)

# Routes
app.include_router(routes_home.router, tags=['Home'])
app.include_router(routes_health.router, tags=['Health'])
app.include_router(routes_auth.router, tags=['Authorization'])
app.include_router(routes_predict.router, tags=['Prediction'])

# Monitoring using Prometheus
Instrumentator().instrument(app).expose(app)

# Exception handlers
register_exception_handlers(app)