import re
import markdown

def parse_markdown_to_html(md_text: str, target_mode: str = "pdf", pdf_filename: str = "CV_andres_pedraza_miguez.pdf") -> tuple[str, str]:
    """
    Parses CV markdown to HTML body and extracts document title.
    
    Args:
        md_text: Raw markdown content.
        target_mode: 'pdf' or 'html'.
        pdf_filename: The target PDF filename to link to when in 'html' mode.
        
    Returns:
        tuple of (html_body, title)
    """
    # 1. Extract document title (from first # Heading)
    title = "Andrés Pedraza Míguez - CV"
    match_title = re.search(r'^#\s+(.+)$', md_text, flags=re.MULTILINE)
    if match_title:
        title = match_title.group(1).strip()

    # 2. Transform links based on target mode
    processed_md = md_text
    if target_mode == "html":
        # In HTML mode (web browser), visitors are already on the site.
        # Replace the Online CV link with a Download PDF link with the download attribute.
        # Pattern matches: - **Online CV:** [Name](url)
        processed_md = re.sub(
            r'[-*]\s+\*\*Online CV:\*\*\s+\[.*?\]\(.*?\)',
            rf'- **Download CV:** <a href="{pdf_filename}" download>Download PDF</a>',
            processed_md,
            flags=re.IGNORECASE
        )

    # 3. Parse markdown into HTML
    extensions = [
        "extra",          # tables, attr_list, def_list, fenced_code, etc.
        "codehilite",     # syntax highlighting
        "sane_lists",     # sane list behavior
        "smarty",         # smart quotes and dashes
    ]
    extension_configs = {
        "codehilite": {
            "guess_lang": False,
            "noclasses": False,
        }
    }

    html_body = markdown.markdown(
        processed_md,
        extensions=extensions,
        extension_configs=extension_configs
    )

    return html_body, title
