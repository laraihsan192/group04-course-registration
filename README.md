# University Course Registration System

**Group 04 · Section 2**  
**Course** — Software Engineering (CS13477), PSUT  
**Instructor** — Dr. Samer El Kababji

## Team members

- Lara Ihssan Toma 20230811
- Leen Munther Hasan 20230333
- Leen Tawfiq Hosary 20230622
- Leen Wael Albitar 20230147

## Project overview

We’re building a web app that helps students plan their semester timetable. Students will be able to search for courses by name or code, compare sections, and register during the semester’s registration period. Before confirming enrollment, the app will check prerequisites, seat availability, and timetable conflicts.

In the final demo, a student will sign in, find a section, register for it, and see it on their timetable. They’ll also be able to drop the section during the allowed drop period. The demo will use fictional student and course records for one semester.

## Tools

We use GitHub for version control, Markdown for documentation, and Mermaid for diagrams. We plan to use a coding agent for implementation and testing.

## Architecture and diagrams

- [System architecture](docs/architecture.md) — C4 context and container views, plus the main application components.
- [Use case diagram](uml/use_cases.md) — What a student can do in the app.
- [Registration sequence diagram](uml/register_sequence.md) — What happens after a student requests a seat.
- [Course and section data model](uml/data_model.md) — How courses, sections, and meeting times are related.

## Repository structure

- `docs/` contains the [project description](docs/project_description.md), [requirements](docs/requirements.md), [incremental plan](docs/incremental_development_plan.md), architecture, traceability matrix, and AI development log.
- `uml/` contains the editable project diagrams.

## Incremental development

- [v0.1.0-design](https://github.com/laraihsan192/group04-course-registration/releases/tag/v0.1.0-design) — Reviewed design for demo sign-in and course search.
- `v0.1.0` — Planned working version of demo sign-in and course search.
