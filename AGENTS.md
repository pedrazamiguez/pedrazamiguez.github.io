# Project Instructions & Agent Guidelines

## 1. Project Overview & Architecture
This repository contains the online CV and professional web presence for **Andrés Pedraza Míguez**, publicly hosted on GitHub and served via **GitHub Pages** at:
👉 **[https://pedrazamiguez.github.io](https://pedrazamiguez.github.io)**

### Key Files & Roles
- **`CV_andres_pedraza_miguez.md`**: The **master source of truth** for Andrés's standard/core CV. All general updates to work history, skills, contact info, and summary must be made here.
- **`scripts/build_cv.py`**: The automated Python build script that compiles Markdown into HTML (`index.html`) and PDF (`CV_andres_pedraza_miguez.pdf`) using Playwright Chromium.
- **`markdown-pdf.css`**: The unified stylesheet formatting both HTML and PDF outputs cleanly and consistently.
- **`index.html`**: The public entry point for GitHub Pages, generated automatically with the **Download PDF** link.
- **`CV_andres_pedraza_miguez.pdf`**: The downloadable PDF version of the master CV, generated automatically with the **Online CV** link.
- **`tailored/`**: Directory for company- or role-specific tailored CV variants (e.g., `CV_Andres_Pedraza_<Company>_<Role>.md`).

---

## 2. The Core Conversion & Automated Linking Rule (CRITICAL)

When parsing `CV_andres_pedraza_miguez.md` to HTML and PDF, there is a fundamental difference in how links must behave:

### Why the links differ
1. **In Markdown & PDF (`CV_andres_pedraza_miguez.pdf`)**:
   - The reader has an offline/static document.
   - It **MUST** link to the live online CV:
     ```markdown
     - **Online CV:** [Andrés Pedraza Míguez](https://pedrazamiguez.github.io)
     ```
2. **In HTML (`index.html`)**:
   - The visitor is already viewing the online CV. A self-reference is redundant.
   - It **MUST** offer a download link to the PDF:
     ```html
     <li><strong>Download CV:</strong> <a href="CV_andres_pedraza_miguez.pdf" download>Download PDF</a></li>
     ```

### Automated Build Procedure
All conversions and link adjustments are handled automatically by `scripts/build_cv.py`:
- **Build Master CV**: `python3 scripts/build_cv.py` (generates `index.html` and `CV_andres_pedraza_miguez.pdf`).
- **Build Specific Tailored CV**: `python3 scripts/build_cv.py tailored/CV_Andres_Pedraza_<Company>_<Role>.md`.
- **Build All CVs**: `python3 scripts/build_cv.py --all`.

---

## 3. Mandatory Agent Protocol

Whenever any AI agent suggests, edits, or applies changes to `CV_andres_pedraza_miguez.md` or any CV content:
- **Automatically run the build tool or remind the user**:
  ```bash
  python3 scripts/build_cv.py
  ```
  *(This automatically produces the updated `index.html` and `CV_andres_pedraza_miguez.pdf` with properly formatted links).*

---

## 4. Tailored CV Generation Workflow (Job Description Matching)

When the user provides a **Job Description (JD)** or asks to prepare an application for a specific role:

### 1. Golden Rule: Keep Master CV Centered
- **NEVER** overwrite the master `CV_andres_pedraza_miguez.md` with a job-specific version.
- Always create a new file under `tailored/` named:
  `tailored/CV_Andres_Pedraza_<Company>_<Role>.md` (e.g., `tailored/CV_Andres_Pedraza_Revolut_Senior_Backend_Engineer.md`).

### 2. Tailoring Strategy
When analyzing a JD:
1. **Analyze Requirements & Tone**:
   - Extract required & preferred technical stack (e.g. Java 21, Spring Boot, Kafka, Kotlin, Compose, AWS/Azure, Kubernetes).
   - Identify core themes (e.g., High-throughput Distributed Systems, Architecture Refactoring, Mobile Tech Leadership, Legacy Modernization, FinTech/E-commerce domain).
   - Identify ATS (Applicant Tracking System) keywords and phrasing.
2. **Align Professional Summary**:
   - Tailor the opening summary to directly address the role's priorities (e.g., spotlighting backend scale vs fullstack/mobile leadership vs contractor availability in UK/EU timezones).
3. **Curate & Reorder Experience Bullet Points**:
   - Highlight achievements directly answering the JD requirements.
   - Emphasize relevant metrics and architectural decisions (e.g., Kafka event streaming, Hexagonal architecture, API-first OpenAPI/AsyncAPI, Android Compose migration).
4. **Maintain Factual Integrity**:
   - Never invent roles, dates, or non-existent experience. Reframe and emphasize genuine expertise and achievements.
5. **Link Strategy for Tailored CVs**:
   - If the tailored CV is exported to PDF for submission, ensure its contact section includes the link to Andrés's main online portfolio:
     `- **Online CV:** [Andrés Pedraza Míguez](https://pedrazamiguez.github.io)`
     `- **LinkedIn:** [pedrazamiguez](https://www.linkedin.com/in/pedrazamiguez/)`
     `- **GitHub:** [pedrazamiguez](https://github.com/pedrazamiguez)`

---

## 5. Andrés's Core Profile & Strengths Summary
- **Title**: Senior Java & Kotlin Engineer | Remote Contractor Specialist
- **Experience**: 14+ years in software engineering.
- **Core Specialties**:
  - **Backend**: Java (up to Java 21), Spring Boot (2 & 3), Spring Cloud, Microservices, Hexagonal Architecture, REST, OpenAPI, AsyncAPI, Kafka, Avro.
  - **Mobile / Hybrid**: Kotlin, Android Native, Jetpack Compose, Clean Architecture, Mobile App Rescue & Refactoring.
  - **Databases & Search**: PostgreSQL, MongoDB, Redis, Elasticsearch & Kibana.
  - **Cloud & DevOps**: AWS (EC2, S3, RDS), Azure, Docker, Jenkins, CI/CD, Bash scripting.
  - **Ways of Working**: Remote contractor for UK & global enterprises (Inditex/Zara, Brandworkz, Locassa), English fluency, software craftsmanship, mentorship, TDD/automated testing.
