import os
import tempfile
from playwright.sync_api import sync_playwright

def render_pdf(doc_html: str, output_pdf_path: str):
    """
    Renders the provided HTML document to a PDF file using Playwright Chromium.
    
    Args:
        doc_html: Complete HTML document string.
        output_pdf_path: Path where the output PDF should be saved.
    """
    os.makedirs(os.path.dirname(os.path.abspath(output_pdf_path)), exist_ok=True)
    
    with tempfile.NamedTemporaryFile('w', suffix='.html', encoding='utf-8', delete=False) as f:
        temp_html_path = f.name
        f.write(doc_html)
        
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.goto(f"file://{os.path.abspath(temp_html_path)}", wait_until="networkidle")
            
            # Wait for fonts to load if available
            try:
                page.evaluate("() => document.fonts.ready")
            except Exception:
                pass
                
            page.pdf(
                path=output_pdf_path,
                format="A4",
                prefer_css_page_size=True,
                print_background=True
            )
            browser.close()
    finally:
        if os.path.exists(temp_html_path):
            os.remove(temp_html_path)
