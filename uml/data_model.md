# Group 04 — Course and Section Data Model

A course, such as Data Structures, can have several sections. Each
section has its own capacity and meeting times. Students search by
course name or code, then compare the sections.

```mermaid
erDiagram
    COURSE ||--o{ SECTION : has
    SECTION ||--|{ MEETING_TIME : meets_at

    COURSE {
        string course_code PK
        string name
    }

    SECTION {
        int section_id PK
        string course_code FK
        string section_number
        int capacity
    }

    MEETING_TIME {
        int meeting_id PK
        int section_id FK
        string day_of_week
        time start_time
        time end_time
    }
```

For the first demo, the catalog can show available seats using sample
enrollment counts. Once registration is implemented, available seats
will be the section's capacity minus its active enrollments.
