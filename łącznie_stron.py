import PyPDF2
#Nazwa pliku wejściowego
input_file = "Sylabus.pdf"

page_count = int(input("Podaj liczbę stron, która ma być w jednym pliku: "))

# Otwieranie pliku wejściowego
pdf_file = open(input_file, 'rb')
pdf_reader = PyPDF2.PdfReader(pdf_file)

# Liczba stron w pliku wejściowym
num_pages = len(pdf_reader.pages)
if page_count>num_pages:
    quit("nie mo")

print("liczba stron pliku: ", num_pages)
for i in range(0, num_pages, page_count):
    output_pdf = PyPDF2.PdfWriter()

    for j in range(i, i+page_count):
        if j < num_pages:
            output_pdf.add_page((pdf_reader.pages[j]))

    output_filename = f"output_{i//page_count}.pdf"
    with open(output_filename, "wb") as out:
        output_pdf.write(out)

# Zamykanie pliku
pdf_file.close()
