COS30082 - Applied Machine Learning Assignment

Image Classification of Biological Classes

This repository contains the submission for the COS30082 image classification assignment. The project involves building, training, and comparing two Convolutional Neural Networks (a custom CNN and a transfer learning model) to classify images into 10 biological categories (e.g., 'Amphibia', 'Aves', 'Fungi').

The project includes:

Jupyter notebooks for data exploration and model prototyping.

A trained Keras model (.h5 file).

An interactive web application built with Streamlit to demonstrate the best-performing model.

A final PDF report detailing the methodology and results.

📂 Repository Structure

.
├── 📜 README.md         # This file 

├── 🐍 requirements.txt  # Project dependencies 

├── .gitignore          # Files to ignore 

│

├── 📂 data/            # Contains README on where to get data 

│

├── 📂 frontend/        # Streamlit app 

│   ├── 📄 app.py

│   └── ...

│
├── 📂 models/          # Where the trained model is saved 

│   └── 📄 best_model.h5

│

├── 📂 notebooks/       # All development notebooks 

│   ├── 🧪 1_data_exploration.ipynb

│   └── 🧠 2_model_prototyping.ipynb

│

└── 📂 report/ 

    └── 📄 Assignment_Report.pdf 


🚀 How to Run the Project

Follow these steps to set up the environment and run the web application.

1. Prerequisites

Python 3.8 - 3.11

pip (Python package installer)

2. Clone the Repository

git clone [https://github.com/your-username/cos30082-image-classification.git](https://github.com/your-username/cos30082-image-classification.git)
cd cos30082-image-classification


3. Set Up the Environment

Install all required Python libraries using the requirements.txt file.

pip install -r requirements.txt


4. Get the Data

The image dataset is too large for GitHub. A placeholder README.md is in the data/ folder with instructions.

Download: Get the dataset from the link provided in the assignment.

Place: Unzip the file and ensure the train/ folder is placed inside the data/ directory. The final path should be data/train/....

5. Run the Model Prototyping Notebook (Important)

The trained best_model.h5 is saved in the models/ folder. However, to see how it was generated, you can run the notebooks/2_model_prototyping.ipynb notebook. This notebook contains all code for training and evaluation.

6. Run the Streamlit Web App

This is the interactive demo of the final, best-performing model.

Navigate to the frontend directory:

cd frontend


Run the app.py script:

streamlit run app.py


Open the http://localhost:8501 URL that appears in your terminal to use the app.
