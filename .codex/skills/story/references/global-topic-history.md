# Global Topic History

Apply this protocol across every story, scan, explainer, title, and hot-topic
skill. The project-wide source of truth is:

```text
选题历史/global-topic-history.jsonl
```

When SGGOI Studio is running and logged in, the same check also performs an
atomic company-wide reservation through the existing SGGOI Go service. The
project JSONL remains the detailed local history; the server prevents two
employees from claiming the same fingerprint at the same time. If the desktop
or network is unavailable, reserve provisionally in the local SQLite outbox,
warn the operator, and reconcile on the next online check.

Before showing any topic, premise, angle, title batch, hotspot, or evergreen
candidate:

1. Import existing domain ledgers and summarize the global history.
2. Compare the real semantic engine, event, mechanism, conflict, and payoff;
   changing only names, genre, country, role, or surface object does not make a
   topic new.
3. Run `check` with specific semantic tags. Any prior status (`presented`,
   `selected`, `generated`, or `rejected`) is burned by default.
4. Add every candidate as `presented` before displaying it. Unselected and
   rejected candidates must not return in later sessions.
5. After the user selects or generates a topic, add the corresponding status.

Only reuse a blocked topic when the user explicitly asks to revisit, remake,
continue, or compare it. Do not silently recycle a hotspot across domains; a
news event already used for an isekai premise is also burned for explainers,
female fantasy, silver literature, and general web fiction.

```powershell
python "$HOME/.codex/skills/story/scripts/topic_history.py" --root . import-existing
python "$HOME/.codex/skills/story/scripts/topic_history.py" --root . summary
python "$HOME/.codex/skills/story/scripts/topic_history.py" --root . check --seed "{seed}" --tags "{semantic,tags}"
python "$HOME/.codex/skills/story/scripts/topic_history.py" --root . add --domain "{domain}" --source "{source}" --seed "{seed}" --tags "{tags}" --status presented
python "$HOME/.codex/skills/story/scripts/topic_history.py" --root . sync-company
```

If no writable project root exists, keep a turn-local burned list and tell the
user that cross-session deduplication requires a project ledger.
