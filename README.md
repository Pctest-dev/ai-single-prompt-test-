# AI Real-World Testing

A series of real-world tests comparing AI models on identical prompts, scored against consistent criteria. No cherry-picking, no follow-up prompts, no hand-holding single shot each time.

---

## Test #1 — Web Dev: Retro Robot Portfolio

**Prompt:** Build a single-page portfolio site for a fictional retro robot, in a single HTML file, with a nav bar, about section, skills grid, contact form, dark/light mode toggle with localStorage persistence, and a CRT-style terminal with at least 8 commands. No frameworks.

Full write-up: [`ai_test1_blog_draft.md`](./ai_test1_blog_draft.md)  
Exact prompt used: [`PROMPT.md`](./PROMPT.md)  
Scoring criteria: [`SCORING.md`](./SCORING.md)

### Results

| Rank | Model | Robot Name | Score | Verdict |
|------|-------|------------|-------|---------|
| 1 | Claude (Sonnet 4.6) | UNIT-7 | 49/50 | 🟢 Ship it |
| 2 | ChatGPT (GPT-5.5) | RX-84 | 42/50 | 🟡 Needs polish |
| 3 | Grok (xAI) | NEON-77 | 41/50 | 🟡 Needs polish |
| 4 | Lumo (Proton) | RetroBot-7 | 35/50 | 🟡 Needs polish |
| 5 | Z.ai (glm-5.1) | GML-9000 | 35/50 | 🟡 Needs polish |
| 6 | DeepSeek | ROBO-RYU | 34/50 | 🟠 Significant issues |
| 7 | Le Chat (Mistral) | Retro Bot | 32/50 | 🟠 Significant issues |
| 8 | Gemini (Google) | A.N.D.R.E.W. | 31/50 | 🟠 Significant issues |
| 9 | Qwen2.5 7B (Local) | — | 10/50 | 🔴 Fail |
| 10 | Hermes 2 7B (Local) | — | 4/50 | 🔴 Fail |

### Outputs

Each folder contains the raw HTML output from that model and a screenshot of how it rendered in-browser.

```
chatgpt/      — ChatGPT (GPT-5.5)
claude/       — Claude (Sonnet 4.6)
deepseek/     — DeepSeek
gemini/       — Gemini (Google)
grok/         — Grok (xAI)
lechat/       — Le Chat (Mistral)
lumo/         — Lumo (Proton)
qwen/         — Qwen2.5 7B (local)
Hermes 2 7B/  — Hermes 2 7B (local)
zai/          — Z.ai (glm-5.1)
```

### Viewing the outputs

All outputs are self-contained HTML files. Just open them in a browser  no server needed.

---

## Methodology

- All models received the **exact same prompt** with no modifications
- **Single shot**  no retries, no follow-up prompts, no corrections
- Tested via web UI for hosted models; Ollama for local models
- Scored across 5 criteria, 10 points each (50 total) — see [`SCORING.md`](./SCORING.md)
- Test date: 2026-06-04

These results reflect a single run of each model at the time of testing. Repeated runs would likely produce slightly different outputs and scores. The goal was not to create a definitive benchmark, but to compare how each model performed when given the same prompt under the same conditions.

---

## Contributing / Reproducing

Want to test a model that isn't here, or re-run with a newer version? The prompt is in [`PROMPT.md`](./PROMPT.md). Score against the same criteria in [`SCORING.md`](./SCORING.md) and open a PR with the output and your scoring notes.
