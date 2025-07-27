import pdfplumber, re, json, os
from deep_translator import GoogleTranslator

INPUT_DIR = "input_pdfs"
OUTPUT_JSON = "output.json"

# Heuristic patterns for headings
def detect_headings(text):
    headings = []
    for line in text.splitlines():
        clean = re.sub(r"^[\d\.\-•\s]+", "", line).strip()
        if not clean:
            continue

        # Heading detection rules
        if re.match(r"^[A-Z][A-Z\s]{3,}$", clean):
            level = "H1"
        elif re.match(r"^[A-Z][a-zA-Z\s]{3,}$", clean):
            level = "H2"
        elif re.match(r"^\w.*:$", clean):
            level = "H3"
        else:
            continue
        headings.append((level, clean))
    return headings

# Translation using Deep Translator (no coroutine issue)
from deep_translator import GoogleTranslator
from deep_translator import GoogleTranslator

def translate(text, dest_lang):
    try:
        return GoogleTranslator(source='auto', target=dest_lang).translate(text)
    except Exception as e:
        return f"[Translation error: {str(e)}]"


# Process a single PDF
def process_pdf(path):
    with pdfplumber.open(path) as pdf:
        full_text = ""
        for page in pdf.pages:
            full_text += page.extract_text() + "\n"
        return detect_headings(full_text)

# Main function
def main():
    if not os.path.exists(INPUT_DIR):
        print(f" Folder '{INPUT_DIR}' not found. Please create it and add PDFs.")
        return

    all_results = {}

    for filename in os.listdir(INPUT_DIR):
        if not filename.lower().endswith(".pdf"):
            continue
        path = os.path.join(INPUT_DIR, filename)
        print(f"Processing {filename}...")

        headings = process_pdf(path)
        translated = []
        for level, text in headings:
            translated.append({
                "level": level,
                "en": text,
                "hi": translate(text, "hi"),
                "ja": translate(text, "ja")
            })
        all_results[filename] = translated

    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(all_results, f, ensure_ascii=False, indent=2)

    print(f"\n Done! Headings saved to {OUTPUT_JSON}")

if __name__ == "__main__":
    main()
