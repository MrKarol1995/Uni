import PyPDF2

def merge_pdfs(input_files, output_file='Mega.pdf'):
    """
    Łączy kilka plików PDF w jeden dokument.
    """
    merged_pdf = PyPDF2.PdfMerger()

    # Dodaj pliki PDF do łączonego dokumentu
    for input_file in input_files:
        merged_pdf.append(input_file)

    # Zapisz łączony dokument do pliku wyjściowego
    with open(output_file, 'wb') as output:
        merged_pdf.write(output)

    print(f'Pliki zostały połączone w dokument: {output_file}')

input_files = ['plik1.pdf', 'plik2.pdf', 'plik3.pdf']
output_file = 'Mega.pdf'

merge_pdfs(input_files, output_file)
