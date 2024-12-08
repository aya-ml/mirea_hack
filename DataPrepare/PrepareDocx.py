import random
from docx import Document

class RussianDocxGenerator:
    file_counter = 1

    @staticmethod
    def load_russian_words(word_file_path):
        with open(word_file_path, encoding="windows-1251") as f:
            return [line.strip() for line in f.readlines()]

    @staticmethod
    def generate_random_real_words(word_list, num_words):
        return random.sample(word_list, num_words)

    @classmethod
    def create_docx(cls, word_file_path, pages=100, output_dir='.'):
        russian_word_list = cls.load_russian_words(word_file_path)
        filtered_word_list = [word for word in russian_word_list if 4 <= len(word) <= 10]

        doc = Document()

        for page in range(pages):
            content_types = ['table', 'list']
            random.shuffle(content_types)

            for content_type in content_types:
                if content_type == 'table':
                    rows, cols = random.randint(1, 15), random.randint(1, 9)
                    table = doc.add_table(rows=rows, cols=cols)
                    table.style = 'Table Grid'
                    unique_words = cls.generate_random_real_words(filtered_word_list, rows * cols)
                    for i in range(rows):
                        for j in range(cols):
                            table.cell(i, j).text = unique_words.pop()

                    doc.add_paragraph()
                elif content_type == 'list':
                    num_items = random.randint(1, 15)
                    unique_words = cls.generate_random_real_words(filtered_word_list, num_items)
                    for word in unique_words:
                        doc.add_paragraph(word, style='List Paragraph')
                    doc.add_paragraph()

        file_name = f"{output_dir}/Generated_Docx_{cls.file_counter}.docx"
        doc.save(file_name)

        cls.file_counter += 1
        print(f"Файл сохранен: {file_name}")


class DocxParser:
    @classmethod
    def parse_tables(cls, doc: Document) -> list:
        return [
            [
                [cell.text.strip() for cell in row.cells]
                for row in table.rows
            ]
            for table in doc.tables
        ]

    @classmethod
    def parse_lists(cls, doc: Document) -> list:
        lists = []
        current_list = []

        for paragraph in doc.paragraphs:
            text = paragraph.text.strip()
            if not text:
                if current_list:
                    lists.append(current_list)
                    current_list = []
                continue

            style_name = paragraph.style.name.lower()
            is_list = "list paragraph" in style_name

            if is_list:
                current_list.append(text)
            else:
                if current_list:
                    lists.append(current_list)
                    current_list = []

        if current_list:
            lists.append(current_list)

        return lists

    @classmethod
    def parse_docx(cls, file_path: str) -> dict:
        doc = Document(file_path)
        return {
            "tables": cls.parse_tables(doc),
            "lists": cls.parse_lists(doc)
        }