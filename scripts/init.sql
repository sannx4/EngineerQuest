-- Local infrastructure seed only; product migrations begin in roadmap Day 9.
CREATE TABLE IF NOT EXISTS platform_metadata (
    key text PRIMARY KEY,
    value text NOT NULL
);
INSERT INTO platform_metadata (key, value) VALUES ('schema_version', 'local-1')
ON CONFLICT (key) DO UPDATE SET value = EXCLUDED.value;
