Gemini Pro Streamlit Chatbot
Overview
This repository contains a Streamlit-based chatbot powered by the Gemini API. The chatbot allows users to interact with a variety of services by making requests to Gemini's API for relevant data.

Steps to Execute the Project
1. Install Python 3
Streamlit requires Python 3.7 or higher. If Python 3 is not already installed:

Download the latest Python 3 version from python.org.
Install Python and ensure you check the option "Add Python to PATH" during installation.

2. Add the API Key to the .env File
Create or edit a .env file in the project directory and add the following line:

GEMINI_API_KEY=your_gemini_api_key_here

3. Create a Virtual Environment

Run the following command to create a virtual environment:
python3 -m venv venv

Activate the Virtual Environment (Windows)
Run this command to activate the virtual environment:
venv\Scripts\activate

4. Install Dependencies
Install the required dependencies listed in the requirements.txt file:
pip install -r requirements.txt

5. Run the Application
Start the Streamlit application by running:
streamlit run main.py

6. Access the Application
After running the command, open the URL displayed in the terminal, such as:
http://localhost:8501

Additional Information
Technologies Used: Python, Streamlit, Gemini API
Project Structure: main.py (application entry point), requirements.txt (dependencies), .env (environment variables)

