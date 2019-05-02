from PyPDF2 import PdfFileReader


def extract_information(path_pdf):          # ścieżka do pliku jako argument
    with open(path_pdf, 'rb') as f:         # tryb open jako 'rb' -> czytaj
        pdf = PdfFileReader(f)
        info = pdf.getDocumentInfo()
        pages = pdf.getNumPages()

        txt = f"""                          
        Information about {path_pdf}
        
        Author: {info.author}
        Creator: {info.creator}
        Producer: {info.producer}
        Subject: {info.subject}
        Title: {info.title}
        Number of pages {pages}
        
        """
        print(txt)


if __name__ == '__main__':
    path = 'reportlab-userguide.pdf'
    extract_information(path)
