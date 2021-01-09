CREATE TABLE messages (
    id serial primary key,
    message TEXT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
