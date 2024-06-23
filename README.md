<h1 align="center">
Zocket - Ad Creative Recognition Pipeline
</h1>

<hr/>

## Setup Instructions (For Local)

### 1. Setting up the Python Virtual Environment (venv)

#### For Windows
```bash
# Navigate to the project directory
cd my_project_directory

# Create a virtual environment named 'venv'
python -m venv venv

# Activate the virtual environment
venv\Scripts\activate

# Ensure the virtual environment is activated
# Install the required packages from requirements.txt
pip install -r requirements.txt

# Ensure the virtual environment is activated
# Run the Streamlit application
streamlit run app.py
```

### Steps to Setup GOOGLE_API_KEY
1. Go to the Google Cloud Studio.
2. Create a new project or select an existing project.
3. Enable the necessary APIs for your project.
4. In the left menu, click on "APIs & Services" and then select "Credentials".
5. Click on "Create Credentials" and choose the appropriate credential type (API key).
6. Copy the provided API key.
7. In your code, replace the placeholder API key with the copied API key.

### Steps to Setup HUGGINGFACE_API_KEY
1. Go to the Huggingface website (https://huggingface.co/).
2. Sign in to your account or create a new account.
3. Once logged in, click on your profile picture and select "Settings".
4. In the navigation bar on the left, click on "API token".
5. Click on "New token" and provide a name for your token.
6. Copy the generated API token.
7. In your code, replace the placeholder API token with the copied API token.

## Experiment Notebook

The notebook "Zocket.ipynb" contains all the code snippets related to the project experiment.

### Streamlit Apllication Screenshots
<hr>
<img src="images/Screenshot 2024-06-23 133622.png" name="">
<img src="images/Screenshot 2024-06-23 134538.png" name="">

### Jupyter Notebook Walkthrough
<hr>
Loading Images
<img src="images/Screenshot 2024-06-23 134834.png" name="">
</br>
Generating the Captions for the Images using Florence-2-Large Model from Huggingface
<img src="images/Screenshot 2024-06-23 133913.png" name="">
</br>
Object Detection
<img src="images/Screenshot 2024-06-23 133940.png" name="">
</br>
OCR Detection
<img src="images/Screenshot 2024-06-23 133950.png" name="">
</br>
Generating Metadata for the Image for Processing if it is Ad Capaign or Not
<img src="images/Screenshot 2024-06-23 134019.png" name="">
</br>
Analyzing the metadata/Caption for predictions
<img src="images/Screenshot 2024-06-23 134032.png" name="">
</br>
