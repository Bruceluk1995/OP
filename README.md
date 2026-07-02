# OP Writing Project

Codex story-writing workspace for Japanese RPG isekai drafts and planning.

## Use on another computer

```powershell
git clone https://github.com/Bruceluk1995/OP.git
cd OP
```

Open this folder in Codex, then start a new thread with:

```text
请先读取 AGENTS.md，按这个项目的写作规则继续。
```

If `/skills` does not show `$story`, `$jp-isekai`, or related writing skills, install or copy the Codex skills into that computer's `C:\Users\<your-user>\.codex\skills` folder, then open a new Codex thread.

This repo includes the project skills under `.codex/skills`. On Windows, install them into the local Codex registry with:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\install-codex-skills.ps1
```

After the script finishes, restart Codex and open a new thread. Existing threads may still show an old `/skills` registry.

## Important files

- `AGENTS.md` - project routing and collaboration rules.
- `.codex/` - project hooks, custom agents, and story reference files.
- `episodes/` - drafted Japanese episodes and source chapter adaptations.
- `planning/` - adaptation plans and writing structure.
