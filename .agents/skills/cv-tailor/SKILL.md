---
name: cv-tailor
description: >-
  Tailors and optimizes Andrés Pedraza Míguez's CV for a specific Job Description (JD)
  or target company. Use when the user shares a job posting or asks to adapt/customize their CV for a role.
---

# CV Tailoring Skill (JD Matching & Optimization)

Use this skill whenever Andrés provides a job description (JD) or asks to adapt his CV for a specific role or company.

## Goal
Produce a highly targeted, versioned Markdown CV in the `tailored/` directory that maximizes ATS compatibility, highlights relevant achievements, and resonates with hiring managers and technical interviewers—all while keeping `CV_andres_pedraza_miguez.md` intact as the central master version.

---

## Step-by-Step Procedure

### 1. Ingest & Analyze the Job Description (JD)
Extract key signals from the JD:
- **Core Stack**: Mandatory and nice-to-have technologies (e.g., Java 21, Spring Boot 3, Kotlin, Jetpack Compose, Kafka, AWS, Kubernetes).
- **Seniority & Role Scope**: Individual contributor, Tech Lead, Staff/Principal, Contractor, Fullstack.
- **Architectural & Methodological Themes**: Event-driven architecture, microservices vs monolith, legacy refactoring, mobile clean architecture, performance optimization, TDD/CI-CD.
- **ATS Keywords**: Specific terminology, library names, and domain phrases.

### 2. Formulate Strategy & Review with Andrés
Briefly identify the key angle for this application:
- **Backend / Distributed Systems Lead**: Focus on Java 21, Spring Boot 3, Kafka, Avro, High throughput, Microservices, Cloud.
- **Mobile / Android Lead / Specialist**: Focus on Kotlin, Jetpack Compose, clean architecture, refactoring legacy mobile apps, cross-functional bridge.
- **Fullstack / Contractor Specialist**: Emphasize hybrid versatility, fast onboarding into complex environments, self-management, UK remote contracting track record.

### 3. Generate the Tailored CV File
Create a new file in the `tailored/` folder:
`tailored/CV_Andres_Pedraza_<Company>_<Role>.md` (e.g., `tailored/CV_Andres_Pedraza_Revolut_Senior_Backend_Engineer.md`).

#### Content Customization Guidelines:
1. **Title & Headline**:
   - Align subtitle to match target role title closely (e.g., `*Senior Java / Kotlin Backend Engineer | Remote Specialist*` or `*Lead Android Engineer (Kotlin & Jetpack Compose)*`).
2. **Contact Section**:
   - Keep standard contact links (Email, LinkedIn, GitHub, Phone).
   - Ensure the **Online CV** link points to `https://pedrazamiguez.github.io`:
     `- **Online CV:** [Andrés Pedraza Míguez](https://pedrazamiguez.github.io)`
3. **Professional Summary**:
   - Rewrite the 2-paragraph summary to directly mirror the top 3-4 priorities from the JD.
4. **Work Experience Bullet Points**:
   - Reorder and emphasize bullet points under Plexus Tech (Inditex), Brandworkz, and Locassa that demonstrate direct experience with the target stack and challenges.
   - Spotlight relevant keywords (e.g., bolding specific technologies matching the JD).
5. **Factual Integrity (STRICT)**:
   - Do NOT invent companies, dates, or non-existent roles. Every claim must remain true to Andrés's actual background.

### 4. Build & Export the Tailored PDF
Run the automated build tool to generate the tailored PDF:
```bash
python3 scripts/build_cv.py tailored/CV_Andres_Pedraza_<Company>_<Role>.md
```
This automatically compiles the PDF to `tailored/CV_Andres_Pedraza_<Company>_<Role>.pdf` while keeping the online portfolio link pointing back to `https://pedrazamiguez.github.io`.
