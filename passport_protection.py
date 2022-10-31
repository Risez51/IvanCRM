from storage import Storage
from docToPdf import DocToPdf
from watermark_for_pdf import Watermark


class PassportProtection:
    def __init__(self, input_files_path: str, output_files_path: str):
        self.input_files_path = input_files_path
        self.output_files_path = output_files_path

    def start(self):
        input_files = Storage.get_files_name(self.input_files_path)
        for current_file in input_files:
            DocToPdf(self.input_files_path, self.output_files_path).convert(current_file)

        output_files = Storage.get_files_name(self.output_files_path)
        for current_file in output_files:
            Watermark(f'{self.output_files_path}\\{current_file}').add_watermark()

