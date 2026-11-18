# Group 04 — Registration Sequence Diagram

Leen is signed in and has selected a course section. This diagram shows
what happens after she clicks **Register**.

```mermaid
sequenceDiagram
    actor Leen as Leen (student)
    participant Page as Registration page
    participant Enrollment as Enrollment component
    participant DB as Database

    Leen->>Page: Click Register
    Page->>Enrollment: Request enrollment for the selected section
    Note over Enrollment: Use Leen's signed-in account
    Enrollment->>DB: Read registration period, prerequisites, seats, and timetable
    DB-->>Enrollment: Return section and student records
    Enrollment->>Enrollment: Check the period, prerequisites, seats, and conflicts

    alt A check fails
        Enrollment-->>Page: Return the reason registration failed
        Page-->>Leen: Show the reason
    else All checks pass
        Enrollment->>DB: Recheck seat availability and save enrollment in one transaction
        alt Enrollment saved
            DB-->>Enrollment: Confirm enrollment
            Enrollment-->>Page: Return confirmation
            Page-->>Leen: Show confirmation and the new section on her timetable
        else The last seat was taken
            DB-->>Enrollment: Report that the section is full
            Enrollment-->>Page: Return section-full message
            Page-->>Leen: Show that the section is full
        end
    end
```

If registration fails, nothing is added to Leen's timetable. The final seat
check and enrollment save happen together so two students can't both claim
the last seat.
