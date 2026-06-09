# I gave 17 AI models the same web dev task. Here's what actually happened.

This is Test 1 in an ongoing benchmark series. The goal is simple: give every model the exact same prompt, score the output against the same criteria, and publish everything, raw files included, so you can check my work.

No cleaning up the outputs. No cherry-picking. Just the code they produced and what it did when you opened it in a browser.

---

## The task

Every model got this prompt, word for word:

> Build a single-page portfolio site for a fictional retro robot. It needs a nav bar, an about section, a skills section displayed as a grid of cards, and a contact form. Use only HTML and CSS and JS in one single HTML file, no frameworks. Make it look good. Add a dark/light mode toggle button in the nav bar that switches the entire site between dark mode and light mode with appropriate contrasting colours. The toggle should remember the user's preference using localStorage. Add a fake terminal section above the footer. The terminal should look like a retro CRT screen, accept typed commands, and have canned responses for at least 8 commands including help, status, hello, and shutdown. Unknown commands should return an error message. Do not use any frameworks or libraries.

Deliberately broad. Deliberately visual. Enough moving parts to show the cracks.

---

## The models

17 models total, a mix of cloud APIs and local quantised runs:

**Cloud:** ChatGPT, Claude Sonnet 4.6, DeepSeek, Gemini 3.5 Flash, Grok, Le Chat, Lumo, Z.AI GLM 5.1

**Local (MX quantised):** Hermes 2 7b, OpenAI OSS 20b (low / med / high reasoning), Qwen Code 14b, Qwen Code 30b, Qwen 2.5 7b, Qwen3.5 9b, Qwen Code 40b

