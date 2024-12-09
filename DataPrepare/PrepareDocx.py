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
                    result.append({"type": "list", "text": current_list})
                    current_list = []

            if not text:
                continue

            result.append({"type": "paragraph", "text": text})

            try:
                if len(paragraph._element.xpath("./following-sibling::w:tbl")) > 0:
                    table = next(tables_iter)
                    table_data = [
                        [[cell.text.strip() for cell in row.cells] for row in table.rows]
                    ]
                    result.append({"type": "table", "text": table_data})
            except StopIteration:
                pass

        if current_list:
            result.append({"type": "list", "text": current_list})

        return result