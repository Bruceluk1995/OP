# Global Topic History

This is a mandatory company-wide gate for every story, scan, explainer, title,
hot-topic, evergreen-topic, premise, and episode-angle workflow. It applies to
interactive work, user-delegated automatic selection, and unattended SGGOI
automation. Project-local recent history is useful context, but it never
replaces the online company reservation.

The project-wide detailed source of truth is:

```text
选题历史/global-topic-history.jsonl
```

When SGGOI Studio is running and logged in, the same check also performs an
atomic company-wide reservation through the existing SGGOI Go service. The
project JSONL remains the detailed local history; the server prevents two
employees from claiming the same fingerprint at the same time. If the desktop
or network is unavailable, the local SQLite outbox may retain the attempted
reservation for later reconciliation, but it does not authorize presenting or
generating that topic. This gate fails closed until online confirmation exists.

Before showing, selecting, or generating any topic, premise, episode angle,
title batch, hotspot, or evergreen candidate:

1. Import existing domain ledgers and summarize the global history.
2. Compare the real semantic engine, event, mechanism, conflict, and payoff;
   changing only names, genre, country, role, or surface object does not make a
   topic new.
3. Build one stable semantic fingerprint in this exact key order:
   `role=...|engine=...|pressure=...|payoff=...|venue=...|aftertaste=...`.
   Describe story functions, not names, countries, franchises, or ornamental
   nouns. Use that complete string as `--seed`; keep `--tags` empty so SGGOI
   automation and skill-side checks reserve the same online key.
4. Run `check` before a candidate may win. Any prior status (`presented`,
   `selected`, `generated`, or `rejected`) is burned by default.
5. Add every candidate as `presented` before displaying it. Unselected and
   rejected candidates must not return in later sessions.
6. After the user selects or generates a topic, add the corresponding status.

An existing serialized work may keep its established main premise under the
same work id. A genuinely new episode angle, hot seed, conflict engine, or
payoff still passes this gate. If the online service reports a conflict, reject
the candidate and select another one; never continue on the basis of local
history alone.

Only reuse a blocked topic when the user explicitly asks to revisit, remake,
continue, or compare it. Do not silently recycle a hotspot across domains; a
news event already used for an isekai premise is also burned for explainers,
female fantasy, silver literature, and general web fiction.

```powershell
python "$HOME/.codex/skills/story/scripts/topic_history.py" --root . import-existing
python "$HOME/.codex/skills/story/scripts/topic_history.py" --root . summary
python "$HOME/.codex/skills/story/scripts/topic_history.py" --root . check --seed "{role=...|engine=...|pressure=...|payoff=...|venue=...|aftertaste=...}" --tags ""
python "$HOME/.codex/skills/story/scripts/topic_history.py" --root . add --domain "{domain}" --source "{source}" --seed "{same semantic fingerprint}" --tags "" --status presented
python "$HOME/.codex/skills/story/scripts/topic_history.py" --root . sync-company
```

If no writable project root exists, the skill must still use the SGGOI online
bridge when available. If neither the online bridge nor a writable fallback is
available, stop before presenting or generating a new topic and clearly report
that company-wide deduplication is unavailable.
