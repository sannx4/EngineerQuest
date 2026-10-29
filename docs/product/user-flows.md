# User journeys

Open prototype.html locally in a browser. It is a clickable low-fidelity journey prototype;
no real authentication, payments, deletion or persistence is performed.

| Journey         | Entry → exit                         | Loading / failure / offline recovery                          | Accessibility                       | Event                  |
| --------------- | ------------------------------------ | ------------------------------------------------------------- | ----------------------------------- | ---------------------- |
| Signup          | Welcome → class                      | Disable repeated submit; generic server error; retry online   | Named fields, focus error summary   | signup_submitted       |
| Class           | Signup/dashboard → lesson            | Empty choices explanation; preserve choice on retry           | Radio group and keyboard navigation | class_selected         |
| First lesson    | Class/dashboard → feedback           | Skeleton; content unavailable retry; cached read only offline | Heading and answer labels           | lesson_started         |
| Failure/retry   | Answer → feedback → same lesson      | Keep answer on timeout; retry uses request ID                 | Announce feedback, focus heading    | attempt_failed         |
| Completion      | Correct answer → dashboard           | Pending sync shown; server deduplicates                       | Text completion status              | lesson_completed       |
| Streak recovery | Dashboard → practice                 | Show timezone; outage cannot silently erase earned streak     | Avoid color-only state              | streak_recovery_opened |
| Subscription    | Dashboard → checkout → dashboard     | No entitlement until verified; cancel safely; offline blocked | Price and renewal text announced    | checkout_opened        |
| Deletion        | Settings → confirmation → signed out | Reauthenticate; pending request visible; offline blocked      | Destructive confirmation and cancel | deletion_requested     |

Cognitive desk walkthrough: all listed screens have exits and recovery paths; this is an
internal specification review, not a completed human usability study. Subscription and
streak are future journeys and not v0.1 implementation commitments. Events are schema
names only; no analytics is transmitted by prototype. No email, answers or tokens in events.
