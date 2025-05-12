
# Estrattore API

Questa API FastAPI riceve un file (immagine o PDF), estrae testo tramite OCR o parsing PDF, e restituisce i seguenti campi:
1. Codice cliente
2. Descrizione prodotto
3. Tipologia
4. Classe di resistenza
5. Materiale
6. Rivestimento
7. Patch
8. Rondella
9. Peso solo vite finita
10. Peso rondella
11. Lunghezza filettatura
12. Lunghezza totale vite
13. Diametro nominale filetto
14. Tipo di filettatura
15. Elenco norme richiamate
16. Tipo di punta
17. Tipo di testa

## Installazione delle dipendenze

Assicurati di avere installato le seguenti dipendenze:

pip install fastapi uvicorn pytesseract pillow pymupdf python-multipart

## Avvio dell'API

Per avviare l'API, esegui il seguente comando:

uvicorn estrattore_api:app --reload
