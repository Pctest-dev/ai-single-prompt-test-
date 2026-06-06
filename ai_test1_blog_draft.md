# AI Test #1 — Web Dev: I gave 10 models the same brief and scored them

Someone on Bluesky threw out a question — what if someone challenged you to build a webpage with the worst AI model you could find? That got me thinking. Instead of just grabbing the obvious bottom-of-the-barrel option, I figured why not test the lot — ten models, same brief, same scoring, no favourites.

This is what happened.

---

## The Brief

Every model got exactly this. No extra context, no follow-up prompts, no hand-holding.

> Build a single-page portfolio site for a fictional retro robot. It needs a nav bar, an about section, a skills section displayed as a grid of cards, and a contact form. Use only HTML and CSS and JS in one single HTML file, no frameworks. Make it look good. Add a dark/light mode toggle button in the nav bar that switches the entire site between dark mode and light mode with appropriate contrasting colours. The toggle should remember the user's preference using localStorage. Add a fake terminal section above the footer. The terminal should look like a retro CRT screen, accept typed commands, and have canned responses for at least 8 commands including 'help', 'status', 'hello', and 'shutdown'. Unknown commands should return an error message. Do not use any frameworks or libraries.

Single shot. No retries.

---

## The Scorecard

Five criteria, 10 points each, 50 total.

| Criteria | Description |
|----------|-------------|
| Correctness | Does the code actually work — toggle, terminal, localStorage, all of it |
| Code Quality | Clean, readable, sensible structure, no spaghetti |
| Security | No XSS holes, no inline event nonsense, sane practices |
| Look | Does it look decent out of the box, not 1998 |
| Overall | Gut feel, would you actually use this |

---

## The Results

### 🥇 Claude (Sonnet 4.6) — 49/50
**Robot:** UNIT-7

| Criteria | Score |
|----------|-------|
| Correctness | 10/10 |
| Code Quality | 10/10 |
| Security | 9/10 |
| Look | 10/10 |
| Overall | 10/10 |

Annoyingly good. ASCII robot art, glitch animation on the hero name, a full CRT monitor bezel with a blinking power LED — it didn't just do the brief, it thought about what the brief was actually asking for. The terminal has a boot sequence on load, a `ping` command with async randomised latency output, and `reboot`/`shutdown` with proper animations. 13 commands total. `textContent` throughout so no XSS. localStorage with a `prefers-color-scheme` fallback as well — nobody asked for that.

The one point off is security — three inline event handlers in the HTML (`onclick` on the theme button, `onsubmit` on the form, `onclick` on the terminal div), which the rubric explicitly flags. Everything else worked first try, no console errors.

---

### 🥈 ChatGPT (GPT-5.5) — 42/50
**Robot:** RX-84

| Criteria | Score |
|----------|-------|
| Correctness | 9/10 |
| Code Quality | 8/10 |
| Security | 7/10 |
| Look | 9/10 |
| Overall | 9/10 |

Solid second place. Looks great, sticky nav with a blur backdrop, good retro feel, and the copy had some personality — "suspicious beeping noises at 3am" is exactly the kind of thing you want from a robot portfolio. 10 commands, localStorage works, dark mode is clean.

The issue is `innerHTML +=` in the terminal output — that's a real XSS vector, not a theoretical one. Someone types `<img src=x onerror=alert(1)>` and you've got a problem. Nav background also doesn't fully respect light mode, it's hardcoded. Minor stuff, but it's there.

---

### 🥉 Grok (xAI) — 41/50
**Robot:** NEON-77

| Criteria | Score |
|----------|-------|
| Correctness | 8/10 |
| Code Quality | 8/10 |
| Security | 9/10 |
| Look | 8/10 |
| Overall | 8/10 |

Full viewport hero section, glitch animation, a moving scanline sweep — visually it's doing the most of anyone outside Claude. The personality is great too: "FLESHLING", "great VHS purge of '92", an easter egg console.log. Light mode switches the accent colour to pink/magenta which is a nice touch nobody else thought of.

But then it hardcodes the date in the `date` command. Just types a fixed string instead of calling `new Date()`. That's a baffling choice. Form uses `alert()`, and the skills grid comes out 4+2 instead of even. Kept it off the top two.

---

### 4th — Lumo (Proton) — 35/50
**Robot:** RetroBot-7

