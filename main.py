import storage
from user_console_interaction import UserConsoleInteraction
import passport_protection
import pdfToJpg
import imgToPdf

def main():
    #UserConsoleInteraction().start()
    # конвертация .doc and .docx  pdf формат, результат в папке с проектом


    docs_path = 'C:\\Users\\OperTech\\Desktop\\Калиброн\\'
    output_dir = 'C:\\Users\\OperTech\\Desktop\\Калиброн\\result_pdf'
    passport_protection.PassportProtection(docs_path, output_dir).start()

    #dir_pdf_for_jpg = 'C:\\Users\\OperTech\\Desktop\\Калиброн\\result_pdf\\Паспорт Стойка 15-СТМ Калиброн.pdf'
    #dir_out_for_jpg = 'C:\\Users\\OperTech\\Desktop\\Калиброн\\result_pdf'
    #pdfToJpg.PdfToJpg(dir_pdf_for_jpg, dir_out_for_jpg).convert()
    #storage.Storage().delete_folder_with_files(dir_out_for_jpg + '\\template')

    #dir_input_jpgs = 'C:\\Users\\OperTech\\Desktop\\Калиброн\\'
    #dir_output_jpgs = 'C:\\Users\\OperTech\\Desktop\\Калиброн\\result_pdf'
    #imgToPdf.ImgToPdf(dir_input_jpgs, dir_output_jpgs).convert()


if __name__ == '__main__':
    main()
