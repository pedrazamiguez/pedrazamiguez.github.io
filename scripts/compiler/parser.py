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

    # 4. Enhance semantic header and contact grid
    def format_header_and_contact(match):
        h1_tag = match.group(1).strip()
        sub_text = match.group(2).strip()
        ul_content = match.group(3).strip()
        
        # Parse li elements into clean contact items
        items = re.findall(r'<li>\s*<strong>(.*?):?</strong>\s*(.*?)\s*</li>', ul_content, flags=re.DOTALL)
        
        action_btn_html = ""
        contact_items_html = []
        for label, val in items:
            clean_label = label.strip().rstrip(':')
            val_clean = val.strip()
            if "download" in clean_label.lower():
                action_btn_html = f'<div class="header-action">{val_clean}</div>'
            else:
                contact_items_html.append(
                    f'<div class="contact-item">'
                    f'<span class="contact-label">{clean_label}:</span> '
                    f'<span class="contact-value">{val_clean}</span>'
                    f'</div>'
                )
        
        grid_html = "\n      ".join(contact_items_html)
        action_row = f'\n    {action_btn_html}' if action_btn_html else ''
        
        return (
            f'<header class="cv-header">\n'
            f'  <div class="header-top">\n'
            f'    <div class="header-titles">\n'
            f'      {h1_tag}\n'
            f'      <p class="cv-subtitle">{sub_text}</p>\n'
            f'    </div>{action_row}\n'
            f'  </div>\n'
            f'  <div class="contact-card">\n'
            f'    <div class="contact-grid">\n'
            f'      {grid_html}\n'
            f'    </div>\n'
            f'  </div>\n'
            f'</header>'
        )

    html_body = re.sub(
        r'(<h1>.*?</h1>)\s*<p>(?:<em>)?(.*?)(?:</em>)?</p>\s*<h2>Contact Information</h2>\s*<ul>(.*?)</ul>',
        format_header_and_contact,
        html_body,
        flags=re.DOTALL | re.IGNORECASE
    )

    # 5. Format Tech Stack lines into modern badge containers with title TECH STACK (no colon)
    def format_tech_stack(match):
        stack_text = match.group(2).strip()
        # Clean potential trailing period or comma
        stack_text = re.sub(r'[\.,]$', '', stack_text)
        items = [item.strip() for item in stack_text.split(',') if item.strip()]
        pills_html = "".join(f'<span class="tech-pill">{item}</span>' for item in items)
        return (
            f'<div class="tech-stack-container">'
            f'<span class="tech-stack-label">TECH STACK</span>'
            f'<div class="tech-pills">{pills_html}</div>'
            f'</div>'
        )

    html_body = re.sub(
        r'<p><strong>(Tech Stack:?)</strong>\s*(.*?)</p>',
        format_tech_stack,
        html_body,
        flags=re.DOTALL
    )

    # 6. Format Main Project / Projects lines into project highlights
    html_body = re.sub(
        r'<p><strong>(Main Project:?|Projects:?)</strong>\s*(.*?)</p>',
        r'<div class="project-highlight"><span class="project-label">\1</span> <span class="project-desc">\2</span></div>',
        html_body,
        flags=re.DOTALL
    )

    return html_body, title

