
from user_console_interaction import UserConsoleInteraction
import passport_protection
import pdfToJpg

def main():
    #UserConsoleInteraction().start()
    # конвертация .doc and .docx  pdf формат, результат в папке с проектом


    docs_path = 'C:\\Users\\Ivan-pc\\Desktop\\Калиброн\\pdf\\word\\'
    passport_protection.PassportProtection(docs_path).start()

    #dir_pdf_for_jpg = 'C:\\Users\\Ivan-pc\\Desktop\\Калиброн\\pdf\\word\\Паспорт ГИ SHAN.pdf'
    #dir_out_for_jpg = 'C:\\Users\\Ivan-pc\\Desktop\\Калиброн\\pdf\\word\\'
    #pdfToJpg.PdfToJpg(dir_pdf_for_jpg, dir_out_for_jpg).convert()


if __name__ == '__main__':
    main()
