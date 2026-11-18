# Group 04 — Use Case Diagram

The student is the main user of the University Course Registration System.
The diagram shows the actions students can take during the demo semester.

```mermaid
flowchart LR
    Student["Student"]
    subgraph System["University Course Registration System"]
        direction TB
        SignIn(["Sign in"])
        Search(["Search courses and view sections"])
        Register(["Register for a section"])
        Drop(["Drop a section"])
        Timetable(["View semester timetable"])
    end
    Student --- SignIn
    Student --- Search
    Student --- Register
    Student --- Drop
    Student --- Timetable
```

Registration and dropping are available during their respective periods.
When a student registers, the system also checks prerequisites, available
seats, and timetable conflicts.
