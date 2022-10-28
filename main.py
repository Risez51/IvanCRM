import docToPdf
from user_console_interaction import UserConsoleInteraction


def main():

    UserConsoleInteraction().start()
    # конвертация .doc and .docx  pdf формат, результат в папке с проектом
    #docToPdf.DocToPdf('E:\\Калиброн\\ГОСРЕЕСТР\\Стойки, кронциркули, уровни, угольники').start_convert()
    #docToPdf.DocToPdf('E:\\Калиброн\\ГОСРЕЕСТР\\от 24.10.22').convert_word_to_pdf()
    #docToPdf.DocToPdf('E:\\Калиброн\\ГОСРЕЕСТР\\Стойки, кронциркули, уровни, угольники\\test').add_watermark()


if __name__ == '__main__':
    main()
