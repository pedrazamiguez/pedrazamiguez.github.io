# Tailored CVs

This directory stores customized, role-specific versions of Andrés Pedraza Míguez's CV tailored for specific job descriptions and target companies.

## Naming Convention
`CV_Andres_Pedraza_<Company>_<Role>.md`

Example:
`CV_Andres_Pedraza_Acme_Senior_Backend_Engineer.md`

## Notes
- The master version remains `../CV_andres_pedraza_miguez.md`.
- Tailored Markdown CVs are compiled to both HTML and PDF using `python3 scripts/build_cv.py tailored/<CV_file>.md`.
- In PDFs generated from tailored CVs, the **Online CV** link points directly to its corresponding tailored web version on GitHub Pages: `https://pedrazamiguez.github.io/tailored/<CV_file>.html`.
- In HTML files generated in `tailored/`, the top action button allows recruiters to download that specific tailored PDF directly.
