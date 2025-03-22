# Testing RF-DETR Model

This repository demonstrates how to run and test the RF-DETR model. It includes scripts and sample video files to help you get started with processing video data using the model.

## Repository Link

[GitHub Repository](https://github.com/Shaik-Hamzah123/RF-DETR-Test)

## Overview

The repository contains the following key files:
- **run_model.py**: The main script to run the RF-DETR model on video input.
- **requirements.txt**: Contains a list of Python packages needed for the project.
- **walking.mp4**: The sample input video file.
- **output_compressed.mp4**: The processed output video.
- **.gitignore**: Specifies files and directories to be ignored by Git.
- **classes.json**: A JSON file containing the class mappings used by the model.

## Prerequisites

- **Python 3.6+**: Ensure you have Python installed.
- **Pip**: Package installer for Python.
- (Optional) **Virtual Environment**: It is recommended to use a virtual environment for dependency management.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Shaik-Hamzah123/RF-DETR-Test.git
   cd RF-DETR-Test
   ```

2. **(Optional) Create and activate a virtual environment:**

   ```bash
   python -m venv env
   source env/bin/activate  # For Windows: env\Scripts\activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the model:**

   Execute the main script to start processing the input video:

   ```bash
   python run_model.py
   ```

2. **Review the output:**

   - The script processes the input video (`walking.mp4`) and generates a processed version (`output_compressed.mp4`).
   - Check the console output for any messages or errors.

## Troubleshooting

- **Missing Modules:**  
  If you receive a `ModuleNotFoundError`, make sure you have installed all dependencies with:
  
  ```bash
  pip install -r requirements.txt
  ```

- **Environment Issues:**  
  If you experience issues, consider creating a new virtual environment and reinstalling the dependencies.


Enjoy testing the RF-DETR model! :) 
