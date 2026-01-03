# IntelliDent AI – AI Engineer Internship Assignment

This repository contains solutions for selected technical tasks completed
as part of the AI Engineer Internship selection process at IntelliDent AI.

The focus of this submission is on:
- Image preprocessing and analysis
- Dataset quality validation
- Basic API development

## Implemented Tasks

- **Task 1: Medical Image Loader & Analyzer**  
  Loads color images, converts them to grayscale, resizes them to a fixed
  resolution, and computes basic statistics such as image resolution and
  mean pixel intensity.

- **Task 3: Image Quality Checker**  
  Performs basic dataset quality checks using variance of Laplacian
  for blur detection and mean pixel intensity for brightness evaluation.

- **Task 8: FastAPI Image Upload API**  
  A simple FastAPI endpoint that accepts an image upload and returns
  image metadata such as format and dimensions.

## Project Structure

intellident-ai-assignment/
│
├── data/
│ ├── images/ # Original input images
│ └── processed/ # Grayscale, resized images
│
├── scripts/
│ ├── image_loader.py
│ └── quality_checker.py
│
├── api/
│ └── main.py # FastAPI application
│
├── requirements.txt
└── README.md

shell
Copy code

## How to Run

### 1. Install dependencies
```bash
pip install -r requirements.txt
2. Run image preprocessing (Task 1)
bash
Copy code
python scripts/image_loader.py
3. Run image quality checker (Task 3)
bash
Copy code
python scripts/quality_checker.py
4. Run FastAPI application (Task 8)
bash
Copy code
uvicorn api.main:app --reload
Open browser:

arduino
Copy code
http://127.0.0.1:8000/docs
Notes
Public color images were used to demonstrate image preprocessing.

Thresholds for blur and brightness are intentionally simple and
explainable to reflect real-world dataset validation logic.

The tasks are designed to demonstrate clear thinking, clean structure,
and basic AI system understanding rather than model complexity.
