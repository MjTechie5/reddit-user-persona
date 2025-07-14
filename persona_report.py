from fpdf import FPDF
import os
import re

class PersonaPDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 16)
        self.cell(0, 10, "Reddit User Persona", ln=True, align="C")

    def chapter_title(self, title):
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, title, ln=True)
        self.ln(2)

    def chapter_body(self, body):
        self.set_font("Arial", "", 12)
        safe_text = remove_non_latin1(body)
        self.multi_cell(0, 8, safe_text)
        self.ln()

def remove_non_latin1(text):
    return text.encode("latin-1", errors="ignore").decode("latin-1")

def save_persona_as_pdf(username, persona_text):
    pdf = PersonaPDF()
    pdf.add_page()

    pdf.chapter_title(f"Username: u/{username}")
    pdf.chapter_body(persona_text)

    output_path = os.path.join("output", f"{username}_persona.pdf")
    os.makedirs("output", exist_ok=True)
    pdf.output(output_path)
    print(f" Persona saved at {output_path}")