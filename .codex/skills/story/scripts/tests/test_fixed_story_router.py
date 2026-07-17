from __future__ import annotations

import sys
import unittest
from pathlib import Path


SCRIPTS = Path(__file__).resolve().parents[1]
STORY_SKILL = SCRIPTS.parent
sys.path.insert(0, str(SCRIPTS))
import audit_skill_bundle  # noqa: E402


class FixedStoryRouterTest(unittest.TestCase):
    def test_current_story_skill_matches_frozen_v1_contract(self) -> None:
        text = (STORY_SKILL / "SKILL.md").read_text(encoding="utf-8")
        self.assertIsNone(audit_skill_bundle.fixed_story_router_problem(text))

    def test_option_rename_is_blocking_drift(self) -> None:
        text = (STORY_SKILL / "SKILL.md").read_text(encoding="utf-8")
        changed = text.replace("1. 长篇网文／持续连载", "1. 长篇小说／持续连载", 1)
        problem = audit_skill_bundle.fixed_story_router_problem(changed)
        self.assertIsNotNone(problem)
        self.assertIn("user authorization", problem or "")

    def test_option_reordering_is_blocking_drift(self) -> None:
        text = (STORY_SKILL / "SKILL.md").read_text(encoding="utf-8")
        changed = text.replace(
            "1. 长篇网文／持续连载\n2. 短季分集小说／连续剧（默认首季6集）",
            "1. 短季分集小说／连续剧（默认首季6集）\n2. 长篇网文／持续连载",
            1,
        )
        self.assertIsNotNone(audit_skill_bundle.fixed_story_router_problem(changed))


if __name__ == "__main__":
    unittest.main()
