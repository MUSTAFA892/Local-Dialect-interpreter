
---

# Local Dialect Interpreter API

This project provides a **Local Dialect Interpreter API** that translates informal local dialects into standard English in real-time. It helps non-native speakers or tourists understand local expressions by identifying the language and providing the corresponding translation.

### Tech Stack:
- **FastAPI**: For creating the API and handling HTTP requests.
- **Google Gemini API**: Used for generating content (translations and dialect interpretation).
- **LangChain**: For handling prompts and language models.
- **Python**: For the development of the API logic.
- **Uvicorn**: For running the FastAPI app.
- **Pydantic**: For validating the request data.
- **dotenv**: For loading environment variables from a `.env` file.

### Features:
- Identify the dialect language of a given phrase.
- Translate the dialect into standard English.
- Real-time response for local dialect translation.

---

## Installation

### Step 1: Clone the Repository
Clone the repository to your local machine using the following command:

```bash
git clone https://github.com/your-username/Local-Dialect-Interpreter.git
cd Local-Dialect-Interpreter
```

### Step 2: Set Up Virtual Environment
Create and activate a Python virtual environment:

```bash
# On Linux/macOS
python3 -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate
```

### Step 3: Install Dependencies
Install the required dependencies using `pip`:

```bash
pip install -r requirements.txt
```

Make sure to include the following in your `requirements.txt`:

```
fastapi
uvicorn
pydantic
google-genai
langchain
python-dotenv
google-auth
google-auth-oauthlib
google-auth-httplib2
```

### Step 4: Set Up Environment Variables
Create a `.env` file in the root of your project and add the following variables:

```
GEMINI_API_KEY=your_gemini_api_key
LANGCHAIN_API_KEY=your_langchain_api_key
GOOGLE_APPLICATION_CREDENTIALS=path_to_your_service_account_key_json
```

- **GEMINI_API_KEY**: Your API key from Google Gemini (this will be used to access Google’s generative models).
- **LANGCHAIN_API_KEY**: Your LangChain API key for tracking and usage purposes.
- **GOOGLE_APPLICATION_CREDENTIALS**: The path to your Google Cloud service account key (`key.json`).

---

## How to Get the `key.json` (Google Cloud Service Account Key)

### Step 1: Create a Google Cloud Project
1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Click on the **Project Dropdown** and create a new project.

### Step 2: Enable Gemini API
1. In the Google Cloud Console, navigate to **APIs & Services > Library**.
2. Search for **Gemini API** and enable it for your project.

### Step 3: Create a Service Account
1. Go to **IAM & Admin > Service Accounts**.
2. Click on **Create Service Account**.
3. Name your service account and give it **Editor** or **Owner** permissions (depending on your needs).
4. After creating the service account, click on it to open its details.
5. Under **Keys**, click on **Add Key > Create New Key** and select **JSON**.
6. Save the JSON file, and place it in your project directory (e.g., `key.json`).

### Step 4: Add `key.json` Path to `.env`
Once you have the `key.json`, set the environment variable in your `.env` file:

```
GOOGLE_APPLICATION_CREDENTIALS=path_to_your_service_account_key_json
```

Make sure to replace `path_to_your_service_account_key_json` with the actual file path to the `key.json` file.

---

## Running the Application

### Step 1: Run FastAPI App
To start the FastAPI server, use **Uvicorn**:

```bash
uvicorn app:app --reload
```

This will start the API locally on `http://127.0.0.1:8000`.

### Step 2: Test with Thunder Client or Postman

You can use **Thunder Client** (VSCode extension) or **Postman** to test the API.

#### Example Request:

**POST** request to:

```
http://127.0.0.1:8000/generate-response
```

**Request Body (JSON)**:

```json
{
  "question": "Wassup, bro?"
}
```

#### Example Response:

```json
{
  "response": "Language: American English (Informal)\nTranslation: Hello, brother."
}
```

---

## API Endpoints

### `POST /generate-response`
This endpoint takes a dialect and returns the language of the dialect along with its English translation.

#### Request Body:
```json
{
  "question": "Your local dialect expression here"
}
```

#### Response:
```json
{
  "response": "Language: [Dialect Language]\nTranslation: [English Translation]"
}
```



---

## Frontend Setup with Flask

### 1. **Flask for Frontend**:
   - **Flask** will be used to serve the frontend part of the application (HTML, CSS, and JavaScript files).
   - It will interact with your FastAPI backend via HTTP requests (using AJAX or fetch API in the frontend).

### 2. **Directory Structure**:
   - **`templates/`**: This directory will hold your HTML files (e.g., `index.html`).
   - **`static/`**: This directory will store your static files such as **CSS** and **JavaScript** (e.g., `style.css`, `script.js`).

### 3. **Flask Setup**:
   - In your Flask app (`app.py`), set up routes for rendering the HTML files and handling AJAX requests.
   - **Flask Routes**:
     - The main route (`/`) will render the HTML page with the input fields.
     - The `/translate` route will handle POST requests from the frontend to translate dialect text, and return the translation.

### 4. **Frontend Logic**:
   - **HTML**: Basic structure for the frontend interface.
   - **CSS**: Used to style the page (optional but recommended for design).
   - **JavaScript**: Handles sending AJAX requests to the Flask backend and displaying the translation result. You will send a POST request with the text input from the user, and display the translation response.

### 5. **Communication Between Frontend and Backend**:
   - The Flask app will accept data from the frontend (e.g., a local dialect phrase), and use your backend API (FastAPI) to translate it.
   - This can be done using JavaScript's `fetch` API or `XMLHttpRequest` to make POST requests to the FastAPI endpoints.

### 6. **Environment Variables**:
   - Add a `.env` file in the root of your project for storing keys and sensitive information such as `GEMINI_API_KEY`.
   - Load the `.env` variables in your backend using `dotenv` in Python and in Flask for frontend key management.

---

### Example Overview:

- **Backend (FastAPI)**: Handles dialect translation and processing.
- **Frontend (Flask)**: Presents an interface to the user, takes input text (local dialect), and sends it to the FastAPI backend for translation. It then displays the result on the webpage.

---

### `.env` Setup:
- Store sensitive data like API keys in a `.env` file for both backend and frontend services.
- Example variables to include in your `.env`:
   ```
   GEMINI_API_KEY=your_gemini_api_key
   LANGCHAIN_API_KEY=your_langchain_api_key
   GOOGLE_APPLICATION_CREDENTIALS=path_to_your_service_account_key_json
   ```

---

### Running the Application:
1. **Backend**: Use Uvicorn to run the FastAPI server for processing dialect translation.
2. **Frontend**: Use Flask to serve HTML pages and handle requests from the user interface.


---

## License

This project is licensed under the MIT License.

---

## Contributing

Feel free to fork this project and submit pull requests with improvements or bug fixes!

---
   