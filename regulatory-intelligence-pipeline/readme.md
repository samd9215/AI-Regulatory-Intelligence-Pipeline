# AI Regulatory Intelligence Pipeline

AI-powered regulatory monitoring platform built with Python and FastAPI.

## Features

- Regulatory scraping
- LLM summarization
- PostgreSQL storage
- REST API
- Dockerized deployment
- CI/CD testing

## Tech Stack

- Python
- FastAPI
- PostgreSQL
- OpenAI API
- Docker

## Setup

### Clone

git clone <repo-url>

### Install

pip install -r requirements.txt

### Run

uvicorn app.main:app --reload

## API Endpoints

GET /regulations

POST /ingest