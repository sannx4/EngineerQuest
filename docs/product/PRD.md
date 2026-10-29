# Product requirements — v0.1-foundation

Owner: repository maintainer. Status: proposed; user research pending.

## Personas and jobs

Primary: early-career engineer who can code but struggles to practice operational skills.
Job: complete a short, realistic exercise and understand why an answer failed.
Secondary: career-switching learner needing structured prerequisites and progress.
These are hypotheses, not interview findings.

## First learning loop

Choose engineer class → open first Git lesson → attempt → actionable feedback → retry
→ persist completion → show progress. North-star candidate: weekly learners completing
three distinct lessons with at least one successful retry. Count distinct learner IDs;
exclude staff/test users and count each lesson once per week.

## MVP acceptance stories

| Story                | Measurable acceptance                                             | Owner       |
| -------------------- | ----------------------------------------------------------------- | ----------- |
| Register and sign in | Verified user reaches own dashboard; another user cannot read it  | Identity    |
| Choose class         | Selection persists across restart and is visible on dashboard     | Profile     |
| Attempt first lesson | Valid answer yields deterministic feedback and one completion     | Learning    |
| Retry failure        | Feedback explains mistake; retry does not double-award completion | Learning    |
| Resume               | Restart preserves server-confirmed progress                       | Progression |
| Delete account       | Access revoked immediately; deletion finishes within 30 days      | Identity    |

Non-goals for v0.1: subscriptions, arbitrary code execution, AI tutor, social feeds,
leaderboards, app-store release and all nine complete learning worlds.

## Guardrails

No raw learner code in analytics; no secrets in logs. Track lesson error rate, feedback
latency, completion rate and deletion completion. Targets are in quality requirements;
no baseline or retention improvement is claimed before measurement.

## Release map

1 foundation/auth/profile; 2 gamification; 3 learning core; 4 Git; 5 Linux; 6 SQL;
7 DSA; 8 debugging; 9 networking/security; 10 cloud/DevOps; 11 mentor; 12 launch.
Each release requires tests, an operational rollback and documented evidence.

## Acceptance review

All six MVP stories support entering, completing or trusting the first learning loop.
Payment, AI and rankings are deferred because they are not prerequisites for this loop.
Decision log records scope changes; risks live in risk-register.md.
