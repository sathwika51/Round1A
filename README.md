# 📝 PDF Heading Extractor

This project extracts **headings** from uploaded PDF documents and saves them into a structured **multilingual JSON** format.

Every time the script is run, the output file (`output_multilang.json`) is updated with fresh results.

---

## 📁 Folder Structure
pdf-heading-extractor/
├── heading_extractor.py # Main code
├── output_multilang.json # Output generated after script runs
├── sample_pdfs/ # Folder to place your input PDFs
├── requirements.txt # Required Python packages
├── Dockerfile # (Optional) For containerized setup
└── README.md # Documentation




## 🧠 APPROACH

The goal of this project is to **automate heading extraction from PDF documents** and store the output in a structured multilingual format (JSON).

Here’s a step-by-step overview of how the system works:

1. **Input Preparation**  
   - The user places one or more PDF files inside the `sample_pdfs/` folder.

2. **Script Execution**  
   - The script `heading_extractor.py` is executed.
   - It scans all PDFs in the folder and extracts **headings** based on structure (e.g., font size, boldness, spacing).

3. **Multilingual Support**  
   - The extracted headings can be translated into multiple languages using libraries like `transformers` or `googletrans` (based on what's implemented).

4. **Output Generation**  
   - The results are saved in `output_multilang.json`.
   - Every time the script is run, this file is **replaced with the latest output**.

5. **Use Cases**  
   - Document indexing
   - Language accessibility
   - Report summarization
   - Medical or academic document preprocessing

This approach ensures that the system is **scalable, easy to run**, and suitable for integration into larger applications or interfaces.



---

## ✅ REQUIREMENTS

Install Python libraries using:

```bash
pip install charset-normalizer==3.4.2
pip install colorama==0.4.6
pip install filelock==3.18.0
pip install fsspec==2025.7.0
pip install huggingface-hub==0.33.4
pip install idna==3.10
pip install Jinja2==3.1.6
pip install MarkupSafe==3.0.2
pip install mpmath==1.3.0
pip install networkx==3.4.2
pip install numpy==2.2.6
pip install packaging==25.0
pip install pip==22.2.2
pip install PyMuPDF==1.26.3
pip install PyYAML==6.0.2
pip install regex==2024.11.6
pip install requests==2.32.4
pip install safetensors==0.5.3
pip install sentencepiece==0.2.0
pip install setuptools==63.2.0
pip install sympy==1.14.0
pip install tokenizers==0.19.1
pip install torch==2.7.1
pip install tqdm==4.67.1
pip install transformers==4.40.2
pip install typing_extensions==4.14.1
pip install urllib3==2.5.0



## 🚀 TO RUN

✅ Prepare Input PDFs
Place all the PDF files you want to extract headings from into the sample_pdfs/ folder inside your project directory.

📦 Install Required Libraries
Open Command Prompt or terminal and install the required Python packages:

pip install PyMuPDF transformers torch
# and other libraries listed above

▶️ Run the Script
Use this command to execute the heading extractor:
py -3.10 heading_extractor.py

📄 View the Output
After execution, the file output_multilang.json will be updated with the latest extracted headings from your PDFs.








