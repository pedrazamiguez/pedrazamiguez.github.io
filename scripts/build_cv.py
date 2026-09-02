#!/usr/bin/env python3
"""
CV Build Tool: Compiles Markdown CVs into production HTML and PDF formats.

Usage:
  python3 scripts/build_cv.py                     # Compiles master CV (index.html + CV_andres_pedraza_miguez.pdf)
  python3 scripts/build_cv.py <path/to/cv.md>     # Compiles specific CV file
  python3 scripts/build_cv.py --all               # Compiles master CV and all tailored CVs
  python3 scripts/build_cv.py --html-only         # Only generates HTML
  python3 scripts/build_cv.py --pdf-only          # Only generates PDF
"""

import os
import sys
import glob
import argparse

# Auto re-execute with local .venv python if available and current python lacks dependencies
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
VENV_PYTHON = os.path.join(PROJECT_ROOT, ".venv", "bin", "python")

if os.path.isfile(VENV_PYTHON) and os.path.abspath(sys.executable) != os.path.abspath(VENV_PYTHON):
    try:
        import markdown
        import playwright
    except ImportError:
        os.execv(VENV_PYTHON, [VENV_PYTHON] + sys.argv)

# Add parent directory of scripts to Python path so compiler can be imported
sys.path.insert(0, os.path.dirname(__file__))

from compiler.parser import parse_markdown_to_html
from compiler.template import generate_html_document
from compiler.renderer import render_pdf

MASTER_MD = os.path.join(PROJECT_ROOT, "CV_andres_pedraza_miguez.md")
MASTER_HTML = os.path.join(PROJECT_ROOT, "index.html")
MASTER_PDF = os.path.join(PROJECT_ROOT, "CV_andres_pedraza_miguez.pdf")
CSS_PATH = os.path.join(PROJECT_ROOT, "markdown-pdf.css")

def build_single_cv(md_path: str, html_only: bool = False, pdf_only: bool = False):
    """Builds a single CV markdown file into HTML and/or PDF."""
    if not os.path.isfile(md_path):
        print(f"Error: Markdown file not found: {md_path}")
        return False

    is_master = os.path.abspath(md_path) == os.path.abspath(MASTER_MD)
    
    if is_master:
        output_html = MASTER_HTML
        output_pdf = MASTER_PDF
        pdf_rel_name = os.path.basename(MASTER_PDF)
    else:
        base_name = os.path.splitext(md_path)[0]
        output_html = base_name + ".html"
        output_pdf = base_name + ".pdf"
        pdf_rel_name = os.path.basename(output_pdf)

    with open(md_path, "r", encoding="utf-8") as f:
        md_text = f.read()

    print(f"\nProcessing: {os.path.relpath(md_path, PROJECT_ROOT)}")

    # 1. Generate HTML if requested
    if not pdf_only:
        # In HTML mode, replace Online CV link with Download PDF link
        html_body, title = parse_markdown_to_html(md_text, target_mode="html", pdf_filename=pdf_rel_name)
        full_html = generate_html_document(html_body, title, css_path=CSS_PATH)
        with open(output_html, "w", encoding="utf-8") as f:
            f.write(full_html)
        print(f"  ✓ HTML generated: {os.path.relpath(output_html, PROJECT_ROOT)}")

    # 2. Generate PDF if requested
    if not html_only:
        # In PDF mode, keep the Online CV link
        pdf_html_body, title = parse_markdown_to_html(md_text, target_mode="pdf", pdf_filename=pdf_rel_name)
        pdf_doc_html = generate_html_document(pdf_html_body, title, css_path=CSS_PATH)
        render_pdf(pdf_doc_html, output_pdf)
        print(f"  ✓ PDF generated:  {os.path.relpath(output_pdf, PROJECT_ROOT)}")

    return True

def main():
    parser = argparse.ArgumentParser(description="Compile CV Markdown files to HTML and PDF.")
    parser.add_argument("file", nargs="?", default=None, help="Specific markdown file to compile (default: master CV)")
    parser.add_argument("--all", action="store_true", help="Compile master CV and all files in tailored/")
    parser.add_argument("--html-only", action="store_true", help="Generate only HTML output")
    parser.add_argument("--pdf-only", action="store_true", help="Generate only PDF output")

    args = parser.parse_args()

    if args.all:
        # Compile Master CV
        build_single_cv(MASTER_MD, html_only=args.html_only, pdf_only=args.pdf_only)
        
        # Compile all files in tailored/ (excluding README.md)
        tailored_files = [
            f for f in glob.glob(os.path.join(PROJECT_ROOT, "tailored", "*.md"))
            if not os.path.basename(f).lower().startswith("readme")
        ]
        for tf in sorted(tailored_files):
            build_single_cv(tf, html_only=args.html_only, pdf_only=args.pdf_only)
            
        print("\nAll CVs successfully compiled! 🎉")
    elif args.file:
        target_file = os.path.abspath(args.file)
        success = build_single_cv(target_file, html_only=args.html_only, pdf_only=args.pdf_only)
        if not success:
            sys.exit(1)
        print("\nCompilation completed! 🎉")
    else:
        # Default: compile master CV
        success = build_single_cv(MASTER_MD, html_only=args.html_only, pdf_only=args.pdf_only)
        if not success:
            sys.exit(1)
        print("\nMaster CV successfully compiled! 🎉")

if __name__ == "__main__":
    main()
