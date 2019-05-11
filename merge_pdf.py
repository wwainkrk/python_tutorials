from PyPDF2 import PdfFileWriter, PdfFileReader


def merge_pdfs(pdf_paths, output):                  # argumenty jako sciezki plikow i sciezka jednego zmergowanego pliku
    pdf_writer = PdfFileWriter()

    for pdf_path in pdf_paths:                      # czytamy kazdy pdf podany ze sciezek
        pdf_reader = PdfFileReader(pdf_path)

        for page in range(pdf_reader.getNumPages()):       # kazda strone dodajemy do obiektu write
            pdf_writer.addPage(pdf_reader.getPage(page))

    with open(output, 'wb') as f:
        pdf_writer.write(f)                         # po petlach zapisujemy plik, w podanej lokalizacji jako parametr


if __name__ == "__main__":
    paths = ['rotate_pages.pdf','reportlab-userguide.pdf']
    merge_pdfs(paths, 'merge.pdf')
