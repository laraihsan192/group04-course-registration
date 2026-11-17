# Group 04 — University Course Registration System

## Project description

When students plan their classes for a new semester, finding the courses they
want is only part of the process. They also need to find a section that fits
their timetable, has a seat available, and meets their prerequisite
requirements. Our project brings these steps together in one website.

Students can search for a course by its name or code and compare its sections
by meeting time and available seats. When a student chooses a section and
clicks Register, the system checks whether they have completed the required
prerequisites, whether the section still has space, and whether any of its
meetings overlap with a class already on their schedule.

For example, a student might find an open section of Data Structures that
fits their timetable. If they have not passed Programming I, which is a
prerequisite in our demo, the system explains why they cannot register.
When registration succeeds, the section appears on their weekly schedule.
If they later drop it, the section is removed from their schedule and a
seat becomes available again.

## Project scope

The student is the main user. The website covers course search, section
selection, registration, dropping a section, and viewing a weekly schedule.
The demo follows the student through that process using sample course and
student records.

## Assumptions

- The demo covers one semester and uses fictional student and course records.
- Students register during the semester's registration period and can drop
  sections during the allowed drop period. The weekly timetable shows when
  their enrolled classes meet each week.
- Students sign in using demo accounts. Their completed courses are already
  recorded in the system.
- A course can have multiple sections with different meeting times and
  capacities. A student registers for a specific section.
- Students must have passed all listed prerequisites before they can register.
- Back-to-back classes are allowed. A timetable conflict occurs when two
  meetings overlap on the same day.
- The initial scope focuses on students. Registrar and instructor features
  are optional in the case study and are outside our current scope.
