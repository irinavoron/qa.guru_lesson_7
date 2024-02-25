from zipfile import ZipFile
from pypdf import PdfReader

from tests.conftest import resource_zip_path


def test_pdf():
    with ZipFile(resource_zip_path) as zip_file:
        with zip_file.open('PDF.pdf') as pdf_file:
            reader = PdfReader(pdf_file)
            number_of_pages = len(reader.pages)
    assert number_of_pages == 4

