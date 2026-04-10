# Car Price Prediction API

This project presents a **production-grade machine learning system** for predicting car prices using structured data. It integrates model development with a fully functional backend, incorporating **API design, caching, authentication, monitoring, and deployment** practices commonly used in industry.

---

## Table of Contents

1. Overview
    
2. Features
    
3. Project Workflow
    
4. Machine Learning Pipeline
    
5. API Endpoints
    
6. Project Structure
    
7. Installation & Setup
    
8. How to Run
    
9. Monitoring & Observability
    
10. Security
    
11. Results
    
12. Future Improvements
    
13. Tech Stack
    

---

## Overview

The objective of this project is to build a scalable and efficient system capable of predicting car prices through a trained machine learning model exposed via a REST API.

The system combines:

- A trained **Random Forest regression model**
    
- A **FastAPI-based backend service**
    
- **Redis caching** for performance optimization
    
- **JWT-based authentication and API key validation**
    
- **Monitoring tools (Prometheus and Grafana)**
    
- **Containerized deployment using Docker**
    
- **Cloud deployment via Render with managed Redis**
    

---

## Features

- End-to-end machine learning pipeline from training to deployment
    
- Real-time prediction through REST API
    
- Redis-based caching for repeated predictions
    
- JWT authentication and API key validation
    
- Custom logging middleware for request tracking
    
- Prometheus metrics integration for monitoring
    
- Grafana dashboards for visualization
    
- Docker-based multi-service orchestration
    
- Cloud deployment with external Redis support
    

---

## Project Workflow

1. Data Cleaning and Preparation
    
2. Feature Engineering and Transformation
    
3. Model Training and Evaluation
    
4. Pipeline Serialization
    
5. API Development using FastAPI
    
6. Integration with Redis Cache
    
7. Security Implementation (JWT and API Keys)
    
8. Monitoring Setup (Prometheus and Grafana)
    
9. Containerization with Docker
    
10. Deployment on Render
    

---

## Machine Learning Pipeline

### Dataset

- Contains 16 features:
    
    - 8 categorical
        
    - 8 numerical
        
- Includes missing values and duplicates
    

### Data Cleaning

- Removed duplicate records
    
- Dropped irrelevant columns:
    
    - `name`
        
    - `model`
        
    - `edition`
        

### Target Variable

- `selling_price`
    

### Train-Test Split

- 80% training
    
- 20% testing
    

### Feature Transformation

**Numerical Features**

- Missing values handled using **median imputation**
    
- Scaled using **StandardScaler**
    

**Categorical Features**

- Missing values replaced with `"missing"`
    
- Encoded using **OneHotEncoder**
    

### Model

- Algorithm: `RandomForestRegressor`
    
- Parameters:
    
    - `n_estimators = 10`
        
    - `max_depth = 5`
        

### Pipeline

- Combined preprocessing and model into a unified pipeline
    
- Ensures consistent transformations during inference
    

### Serialization

- Model pipeline saved using `.joblib`
    
- Loaded during API runtime for predictions
    

---

## API Endpoints

### Home

- `/`
    
- Returns a basic welcome response
    

### Health Check

- `/health`
    
- Confirms API availability
    

### Authentication

- `/login`
    
- Generates JWT token for authorized access
    

### Prediction

- `/predict`
    
- Accepts input features and returns predicted car price
    

### Metrics

- `/metrics`
    
- Exposes metrics for monitoring systems
    

---

## Project Structure

```
app/
│
├── main.py
│
├── api/
│   ├── routes_auth.py
│   ├── routes_predict.py
│   ├── routes_home.py
│   └── routes_health.py
│
├── core/
│   ├── config.py
│   ├── security.py
│   ├── dependencies.py
│   └── exceptions.py
│
├── services/
│   └── model_service.py
│
├── middleware/
│   └── logging_middleware.py
│
├── cache/
│   └── redis_cache.py
│
├── model/
│   └── model.joblib
│
├── utils/
│   └── logger.py
│
data/
training/
notebooks/
```

### Root Files

- `requirements.txt`
    
- `Dockerfile`
    
- `docker-compose.yml`
    
- `prometheus.yml`
    
- `render.yaml`
    
- `.env`
    

---

## Installation & Setup

1. Clone the repository
    

```
git clone https://github.com/<your-username>/car-price-prediction-api.git
cd car-price-prediction-api
```

2. Create and activate a virtual environment
    

```
python -m venv venv
source venv/bin/activate       # macOS/Linux
venv\Scripts\activate          # Windows
```

3. Install dependencies
    

```
pip install -r requirements.txt
```

---

## How to Run

### Using Docker

```
docker-compose up --build
```

---

## Access Interfaces

- FastAPI: [http://localhost:8000/](http://localhost:8000/)
    
- Metrics: [http://localhost:8000/metrics](http://localhost:8000/metrics)
    
- Prometheus: [http://localhost:9090/](http://localhost:9090/)
    
- Grafana: [http://localhost:3000/](http://localhost:3000/)
    

---

## Monitoring & Observability

- Integrated **Prometheus FastAPI Instrumentator**
    
- Metrics exposed via `/metrics` endpoint
    

### Key Metrics

- `http_server_requests_total`
    
- `http_request_duration_seconds_bucket`
    
- `http_request_duration_seconds_sum`
    

### Visualization

- Dashboards for:
    
    - Request volume
        
    - Latency distribution
        
    - System performance
        

### Logging

- Custom middleware logs:
    
    - Incoming requests
        
    - Response status codes
        
    - Execution time
        

---

## Security

### JWT Authentication

- Token-based authentication via `/login`
    
- Required for protected endpoints
    

### API Key Validation

- Enforced using dependency injection
    
- Ensures controlled API access
    

---

## Results

- Efficient real-time prediction system with low latency
    
- Reduced redundant computations using Redis caching
    
- Scalable architecture suitable for production deployment
    
- Full observability through monitoring and logging
    

---

## Future Improvements

- Hyperparameter tuning for improved accuracy
    
- Integration of advanced models (XGBoost, LightGBM)
    
- Batch prediction support
    
- CI/CD pipeline integration
    
- Rate limiting and request throttling
    
- Frontend dashboard for user interaction
    

---

## Tech Stack

**Languages & Libraries**

- Python, Pandas, NumPy, Scikit-learn
    

**Backend**

- FastAPI
    

**Caching**

- Redis
    

**Monitoring**

- Prometheus, Grafana
    

**Deployment**

- Docker, Docker Compose, Render
    
