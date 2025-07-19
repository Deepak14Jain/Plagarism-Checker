# Plagiarism Checker

A web application to detect plagiarism between two text files using machine learning and natural language processing. The project consists of a backend API (Flask) and a frontend UI (Streamlit).

---

## Features

- Upload original and submission text files.
- Detects similarity and plagiarism probability.
- Highlights matching text segments.
- User-friendly web interface.

---

## Project Structure

```
Plagarism-Checker/
│
├── streamlit_app/
│   └── app.py                # Streamlit frontend
├── flask_api/
│   ├── app.py                # Flask API backend
│   └── model.py              # Script to train and save the model
|   └── utils.py.py
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
```

---

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <repo-url>
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Train the model (if not already present):**
   ```bash
   python3 flask_api/model.py
   ```

4. **Start the backend Flask API:**
   ```bash
   python3 flask_api/app.py
   ```
   The API will run on `http://localhost:5050`.

5. **Start the Streamlit frontend:**
   ```bash
   streamlit run streamlit_app/app.py
   ```
   The UI will open in your browser.

---

## API Endpoints

### 1. `POST /check`

**Description:**  
Checks for plagiarism between two uploaded text files. ```PFA API.bru```

**Request:**  
- `multipart/form-data` with two files (keys):
  - `original`: The original text file.
  - `submission`: The submission text file.

**Example using `curl`:**
```bash
curl -X POST http://localhost:5000/check \
  -F "original=@original.txt" \
  -F "submission=@submission.txt"
```

**Response:**
```json
{
  "highlighted_original": "<mark>Artificial intelligence is a </mark><mark>growing </mark>f<mark>i</mark>eld<mark> of s</mark>tudy<mark>.</mark>",
  "highlighted_submission": "<mark>Artificial intelligence is a </mark>rapidly <mark>growing </mark>doma<mark>i</mark>n<mark> of s</mark>cience<mark>.</mark>",
  "plagiarized": true,
  "probability": 0.5165,
  "similarity_score": 0.5056
}
```
- `similarity_score`: Cosine similarity between the documents (0 to 1).
- `probability`: Model's predicted probability of plagiarism (0 to 1).
- `plagiarized`: Boolean, whether plagiarism is detected.
- `highlighted_original`: HTML with highlighted matching text in the original.
- `highlighted_submission`: HTML with highlighted matching text in the submission.

---

## Frontend

- Accessible via Streamlit at `http://localhost:8501` (default).
- Upload files, click "Check Plagiarism", and view results with highlighted matches.

---
> **Note:**  
> - Ensure both backend and frontend are running for full functionality.
> - For best results, use plain text files (`.txt`).
> - The backend API defaults to `http://localhost:5050` (update the Streamlit app if you change this).
> - If you encounter connection errors, check that the backend server is running and accessible.
> - Model retraining may be required if you change the detection logic or data.

---

## Contact

For any questions, suggestions, or issues, feel free to reach out directly via project channels, GitHub. I’m happy to help and eager to learn!

My mail ID: deepak.jain05@sap.com or jaindeepak1401+git@gmail.com

>MIT License – feel free to reuse with credit.