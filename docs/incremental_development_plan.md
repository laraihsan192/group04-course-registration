# Group 04 — Incremental Development Plan

We’ll build the course registration website in three increments. First,
students will be able to sign in and find course sections. Next, they’ll
be able to register during the semester’s registration period if they
meet the enrollment rules. Finally, they’ll be able to view their semester
timetable and drop a section during the allowed drop period.

Each increment has two checkpoints. The `-design` tag marks the reviewed
design, and the matching working tag marks the features once they’ve been
implemented and tested. We’ll create each tag after the checkpoint has
been reviewed and merged through a pull request. We’ll keep the branches
after merging.

The requirement IDs come from the [requirements document](requirements.md).
The diagram, module, and test links point to planned paths and will work
once those files are added to the repository.

| Version | Type | Capability / Scope | Deliverable / Evidence | Requirements / Design Links |
| --- | --- | --- | --- | --- |
| `v0.1.0-design` | Design | Demo sign-in and course search | Sign-in and search flows, course and section data model | FR-01–02 · [Architecture](architecture.md), [Use cases](../uml/use_cases.md), [Data model](../uml/data_model.md) |
| `v0.1.0` | Working | Demo sign-in and course search | Sign-in and search demo, passing tests run by the coding agent | FR-01–02 · [Accounts](../src/accounts/), [Catalog](../src/catalog/), [Tests](../tests/test_auth_catalog.py) |
| `v0.2.0-design` | Design | Section registration and enrollment checks | Registration flow with success and rejection paths | FR-03–06, NFR-01 (enrollment access), NFR-02 · [Registration sequence](../uml/register_sequence.md) |
| `v0.2.0` | Working | Section registration and enrollment checks | Registration demo, passing enrollment and last-seat tests run by the coding agent | FR-03–06, NFR-01 (enrollment access), NFR-02 · [Enrollment](../src/enrollment/), [Tests](../tests/test_registration.py) |
| `v0.3.0-design` | Design | Drop a section and view the semester timetable | Drop flow and timetable design | FR-07–08, NFR-01 · [Drop sequence](../uml/drop_sequence.mmd), [Architecture](architecture.md) |
| `v0.3.0` | Working | Drop a section and view the semester timetable | Drop and timetable demo, passing tests run by the coding agent | FR-07–08, NFR-01 · [Enrollment](../src/enrollment/), [Timetable](../src/timetable/), [Tests](../tests/test_drop_timetable.py) |
| `v1.0.0` | Final release | Complete student registration workflow | End-to-end demo, passing tests, final diagrams, and `se_report_group_04.pdf` | All requirement IDs · [Traceability](traceability_matrix.md), [Testing](testing.md), [End-to-end tests](../tests/test_student_workflow.py) |

## v0.1.0-design — Sign-in and course search

- **Main question** — How does a student sign in, find a course, and compare its sections?
- **Tools** — Markdown and Mermaid.
- **Acceptance criteria** — The design shows how students sign in, search by course name or code, and see each section’s meeting times and remaining seats. The data model shows how each course is linked to its sections.

## v0.1.0 — Sign-in and course search

- **Main question** — Can a student use a demo account to find the section they want?
- **Tools** — Coding agent, browser, and automated tests.
- **Acceptance criteria** — A valid demo account can sign in, and a failed sign-in shows a clear message. Searching by name or code returns matching courses and shows their sections, meeting times, and remaining seats.

## v0.2.0-design — Section registration

- **Main question** — What happens when a student clicks Register?
- **Tools** — Markdown and Mermaid.
- **Acceptance criteria** — The design shows how the system identifies the signed-in student and checks the registration period, prerequisites, available seats, and timetable conflicts. It shows what the student sees when registration succeeds or fails and how the system prevents two students from taking the last seat.

## v0.2.0 — Section registration

- **Main question** — Can an eligible student register, and does the system explain why a request was rejected?
- **Tools** — Coding agent, browser, and automated tests.
- **Acceptance criteria** — A valid request saves the enrollment, confirms it, and reduces the available seat count by one. A closed registration period, missing prerequisite, full section, or timetable conflict shows a clear reason and leaves the enrollment and seat count unchanged. Back-to-back classes are allowed. Students can register only for their own accounts, and at most one student can claim the last seat.

## v0.3.0-design — Drop and timetable

- **Main question** — How does a student view their classes and drop a section if their plans change?
- **Tools** — Markdown and Mermaid.
- **Acceptance criteria** — The design shows how the timetable uses the signed-in student’s enrollments to list classes by day and time. The drop flow shows how the system checks whether the drop period is open and whether the student is still enrolled in the selected section.

## v0.3.0 — Drop and timetable

- **Main question** — Does dropping a section update the student’s timetable and free a seat?
- **Tools** — Coding agent, browser, and automated tests.
- **Acceptance criteria** — The timetable shows the student’s enrolled sections by day and time. A successful drop removes the section from the timetable and frees one seat. If the drop period is closed or the student is no longer enrolled in the section, the system explains why the request failed and leaves the timetable and seat count unchanged. Students can view only their own timetable and change only their own enrollments.

## v1.0.0 — Final integrated release

- **Main question** — Can a student complete the whole workflow from signing in to dropping a section?
- **Tools** — Browser, automated tests, GitHub, and the final PDF report.
- **Acceptance criteria** — The team can sign in as Leen, find a course, register during the registration period, see the section on her timetable, and drop it during the allowed drop period. The end-to-end tests pass, the setup instructions work, and the final diagrams, report, traceability matrix, and AI development log reflect the released system.
