from PyPDF2 import PdfFileReader, PdfFileWriter


def split(pdf_path, name_of_split):
    pdf_reader = PdfFileReader(pdf_path)                        # create read pdf object

    for page in range(pdf_reader.getNumPages()):                # each page to each pdf file
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(pdf_reader.getPage(page))            # add simply page to write pdf object

        output=f"{name_of_split}{page}.pdf"                     # format stringa nazwy plikow po podziale
        with open(output, 'wb') as f:
            pdf_writer.write(f)


if __name__ == "__main__":
    path = "rotate_pages.pdf"
    split(path, name_of_split="rotate")
