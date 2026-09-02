# Andrés Pedraza Míguez — Online CV & Portfolio

Welcome! This repository hosts my online CV and professional web presence.

👉 **[View the Live CV / Website](https://pedrazamiguez.github.io)**

---

### Contact & Profiles
- **Role:** Senior Java & Kotlin Engineer | Remote Contractor Specialist
- **Website:** [https://pedrazamiguez.github.io](https://pedrazamiguez.github.io)
- **LinkedIn:** [pedrazamiguez](https://www.linkedin.com/in/pedrazamiguez/)
- **GitHub:** [pedrazamiguez](https://github.com/pedrazamiguez)
- **Email:** [pedraza.miguez@gmail.com](mailto:pedraza.miguez@gmail.com)

---

### Building HTML & PDF CVs
This repository uses a Python and Playwright build script to generate `index.html` and `CV_andres_pedraza_miguez.pdf`:

```bash
# Build master CV (index.html + CV_andres_pedraza_miguez.pdf)
python3 scripts/build_cv.py

# Build a tailored CV
python3 scripts/build_cv.py tailored/CV_Andres_Pedraza_<Company>_<Role>.md

# Build all CVs
python3 scripts/build_cv.py --all
```
