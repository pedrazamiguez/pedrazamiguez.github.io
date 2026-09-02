---
name: cv-builder
description: >-
  Builds and compiles Andrés Pedraza Míguez's master CV and tailored CVs from Markdown into production HTML and PDF formats, automatically applying link transformations.
---

# CV Builder Skill (Markdown to HTML & PDF)

Use this skill whenever you or the user modify `CV_andres_pedraza_miguez.md` or create/update tailored CVs in `tailored/`.

## Purpose & Automated Rules

This skill automates the compilation of Markdown CVs into:
1. **Master CV**:
   - **HTML (`index.html`)**: For public web viewing on GitHub Pages. Transforms the **Online CV** list item into a **Download CV** link pointing to `CV_andres_pedraza_miguez.pdf`.
   - **PDF (`CV_andres_pedraza_miguez.pdf`)**: For offline distribution. The **Online CV** link points to `https://pedrazamiguez.github.io`.
2. **Tailored CVs (`tailored/`)**:
   - **HTML (`tailored/*.html`)**: Generates an online mirror on GitHub Pages with a **Download PDF** link pointing to that specific tailored PDF.
   - **PDF (`tailored/*.pdf`)**: For offline submission to companies/recruiters. The **Online CV** link points directly to its corresponding tailored web URL (`https://pedrazamiguez.github.io/tailored/<Filename>.html`).

---

## Build Commands

### 1. Compile Master CV (Default)
Compiles `CV_andres_pedraza_miguez.md` into `index.html` and `CV_andres_pedraza_miguez.pdf`:
```bash
python3 scripts/build_cv.py
```

### 2. Compile a Specific Tailored CV
Compiles a specific tailored CV (e.g. for a company application):
```bash
python3 scripts/build_cv.py tailored/CV_Andres_Pedraza_Revolut_Senior_Backend_Engineer.md
```

### 3. Compile All CVs
Compiles the master CV and every tailored CV in the `tailored/` folder:
```bash
python3 scripts/build_cv.py --all
```

### 4. Build Flags
- `--html-only`: Only generate the HTML file.
- `--pdf-only`: Only generate the PDF file.

---

## Setup & Dependencies

The compiler relies on Python with `markdown` and `playwright` (installed in `.venv/`):
```bash
# If setting up in a fresh clone:
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
```
*(The `scripts/build_cv.py` script automatically re-executes using `.venv/bin/python` if `.venv` is present).*

---

## Verification Checklist

After running the build tool:
- [ ] Ensure `index.html` was generated and contains the `Download CV` link with the `download` attribute.
- [ ] Ensure `CV_andres_pedraza_miguez.pdf` was generated with current timestamp.
- [ ] If building tailored CVs, ensure the tailored PDF is created in `tailored/`.
