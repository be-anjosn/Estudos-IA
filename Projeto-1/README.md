# Customer Feedback Analysis Pipeline with Ollama and Pydantic

Automated pipeline for batch processing customer reviews using local Large Language Models via **Ollama** and structured validation with **Pydantic**.

The system reads raw reviews from a CSV file, processes each entry using a local LLM to extract sentiment and customer service metrics, validates data consistency, and exports the structured results to a new CSV file.

Check Notion Documentation at [🟦 Notion - Project 1 ](https://app.notion.com/p/Project-1-Python-Pydantic-3f32d68c3578801bb0a1f3e07c36a440?source=copy_link)
---

## 📁 Project Structure

```text
Projeto-1/
├── data/
│   ├── incoming_feedback.csv   # Raw input feedback data
│   └── output_feedback.csv     # Structured, validated output results
├── src/
│   ├── AI.py                   # Ollama local API integration and prompt logic
│   ├── Models.py               # Pydantic schemas and consistency rules
│   └── main.py                 # Pipeline orchestrator
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
```

---

## 🛠️ Prerequisites

- **Python**: Version 3.10 or higher.
- **Git**: Installed.
- **Ollama**: Installed and running locally.

---

## 🚀 Setup and Installation

### 1. Install and Set Up Ollama

1. Download and install Ollama for your operating system:
   - **Windows / macOS**: Download installer from [ollama.com/download](https://ollama.com/download).
   - **Linux**: Run the official installation script:
     ```bash
     curl -fsSL [https://ollama.com/install.sh](https://ollama.com/install.sh) | sh
     ```

2. Ensure the Ollama service is active:
   - On Windows/macOS, verify the icon is active in your system tray.
   - To verify via command line:
     ```bash
     curl http://localhost:11434/
     # Expected response: "Ollama is running"
     ```

3. Pull your target model (e.g., `llama3.2:3b`):
   ```bash
   ollama pull llama3.2:3b
   ```

---

### 2. Download Only the `Projeto-1` Directory

To download solely the `Projeto-1` subfolder instead of the entire repository, run:

```bash
git clone --depth 1 --filter=blob:none --sparse [https://github.com/be-anjosn/Estudos-IA.git](https://github.com/be-anjosn/Estudos-IA.git)
cd Estudos-IA
git sparse-checkout set Projeto-1
cd Projeto-1
```

---

### 3. Configure the Python Environment

1. Create and activate a virtual environment inside the `Projeto-1` folder:
   - **Windows (PowerShell)**:
     ```powershell
     python -m venv venv
     .\venv\Scripts\Activate.ps1
     ```
   - **Linux / macOS**:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

2. Install project dependencies:
   ```bash
   pip install -r requirements.txt
   ```

> **Sample `requirements.txt`:**
> ```text
> ollama>=0.3.0
> pydantic>=2.7.0
> ```

---

## 📊 Data Formats

### Input (`data/incoming_feedback.csv`)
Comma-separated CSV containing unique IDs and customer review texts:
```csv
id,customer_text
C1,"My name is Robert Taylor. The product arrived ahead of schedule and the packaging was in pristine condition. Highly recommend!"
C2,"Terrible experience. The item arrived broken, they do not answer my support emails, and they refused to give me a refund."
```

### Output (`data/output_feedback.csv`)
Generated structured output validated against Pydantic models:
```csv
feeling,customer_service_rating,short_summary,name
positive,5,"Product arrived ahead of schedule and packaging was in pristine condition.",Robert Taylor
negative,1,"Item arrived broken, no support, and no refund.",Unknown
```

---

## ▶️ Running the Pipeline

With the Ollama daemon running and your virtual environment activated, navigate to the `src` folder and execute:

```powershell
cd src
python main.py
```

The execution flow processes each record sequentially:
1. Reads each customer review line from `incoming_feedback.csv`.
2. Sends the text to `ai_generation()` in `AI.py`.
3. Parses and validates the LLM JSON response against `Models.AnaliseFeedback`.
4. Enforces business logic (e.g., positive sentiment must have a rating >= 4).
5. Appends the validated dictionary records to `data/output_feedback.csv`.

---

## 🔍 Troubleshooting & Common Errors
- **`ValueError: Invalid format specifier ...`**: Happens when unescaped curly braces `{` and `}` are used inside Python f-strings. Use raw multiline strings combined with `.replace("__INPUT__", text)` or escape braces as `{{` and `}}`.
- **`ValidationError: Inconsistency: A positive sentiment cannot have a score of 2 or lower!`**: Occurs when small local models hallucinate positive sentiment on negative reviews. Ensure few-shot examples in `AI.py` explicitly map complaints to `negative` ratings (`1` or `2`).
- **Connection Refused (`http://localhost:11434`)**: Verify that the local Ollama daemon service is active and reachable before executing the pipeline.
