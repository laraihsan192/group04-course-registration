# Group 04 — University Course Registration System

## Scope and stakeholders

Our website helps students put together their class timetable for the semester.
Students can search for courses, compare sections, and register during the
semester's registration period. If their plans change, they can drop a section
during the allowed drop period. Their timetable shows when their enrolled
classes meet each week.

Students are the main users. The university registrar is also a stakeholder
because accurate enrollment records and seat counts matter to the registration
process. Our demo focuses on the student side and uses fictional student and
course records for one semester.

## Functional requirements

| ID | What the website should do |
| --- | --- |
| FR-01 | Let students sign in with a demo account. If sign-in fails, show a clear message. |
| FR-02 | Let students search by course name or code. For each matching course, show its sections, meeting times, and remaining seats. |
| FR-03 | Let students register for a section during the semester's registration period if all checks pass. Confirm the enrollment and update the remaining seat count. If registration is closed, tell the student. |
| FR-04 | Check whether the student has passed all required prerequisites. If any are missing, reject the request and tell the student which ones they still need. |
| FR-05 | If the section has no seats left, reject the request and tell the student the section is full. |
| FR-06 | If any of the section's meetings overlap with a class already on the student's timetable on the same day, reject the request and name the conflicting class. Back-to-back classes are allowed. |
| FR-07 | Let students drop a section they're enrolled in during the allowed drop period. Remove it from their timetable and free one seat. If the drop period is closed, tell the student. |
| FR-08 | Show the student's class timetable for the semester, with enrolled classes organized by day of the week and meeting time. |

## Non-functional requirements

| ID | What the system should guarantee |
| --- | --- |
| NFR-01 | Students can only view their own timetable and change their own enrollments. |
| NFR-02 | If two students try to register for the last seat at the same time, at most one gets the seat. |

## Use case — Register for a section

**Who** — A signed-in student.

**Goal** — Enroll in a section for the semester.

1. The student searches for a course, picks a section, and clicks **Register**.
2. The system checks whether the registration period is open.
3. The system checks the student's prerequisites, the section's remaining
   seats, and any conflicts with the student's timetable.
4. If all checks pass, the system saves the enrollment, confirms it, and shows
   the section on the student's timetable. The section now has one fewer seat.

**If registration fails** — The system explains why the request failed.
The student's timetable and the section's seat count stay the same.

**Example** — Leen finds a Data Structures section with an open seat that fits
her timetable. In our demo, Data Structures requires Programming I. If Leen
hasn't passed Programming I, the website tells her she needs to pass it before
she can register for Data Structures.

## Use case — Drop a section

**Who** — A signed-in student with a section on their timetable.

**Goal** — Drop a section they no longer want to take.

1. The student opens their timetable, selects a section, and clicks **Drop**.
2. The system checks whether the drop period is open and whether the student
   is still enrolled in the section.
3. If both checks pass, the system removes the enrollment, frees one seat,
   and shows the updated timetable.

**If the drop fails** — The system explains whether the drop period is closed
or the student is already out of the section. The timetable and seat count
stay the same.

**Example** — Leen decides to drop her Statistics section. Since the drop
period is open and she's still enrolled, Statistics disappears from her
timetable and one seat becomes available.
