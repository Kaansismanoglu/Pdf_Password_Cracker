import PyPDF2

def open_encrypted_pdf(file_path, password):
    try:
        with open(file_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            if pdf_reader.is_encrypted:
                if pdf_reader.decrypt(password) == 1:
                    print("PDF is open successfully. Your Password:", password)
                    return True
                else:
                    print("Incorrect Password:", password)
            else:
                print("PDF hasn't password.")
    except Exception as e:
        print("PDF opening error:", e)
    return False

start_num = 400000
end_num = 700000
pdf_file = "Your File"

for num in range(start_num, end_num+1):
    password = str(num)
    if open_encrypted_pdf(pdf_file, password):
        break
