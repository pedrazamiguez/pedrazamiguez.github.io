import os

def generate_html_document(html_body: str, title: str, css_path: str = None) -> str:
    """
    Wraps HTML body into a complete, standalone HTML5 document with inline CSS styling.
    
    Args:
        html_body: Rendered HTML body content.
        title: Document title for the <title> tag.
        css_path: Path to markdown-pdf.css. If None, resolves relative to script root.
        
    Returns:
        Full HTML document string.
    """
    if css_path is None:
        base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
        css_path = os.path.join(base_dir, "markdown-pdf.css")

    css_content = ""
    if os.path.isfile(css_path):
        with open(css_path, "r", encoding="utf-8") as f:
            css_content = f.read()
    else:
        print(f"Warning: CSS file not found at {css_path}")

    doc_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
{css_content}
    </style>
</head>
<body>
{html_body}
</body>
</html>"""
    return doc_html