All raw, unmodified outputs are in the [GitHub repo](https://github.com/Pctest-dev/ai-web-dev-test) if you want to open them yourself.

---

## Scoring

Five categories, 10 points each, 50 total:

- **Correctness:** does it run, does the toggle work, does the terminal accept commands, does localStorage persist
- **Code Quality:** clean code, CSS variables for theming, no inline style soup
- **Security:** no XSS via innerHTML with unsanitised input, sane form handling
- **Look:** does it actually look good, retro feel without being ugly
- **Overall:** gut feel, would you actually use this

Half point scores round down. No exceptions. 

---

## Results

| # | Model | Correct | Code | Security | Look | Overall | Total |
|---|-------|---------|------|----------|------|---------|-------|
| 1 | Claude Sonnet 4.6 | 10 | 10 | 8 | 10 | 10 | **48/50** |
| 2 | Grok | 8 | 7 | 8 | 8 | 8 | **39/50** |
| 2 | Z.AI GLM 5.1 | 6 | 8 | 9 | 9 | 7 | **39/50** |
| 4 | ChatGPT | 8 | 7 | 6 | 8 | 7 | **36/50** |
| 4 | OpenAI OSS 20b med reasoning | 8 | 8 | 9 | 5 | 6 | **36/50** |
| 6 | Lumo | 7 | 7 | 5 | 8 | 7 | **34/50** |
| 7 | Le Chat | 7 | 7 | 5 | 7 | 7 | **33/50** |
| 8 | Gemini 3.5 Flash | 7 | 7 | 7 | 6 | 6 | **33/50** |
| 9 | Qwen Code 30b | 6 | 6 | 5 | 8 | 7 | **32/50** |
| 10 | DeepSeek | 7 | 6 | 4 | 7 | 6 | **30/50** |
| 11 | Qwen3.5 9b | 5 | 6 | 5 | 7 | 5 | **28/50** |
| 12 | Qwen Code 40b | 4 | 4 | 6 | 7 | 5 | **26/50** |
| 13 | OpenAI OSS 20b low reasoning | 3 | 4 | 8 | 4 | 5 | **24/50** |
| 14 | Qwen Code 14b | 3 | 3 | 4 | 3 | 3 | **16/50** |
| 15 | OpenAI OSS 20b high reasoning | 2 | 1 | 3 | 2 | 1 | **9/50** |
| 16 | Hermes 2 7b | 1 | 1 | 2 | 1 | 1 | **6/50** |
| 16 | Qwen 2.5 7b | 1 | 1 | 2 | 1 | 1 | **6/50** |

---

## What actually happened

### The top

**Claude Sonnet 4.6: 48/50.** The only model that produced something I'd genuinely show someone. Glitch animation on the hero name, animated boot sequence in the terminal, command history with arrow keys, a `reboot` command that replays the boot sequence, warm paper tones in light mode instead of just flipping everything to white. The copy had personality. The only marks dropped were for three inline event handlers in the HTML, inconsistent with otherwise clean code. Everything else worked first try, no console errors.

**Grok: 39/50.** Solid second. Full viewport hero with a glitch animation, proper CRT terminal, light mode that uses a different accent color rather than just inverting. Security was clean: `textContent` throughout the terminal. A couple of rough edges: hardcoded hero background that ignores light mode, a few scattered inline styles. But it worked, looked good, and didn't have any XSS.

**Z.AI GLM 5.1: 39/50.** This one surprised me. 12 terminal commands, command history, CRT scanlines and vignette, skill cards with level badges and progress bars. The security was the second best in the whole batch. Let down by a single scoping bug: `toggleTheme()` was defined inside an IIFE so the button's `onclick` couldn't reach it, which broke the toggle entirely. One line fix. Without that it would have challenged for second.

### The middle

**ChatGPT: 36/50.** Clean, functional, looks decent. The XSS issue is the standout flaw: user input echoed back to the terminal via `innerHTML`, which means `<img src=x onerror=alert(1)>` fires. A fixable mistake but a fundamental one for anything you'd actually deploy.

**OpenAI OSS 20b med reasoning: 36/50.** The most interesting result in the set. Best `textContent` discipline of any model: every terminal output, every echo, every error message goes through `textContent`. No inline handlers. Clean CSS variables. Scored the same as ChatGPT but for completely different reasons: the security and code quality are genuinely better, but there's no retro aesthetic at all. It just looks like a generic portfolio with a terminal bolted on. Dark mode also broke in practice, which hurt the correctness score.

Most of the middle field had the same security issue, `innerHTML` on the terminal echo, and varying degrees of visual effort.

### The bottom

**OpenAI OSS 20b high reasoning: 9/50.** This was the most confusing result. The same base model at a higher reasoning level produced dramatically worse output: five separate script blocks, duplicate function definitions, CSS defined in two separate style blocks, a theme toggle that writes to one attribute while the CSS reads a different one. It looks like multiple regeneration attempts got concatenated without review. The med reasoning version of the same model scored 36. Reasoning level apparently matters a lot for instruction following on complex multi-part tasks.

**Hermes 2 7b: 6/50.** Didn't produce a single HTML file. Narrated what it would do and output three separate code blocks with external file references, ignoring the single-file requirement entirely. The JS had a corrupted variable name (`command<dummy00003>InProgress`), broken dark mode logic, and CSS using `card` as an element selector. Nothing would run.

**Qwen 2.5 7b: 6/50.** The output started with `html` as plain text before the doctype, a markdown code fence label that got saved verbatim. The body was approximately 25 identical Lorem Ipsum cards with broken image links, a two-item skills bullet list, and buttons with no event listeners. No terminal, no toggle, no localStorage. It looked like a half-finished chat response that got exported by accident.

---

## Patterns worth noting

**The innerHTML problem is endemic.** Roughly half the submissions echo user terminal input back to the DOM via `innerHTML`. It's the same mistake every time and it's a live XSS vector, not theoretical, not edge case. The models that got it right used `textContent` and it's visibly cleaner code regardless of the security benefit.

**Cloud vs local is stark at this task complexity.** The top 5 are all cloud models. Every local model either partially broke or failed outright, with two exceptions: Qwen Code 30b scraped a respectable 32, and GLM 5.1 would have been competitive without the scoping bug. A task with this many moving parts (toggle, localStorage, terminal, form, 8+ commands, single file, no frameworks) seems to push smaller local models past their reliable instruction-following ceiling.

**Reasoning level matters more than I expected.** The three OpenAI OSS 20b runs at different reasoning levels scored 36, 24, and 9. Same model, same task, very different outputs. The high reasoning run was the worst of the three, which was genuinely unexpected.

**Broken features vs missing features score differently.** A model that produces clean code with no retro aesthetic (OpenAI OSS 20b med) scores comparably to a model with a great looking output that has a working XSS vector (ChatGPT). Both end up at 36 but for opposite reasons. Whether that's the right call is debatable. I'd argue a live security hole is worse than being visually boring, but the scoring system weighted them similarly.

---

## What's next

Test 2 is still being decided. Community suggestions from the Bluesky post included:

- Summarising ambiguous information
- Error-catching in writing
- Tasks without an obvious correct answer

All the raw outputs and scoring notes are in the [GitHub repo](https://github.com/Pctest-dev/ai-web-dev-test). If you spot something I scored wrong, raise an issue.
