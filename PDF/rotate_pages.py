from PyPDF2 import PdfFileReader, PdfFileWriter


def rotate_pages(path_pdf):
    pdf_writer = PdfFileWriter()                    # obiekt klasy zapisujacej
    pdf_reader = PdfFileReader(path_pdf)            # obiekt klasy czytajacej

    page_1 = pdf_reader.getPage(0).rotateClockwise(90)  # obrot strony o 90 stopni
    pdf_writer.addPage(page_1)                          # dodanie strony do tworzonego obiektu pdf
    page_2 = pdf_reader.getPage(1).rotateCounterClockwise(90)
    pdf_writer.addPage(page_2)

    pdf_writer.addPage(pdf_reader.getPage(2))           # dodanie nieobroconej strony do obiektu

    with open('rotate_pages.pdf', 'wb') as f:
        pdf_writer.write(f)


if __name__ == "__main__":
    path = 'reportlab-userguide.pdf'
    rotate_pages(path)
