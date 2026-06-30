# Z.ai GLM 5.2 dropped mid-series. We tested it immediately.

This isn't part of the main benchmark series. GLM 5.2 released while the series was already in progress, so it didn't sit in the original Test 1 lineup. Rather than shoehorn it into the existing results and mess with the rankings retroactively, it gets its own post.

The short version: it's significantly better than 5.1, and if it had been in from the start it would have finished second overall.

---

## Background

Z.ai GLM 5.1 was already in the benchmark series from Test 1. It finished joint 5th in the unified rankings with 122/150, solid but not exceptional. The scoping bug in Test 1 that broke the theme toggle entirely was the thing that held it back; without that it would have challenged for the top three.

5.2 dropped, so the obvious thing to do was run the same three tasks and see what changed.

The raw output files are in the [GitHub repo](https://github.com/Pctest-dev/ai-single-prompt-test-) along with everything else from the series.

---

## The scores

| Test | GLM 5.1 | GLM 5.2 |
|------|---------|---------|
| Test 1 (Web Dev) | 39/50 | 50/50 |
| Test 2 (Python) | 35/50 | 46/50 |
| Test 3 (Summarisation) | 48/50 | 47/50 |
| **Total** | **122/150** | **143/150** |

21 point improvement across the same three tasks. That's not incremental, that's a different model.

---

## Test 1: Web Dev (50/50)

The original GLM 5.1 submission scored 39 and was let down by a single scoping bug: `toggleTheme()` defined inside an IIFE, unreachable by the button's onclick handler. One line that broke the entire dark mode toggle.

5.2 doesn't have that problem. It doesn't have any problems.

**Correctness: 10/10.** Toggle works, localStorage persists, `data-theme` on `<html>` with full CSS variable coverage. Terminal has 13 commands, well above the 8 minimum, including a `theme` command that calls `themeBtn.click()` directly, which is a neat trick. `date` evaluates at runtime, `uptime` calculates from an actual start timestamp, `scan` animates with stepped setTimeout. Command history with arrow keys and Ctrl+L to clear. Everything functional, no console errors.

**Code Quality: 10/10.** `escapeHTML()` function defined and used on all user input before it touches the DOM. `print()` uses `textContent` for normal output. `printHTML()` only ever receives hardcoded strings or pre-escaped input. CSS variables fully scoped with a comprehensive token set including glow, shadow, and scanline values. Scroll reveal with IntersectionObserver. Animated ASCII robot art in the hero. The input line is rebuilt dynamically after each command, which is the correct approach for a terminal implementation. Clean throughout.

**Security: 10/10.** This is the right way to do it, and it's worth being specific about why. The correct pattern isn't just "avoid innerHTML," it's sanitising input before it touches the DOM at all. GLM 5.2 does exactly that: `escapeHTML()` runs on raw user input before the prompt echo goes in via `innerHTML`. The `echo` command uses `print()` which uses `textContent`. `printHTML()` only ever handles hardcoded strings or already-escaped output. No user input reaches the DOM unsanitised, anywhere. No inline event handlers in the HTML. Form validation done in JS with a proper regex email check. Best security implementation in the entire series, including Test 1.

**Look: 10/10.** Full page CRT scanline overlay, vignette flicker animation, ASCII robot art in the hero, animated pulse badge, skill cards with progress bars, section titles with bracket decoration, animated scan command. Light mode uses warm parchment tones rather than just flipping everything to white. The `theme` terminal command actually switches the whole page. Genuinely the best looking submission across the entire benchmark, including the original Test 1 batch.

**Overall: 10/10.** If GLM 5.2 had been in the original test it would have tied or beaten Claude Sonnet 4.6 on this task. The security implementation specifically puts it ahead, it's the only submission in the entire series that correctly sanitises input before innerHTML rather than just switching to textContent throughout. That distinction matters: textContent everywhere works, but escapeHTML-then-innerHTML is the more flexible and correct pattern.

---

## Test 2: Python (46/50)

5.1 scored 35 here, largely because of contradictory Judy handling: it returned `0` for empty score lists which caused cascading wrong outputs, but then also tried to exclude Judy elsewhere, producing internal contradictions throughout the report.

5.2 is consistent. It uses `avg > 0` as a sentinel throughout, which is semantically wrong (a genuine zero-scorer would be silently mislabelled) but applied consistently across all functions. For this dataset, where the empty score edge case is a missing student rather than a zero-scorer, the outputs are all correct.

The bigger improvements are in structure and presentation. Single-responsibility functions, tuples as data transport between functions, `threshold=50.0` as a configurable parameter, proper docstrings, `if __name__` guard. Best formatted output in the entire test: PASSING/FAILING/NO SCORES inline status column, subject averages with member names, dedicated excluded-students section, double separators between major sections, aligned column headers throughout.

Lost points on error handling (the `avg > 0` sentinel is the wrong tool even if it works here) and a minor verbosity issue in `find_failing_students`. Everything else was clean.

The jump from 5.1's 35 to 5.2's 46 is mostly explained by 5.1's internal contradictions being fixed. 5.2 picks a consistent approach and sticks to it.

---

## Test 3: Summarisation & Reasoning (47/50)

This one barely changed: 5.1 scored 48, 5.2 scored 47. Essentially the same model on a task that isn't heavily dependent on the code-level improvements 5.2 brings.

Two-section format, well structured. Catches five of the six contradictions cleanly. The councillor disagreement is in the summary but missing from the numbered flags list, the same pattern as a few other models in this test. One point off for that inconsistency, one point off on conciseness for some redundancy between sections. Nothing invented.

The fact that it dropped a point here while gaining 11 points across the other two tests tells you something about where the improvements are focused.

---

## Where 5.2 fits in the overall rankings

For reference, the current unified rankings after three tests:

| Rank | Model | Total /150 |
|------|-------|-----------|
| 1 | Claude Sonnet | 147 |
| n/a | **Z.ai GLM 5.2 (bonus)** | **143** |
| 2 | OAI OSS 20b Med | 129 |
| 3 | Lumo | 128 |
| 4 | ChatGPT | 125 |
| 5 | Qwen 40b | 123 |
| 6 | Gemini 3.5 Flash | 122 |
| 7 | Z.ai GLM 5.1 | 122 |

GLM 5.2 sits between Claude and the rest of the field. The gap to 3rd place (OAI OSS 20b Med, 129) is larger than the gap to 1st (Claude, 147). It's not in the official rankings because it wasn't in the series from the start, but that's where it lands.

---

## The 5.1 to 5.2 jump is worth paying attention to

A 21 point improvement on the same three tasks is significant. The specific failure modes that held 5.1 back, the scoping bug in Test 1 and the contradictory Judy handling in Test 2, are both fixed. The security implementation went from fine to the best in the series.

Whether that improvement holds up on future tasks is the actual question. One version upgrade is a data point, not a trend. GLM 5.2 will be in the main series from Test 4 onwards, so there'll be more to go on.

---

*Raw outputs for GLM 5.2 are in the [GitHub repo](https://github.com/Pctest-dev/ai-single-prompt-test-). Same scoring criteria as the main series: five categories, 10 points each, 50 per test.*