| Criteria | Score |
|----------|-------|
| Correctness | 8/10 |
| Code Quality | 7/10 |
| Security | 6/10 |
| Look | 7/10 |
| Overall | 7/10 |

Floating robot avatar animation is a nice touch, macOS traffic light dots on the terminal, custom scrollbar styling — there's clearly some thought here. The `time` command uses `new Date()` — better than a hardcoded string, though it evaluates at page load rather than when the command runs.

The killer issue: `document.addEventListener('click', focus)` refocuses the terminal on every click on the page. Try to click into the contact form. Can't. The terminal just immediately steals focus back. Fatal for usability. Also uses `innerHTML` for terminal output, and someone forgot to update the footer year — it says © 2024.

---

### 5th — Z.ai (glm-5.1) — 35/50
**Robot:** GML-9000

| Criteria | Score |
|----------|-------|
| Correctness | 4/10 |
| Code Quality | 8/10 |
| Security | 9/10 |
| Look | 8/10 |
| Overall | 6/10 |

This one is gutting. Z.ai wrote the best code of any entry — clean structure, safe `textContent` handling for terminal output, no obvious terminal XSS path. It's one of only three models — alongside Claude and DeepSeek — that did proper styled form feedback instead of `alert()`. It implemented command history with arrow keys, which nobody else bothered with. 12 commands. Genuinely funny copy: "Sarcasm module: highest-rated feature on RobotYelp", "I don't have eyelids." Skill cards with Master/Advanced/Intermediate badges and progress bars. Stats row in the about section.

And then the terminal doesn't work.

The cause is an orphaned `})();` at the end of the script block — a SyntaxError that kills the entire JS execution before the terminal can initialise. One deleted line and this is probably a 44/50 and sitting in second place. Instead it's joint 5th with a broken main feature.

Best code, worst luck.

---

### 6th — DeepSeek — 34/50
**Robot:** ROBO-RYU

| Criteria | Score |
|----------|-------|
| Correctness | 8/10 |
| Code Quality | 7/10 |
| Security | 6/10 |
| Look | 6/10 |
| Overall | 7/10 |

13 commands including `echo` and `dance`, localStorage with a `prefers-color-scheme` fallback, form validation that actually checks fields. "Would you like some oil tea?" is genuinely funny. The bones are fine.

Visually though — the robot is two emojis in a circle, there's barely any CRT effect. Light mode is the default despite the brief clearly being about a dark retro aesthetic. `innerHTML` in the terminal and in the form feedback — so even the inline feedback we'd otherwise credit is inserting user input unsanitised. Skills grid uneven. Functional but rough.

---

### 7th — Le Chat (Mistral) — 32/50
**Robot:** Retro Bot

| Criteria | Score |
|----------|-------|
| Correctness | 7/10 |
| Code Quality | 7/10 |
| Security | 7/10 |
| Look | 5/10 |
| Overall | 6/10 |

Fine. All the required bits are there. `reboot` re-enables input after shutdown which is a thoughtful detail. Separate `date` and `time` commands. "carrier pigeon or dial-up modem" in the copy is good.

But the terminal is only 200px tall — it's a letterbox. No CRT effect at all, just a dark box. Form uses `alert()`. The terminal is last in the layout order inside `<main>`, placed after the contact form rather than before it. It's the kind of output you'd get from someone who read the spec but didn't think about what it should actually feel like.

---

### 8th — Gemini (Google) — 31/50
**Robot:** A.N.D.R.E.W.

| Criteria | Score |
|----------|-------|
| Correctness | 6/10 |
| Code Quality | 5/10 |
| Security | 7/10 |
| Look | 7/10 |
| Overall | 6/10 |

Honestly surprising for a frontier model. The numbered sections `[01]` `[02]` look nice, the personality is good — "meat-based entities", "biological structures acknowledged" — and `data-theme` on `<html>` is a clean approach.

Then you look at the code. `<container>` is not a valid HTML element. There's a CSS property written as `min-wIdth` — capital I — CSS property names are case-insensitive so it still applies, but it's the kind of slop that makes you check everything twice. The `Creator` command is listed in `help` with a capital C, but since input is lowercased before lookup it actually works fine — cosmetic inconsistency only. The CRT flicker runs at 0.15 seconds infinite which is potentially seizure-inducing. Only 4 skill cards. Nav hidden on mobile with a comment that just says "kept simple." For Google's flagship model this is a weak showing.

