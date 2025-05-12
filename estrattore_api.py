
from fastapi import FastAPI, File, UploadFile
from typing import List
import pytesseract
from PIL import Image
import fitz  # PyMuPDF
import io

app = FastAPI()

# Function to extract text from image
def extract_text_from_image(image: Image.Image) -> str:
    return pytesseract.image_to_string(image)

# Function to extract text from PDF
def extract_text_from_pdf(pdf_bytes: bytes) -> str:
    pdf_document = fitz.open(stream=pdf_bytes, filetype="pdf")
    text = ""
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        text += page.get_text()
    return text

# Function to parse extracted text and find required fields
def parse_text(text: str) -> dict:
    fields = {
        "codice_cliente": "",
        "descrizione_prodotto": "",
        "tipologia": "",
        "classe_resistenza": "",
        "materiale": "",
        "rivestimento": "",
        "patch": "",
        "rondella": "",
        "peso_solo_vite_finita": "",
        "peso_rondella": "",
        "lunghezza_filettatura": "",
        "lunghezza_totale_vite": "",
        "diametro_nominale_filetto": "",
        "tipo_filettatura": "",
        "elenco_norme_richiamate": "",
        "tipo_punta": "",
        "tipo_testa": ""
    }
    
    # Example parsing logic (this should be adapted to the actual format of your documents)
    lines = text.split('')
    for line in lines:
        if "codice cliente" in line.lower():
            fields["codice_cliente"] = line.split(":")[-1].strip()
        elif "descrizione prodotto" in line.lower():
            fields["descrizione_prodotto"] = line.split(":")[-1].strip()
        elif "tipologia" in line.lower():
            fields["tipologia"] = line.split(":")[-1].strip()
        elif "classe di resistenza" in line.lower():
            fields["classe_resistenza"] = line.split(":")[-1].strip()
        elif "materiale" in line.lower():
            fields["materiale"] = line.split(":")[-1].strip()
        elif "rivestimento" in line.lower():
            fields["rivestimento"] = line.split(":")[-1].strip()
        elif "patch" in line.lower():
            fields["patch"] = line.split(":")[-1].strip()
        elif "rondella" in line.lower():
            fields["rondella"] = line.split(":")[-1].strip()
        elif "peso solo vite finita" in line.lower():
            fields["peso_solo_vite_finita"] = line.split(":")[-1].strip()
        elif "peso rondella" in line.lower():
            fields["peso_rondella"] = line.split(":")[-1].strip()
        elif "lunghezza filettatura" in line.lower():
            fields["lunghezza_filettatura"] = line.split(":")[-1].strip()
        elif "lunghezza totale vite" in line.lower():
            fields["lunghezza_totale_vite"] = line.split(":")[-1].strip()
        elif "diametro nominale filetto" in line.lower():
            fields["diametro_nominale_filetto"] = line.split(":")[-1].strip()
        elif "tipo di filettatura" in line.lower():
            fields["tipo_filettatura"] = line.split(":")[-1].strip()
        elif "elenco norme richiamate" in line.lower():
            fields["elenco_norme_richiamate"] = line.split(":")[-1].strip()
        elif "tipo di punta" in line.lower():
            fields["tipo_punta"] = line.split(":")[-1].strip()
        elif "tipo di testa" in line.lower():
            fields["tipo_testa"] = line.split(":")[-1].strip()
    
    return fields

@app.post("/extract-data/")
async def extract_data(file: UploadFile = File(...)):
    file_bytes = await file.read()
    
    if file.content_type.startswith("image/"):
        image = Image.open(io.BytesIO(file_bytes))
        text = extract_text_from_image(image)
    elif file.content_type == "application/pdf":
        text = extract_text_from_pdf(file_bytes)
    else:
        return {"error": "Unsupported file type"}
    
    extracted_data = parse_text(text)
    return extracted_data
