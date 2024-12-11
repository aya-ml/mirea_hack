from docx import Document

class DocxParser:
    @classmethod
    def parse_docx(cls, file_path: str) -> list:
        doc = Document(file_path)
        result = []
        tables_iter = iter(doc.tables)
        current_list = []

        for paragraph in doc.paragraphs:
            style_name = paragraph.style.name.lower()
            text = paragraph.text.strip()

            if "list paragraph" in style_name:
                if text:
                    current_list.append(text)
                continue
            else:
                if current_list:
                    list_text = " ".join(current_list)
                    result.append({"type": "list", "text": list_text})
                    current_list = []

            if not text:
                continue

            result.append({"type": "paragraph", "text": text})

            try:
                if len(paragraph._element.xpath("./following-sibling::w:tbl")) > 0:
                    table = next(tables_iter)
                    table_data = []

                    for row in table.rows:
                        row_text = " | ".join([cell.text.strip() for cell in row.cells if cell.text.strip()])
                        table_data.append(row_text)

                    table_text = "\n".join(table_data)
                    result.append({"type": "table", "text": table_text})
            except StopIteration:
                pass

        if current_list:
            list_text = " ".join(current_list)
            result.append({"type": "list", "text": list_text})

        return result