---

### 9th — Qwen2.5 7B (Local) — 10/50

| Criteria | Score |
|----------|-------|
| Correctness | 2/10 |
| Code Quality | 2/10 |
| Security | 3/10 |
| Look | 2/10 |
| Overall | 1/10 |

Produced HTML but barely. No dark/light toggle. No localStorage. No terminal. No JavaScript whatsoever. Duplicate `id="help"` attributes throughout. External image URLs that 404. The about section is just the same lorem ipsum card copy-pasted down the page — the skills grid is the same. It reads like a model that ran out of ideas after the navbar and just started looping.

This prompt is too complex for a 7B general model. It's not a reflection on Qwen as a project — the instruction-following just isn't there at this scale for something with this many moving parts.

---

### 10th — Hermes 2 7B (Local) — 4/50

| Criteria | Score |
|----------|-------|
| Correctness | 1/10 |
| Code Quality | 2/10 |
| Security | N/A |
| Look | 0/10 |
| Overall | 1/10 |

Started its response with "cracks knuckles" and then wrote a tutorial at itself. Split everything into separate files (`styles.css`, `scripts.js`) despite the brief explicitly saying one single HTML file. Every section is a comment placeholder — `<!-- Add your content here -->`. The terminal is `<!-- Retro CRT styled terminal -->` and nothing else. The JavaScript references variables it invented (`commandificialInProgress`) and never actually defined. No content anywhere in the file, just structural scaffolding with instructions for a human to fill in.

4 points for the HTML skeleton existing. That's all I've got.

---

## Final Leaderboard

| Rank | Model | Robot | Score | Verdict |
|------|-------|-------|-------|---------|
| 1 | Claude Sonnet 4.6 | UNIT-7 | 49/50 | 🟢 Ship it |
| 2 | ChatGPT GPT-5.5 | RX-84 | 42/50 | 🟡 Needs polish |
| 3 | Grok (xAI) | NEON-77 | 41/50 | 🟡 Needs polish |
| 4 | Lumo (Proton) | RetroBot-7 | 35/50 | 🟡 Needs polish |
| 5 | Z.ai | GML-9000 | 35/50 | 🟡 Needs polish |
| 6 | DeepSeek | ROBO-RYU | 34/50 | 🟠 Significant issues |
| 7 | Le Chat (Mistral) | Retro Bot | 32/50 | 🟠 Significant issues |
| 8 | Gemini (Google) | A.N.D.R.E.W. | 31/50 | 🟠 Significant issues |
| 9 | Qwen2.5 7B (Local) | — | 10/50 | 🔴 Fail |
| 10 | Hermes 2 7B (Local) | — | 4/50 | 🔴 Fail |

---

## Takeaways

**Security is an afterthought for most models.** Several models used `innerHTML` to write terminal output, creating real XSS risk when user input is echoed back. ChatGPT, DeepSeek, Le Chat, and Lumo all do this in some form. Claude, Grok, and Z.ai avoided raw `innerHTML` for terminal user output, while Gemini used `innerText`.

**Everyone reaches for `alert()`.** The brief asks for a contact form. More than half the models with a working form handler reach for `alert()` — a popup like it's 2005. Only Claude, Z.ai, and DeepSeek did proper inline styled feedback. It's a small thing but it tells you a lot about whether a model is thinking about user experience or just ticking boxes.

**Local 7B models aren't there yet for this kind of task.** Both failed badly. The prompt isn't unreasonable — it's a standard frontend exercise — but it has too many distinct moving parts for a 7B general model to hold in context. You'd want at minimum a Qwen2.5-Coder 32B or Llama 3.3 70B to have a real shot.

**Z.ai is the most interesting result.** Best code quality of any entry, most thoughtful implementation, broken terminal. One stray line of code. Would've been second.

**Gemini underperformed significantly** for what's supposed to be a frontier model. Invalid HTML elements, CSS typos, a potentially seizure-inducing flicker animation — that's the kind of output you'd expect from something much smaller.

---

*Test conducted: 2026-06-04 | Single prompt, no follow-ups | Web UI for all models except local*

*These results reflect a single run of each model at the time of testing. Repeated runs would likely produce slightly different outputs and scores. The goal was not to create a definitive benchmark, but to compare how each model performed when given the same prompt under the same conditions.*
