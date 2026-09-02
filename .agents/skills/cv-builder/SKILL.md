---
name: cv-builder
description: >-
  Builds and compiles Andrés Pedraza Míguez's master CV and tailored CVs from Markdown into production HTML and PDF formats, automatically applying link transformations.
---

# CV Builder Skill (Markdown to HTML & PDF)

Use this skill whenever you or the user modify `CV_andres_pedraza_miguez.md` or create/update tailored CVs in `tailored/`.

## Purpose & Automated Rules

This skill automates the compilation of Markdown CVs into:
1. **HTML (`index.html`)**: For public web viewing on GitHub Pages.
   - **Link Rule**: Automatically transforms the **Online CV** list item into a **Download CV** link pointing to the PDF (`<a href="CV_andres_pedraza_miguez.pdf" download>Download PDF</a>`).
2. **PDF (`CV_andres_pedraza_miguez.pdf` or `tailored/*.pdf`)**: For offline distribution / job applications.
   - **Link Rule**: Preserves the **Online CV** link pointing to `https://pedrazamiguez.github.io`.

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
