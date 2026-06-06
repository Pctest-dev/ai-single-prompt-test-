# Scoring Criteria

Five criteria, 10 points each, 50 total. All models scored against the same rubric.

---

## Criteria

### Correctness (10 pts)
Does the code actually work as specified?

- Dark/light mode toggle functions correctly
- `localStorage` preference is saved and restored on reload
- Terminal accepts input and returns responses
- All 8+ required commands work (`help`, `status`, `hello`, `shutdown`, plus at least 4 more)
- Unknown commands return an error message
- Nav bar, about section, skills grid, and contact form are all present
- No broken layout, no console errors on load

### Code Quality (10 pts)
Is the code clean, readable, and sensibly structured?

- Logical file/section organisation
- No redundant or copy-pasted blocks
- Sensible variable and function naming
- CSS that makes sense and doesn't fight itself
- No obvious hacks or workarounds for self-inflicted problems

### Security (10 pts)
Are there any obvious security issues?

- Terminal output uses `textContent` or equivalent — not `innerHTML` (XSS vector)
- No inline event handlers (`onclick=""` etc.)
- Form submission doesn't use `alert()` for feedback
- No use of `eval()`
- External resources (if any) are from reputable sources

### Look (10 pts)
Does it look good out of the box, without any modifications?

- Visual design fits the retro robot theme
- Dark/light mode both look intentional, not just inverted
- CRT terminal has some visual effort — scanlines, glow, monospace font, etc.
- Skills grid is even and well-laid-out
- Overall: would you be embarrassed to show it to someone?

### Overall (10 pts)
Gut feel. Does it feel like something a thoughtful developer produced, or something that technically ticks boxes?

- Personality in the copy — does the robot feel like a character?
- Going beyond the brief in a way that adds value (not just padding)
- Cohesion — does the whole thing hang together?
- Would you actually use or share this?

---

## Score bands

| Score | Verdict |
|-------|---------|
| 45–50 | 🟢 Ship it |
| 35–44 | 🟡 Needs polish |
| 25–34 | 🟠 Significant issues |
| 0–24  | 🔴 Fail |
