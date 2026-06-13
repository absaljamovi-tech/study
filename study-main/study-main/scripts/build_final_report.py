from fpdf import FPDF

INPUT = "FINAL_REPORT.md"
OUTPUT = "FINAL_REPORT.pdf"

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "Final Report: AI-Native Study Entry Submission", 0, 1, "C")
        self.ln(4)

    def chapter_title(self, label: str) -> None:
        self.set_font("Arial", "B", 14)
        self.multi_cell(0, 8, label)
        self.ln(2)

    def chapter_body(self, text: str) -> None:
        self.set_font("Arial", "", 11)
        self.multi_cell(0, 6, text)
        self.ln(2)


def render_markdown_line(pdf: PDF, line: str) -> None:
    stripped = line.strip()
    if not stripped:
        pdf.ln(2)
        return
    if stripped.startswith("# "):
        pdf.chapter_title(stripped[2:])
    elif stripped.startswith("## "):
        pdf.chapter_title(stripped[3:])
    elif stripped.startswith("### "):
        pdf.set_font("Arial", "B", 12)
        pdf.multi_cell(0, 7, stripped[4:])
        pdf.ln(1)
    elif stripped.startswith("- "):
        pdf.set_font("Arial", "", 11)
        pdf.multi_cell(0, 6, f"- {stripped[2:]}")
    else:
        pdf.chapter_body(stripped)


def build_pdf() -> None:
    pdf = PDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    with open(INPUT, "r", encoding="utf-8") as f:
        for line in f:
            render_markdown_line(pdf, line)

    pdf.output(OUTPUT)


if __name__ == "__main__":
    build_pdf()
