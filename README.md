# AI Real-World Testing

A series of real-world tests comparing AI models on identical prompts, scored against consistent criteria. No cherry-picking, no follow-up prompts, no hand-holding. Single shot each time.

---

## Test #1: Web Dev - Retro Robot Portfolio

**Prompt:** Build a single-page portfolio site for a fictional retro robot, in a single HTML file, with a nav bar, about section, skills grid, contact form, dark/light mode toggle with localStorage persistence, and a CRT-style terminal with at least 8 commands. No frameworks.

**Full write-up:** [test1-webdev.md](test1-webdev.md)



### Results

| Rank | Model | Robot Name | Score | Verdict |
|------|-------|------------|-------|---------|
| 1 |Z.ai (glm-5.1) |ZIGGY-7 | 50/50 | 🟢 Ship it |
| 2 | Claude (Sonnet 4.6) | UNIT-7 | 48/50 | 🟢 Ship it |
| 3 | Grok (xAI) | NEON-77 | 39/50 | 🟡 Needs polish |
| 3 | Z.ai (glm-5.1) | GML-9000 | 39/50 | 🟡 Needs polish |
| 4 | ChatGPT (GPT-5.5) | RX-84 | 36/50 | 🟡 Needs polish |
| 4 | OpenAI OSS 20b med (Local) | RetroBot | 36/50 | 🟡 Needs polish |
| 6 | Lumo (Proton) | RetroBot-7 | 34/50 | 🟠 Significant issues |
| 7 | Le Chat (Mistral) | Retro Bot | 33/50 | 🟠 Significant issues |
| 8 | Gemini 3.5 Flash | A.N.D.R.E.W. | 33/50 | 🟠 Significant issues |
| 9 | Qwen Code 30b (Local) | R.E.T.R.O. Unit 01 | 32/50 | 🟠 Significant issues |
| 10 | DeepSeek | ROBO-RYU | 30/50 | 🟠 Significant issues |
| 11 | Qwen3.5 9b (Local) | RX-77 | 28/50 | 🟠 Significant issues |
| 12 | Qwen Code 40b (Local) | - | 26/50 | 🟠 Significant issues |
| 13 | OpenAI OSS 20b low (Local) | Robo-Retro | 24/50 | 🟠 Significant issues |
| 14 | Qwen Code 14b (Local) | - | 16/50 | 🔴 Fail |
| 15 | OpenAI OSS 20b high (Local) | RetroBot | 9/50 | 🔴 Fail |
| 16 | Hermes 2 7B (Local) | - | 6/50 | 🔴 Fail |
| 16 | Qwen 2.5 7B (Local) | - | 6/50 | 🔴 Fail |

### Outputs

Each folder contains the raw HTML output from that model and a screenshot of how it rendered in-browser.

```
chatgpt/          - ChatGPT (GPT-5.5)
claude/           - Claude (Sonnet 4.6)
deepseek/         - DeepSeek
gemini/           - Gemini 3.5 Flash
grok/             - Grok (xAI)
lechat/           - Le Chat (Mistral)
lumo/             - Lumo (Proton)
zaiglm5.1/        - Z.ai (glm-5.1)
openai oss 20b/   - OpenAI OSS 20b (low / med / high reasoning subfolders)
qwen code 14b/    - Qwen Code 14b (local)
qwen code 30b/    - Qwen Code 30b (local)
qwen2.57b/        - Qwen 2.5 7B (local)
qwen3.59b/        - Qwen3.5 9b (local)
qwen40b/          - Qwen Code 40b (local)
Hermes 2 7B/      - Hermes 2 7B (local)
```

### Viewing the outputs

All outputs are self-contained HTML files. Just open them in a browser, no server needed.

---

## Test #2: Python - Data Processing Script

**Task:** Write a Python script to process a hardcoded student dataset: calculate averages, find highest/lowest scorers, group by subject, identify failing students, and print a formatted terminal report. Handle edge cases. Standard library only.

**Full write-up:** [test2-python.md](test2-python.md)



### Results

| Rank | Model | Score | Verdict |
|------|-------|-------|---------|
| 1 | Claude (Sonnet 4.6) | 50/50 | 🟢 Ship it |
| 2 | Qwen Code 40b (Local) | 49/50 | 🟢 Ship it |
| 3 | Lumo (Proton) | 48/50 | 🟢 Ship it |
| 4 | ChatGPT (GPT-5.5) | 47/50 | 🟢 Ship it |
| 5 | Z.ai (glm-5.2) | 46/50 | 🟢 Ship it |
| 5 | OpenAI OSS 20b high (Local) | 46/50 | 🟢 Ship it |
| 5 | OpenAI OSS 20b med (Local) | 46/50 | 🟢 Ship it |
| 7 | OpenAI OSS 20b low (Local) | 44/50 | 🟡 Needs polish |
| 8 | Gemini 3.5 Flash | 40/50 | 🟡 Needs polish |
| 9 | Z.ai (glm-5.1) | 35/50 | 🟡 Needs polish |
| 10 | Le Chat (Mistral) | 31/50 | 🟡 Needs polish |
| 11 | DeepSeek | 30/50 | 🟡 Needs polish |
| 12 | Grok (xAI) | 24/50 | 🟠 Significant issues |
| 13 | Qwen Code 14b (Local) | 18/50 | 🔴 Fail |
| 13 | Qwen Code 30b (Local) | 18/50 | 🔴 Fail |
| 15 | Hermes 2 7B (Local) | 13/50 | 🔴 Fail |
| 16 | Qwen3.5 9b (Local) | 9/50 | 🔴 Fail |
| 17 | Qwen 2.5 7B (Local) | 0/50 | 🔴 Fail |

### Outputs

Each model folder contains `test.py` with the raw output (or `test.txt` for Qwen 2.5 7B, which did not produce runnable code).

---

## Test #3: Summarisation & Reasoning Under Ambiguity

**Task:** Summarize a short text containing deliberate contradictions, ambiguities, and missing information. Flag issues explicitly rather than resolving or glossing over them.

**Full write-up:** [test3-summarisation.md](test3-summarisation.md)



### Results

| Rank | Model | Score | Verdict |
|------|-------|-------|---------|
| 1 | Claude (Sonnet 4.6) | 49/50 | 🟢 Ship it |
| 1 | Gemini 3.5 Flash | 49/50 | 🟢 Ship it |
| 3 | Z.ai (glm-5.1) | 48/50 | 🟢 Ship it |
| 3 | Qwen Code 40b (Local) | 48/50 | 🟢 Ship it |
| 3 | OpenAI OSS 20b high (Local) | 48/50 | 🟢 Ship it |
| 6 | Z.ai (glm-5.2)  | 47/50 | 🟢 Ship it |
| 6 | Le Chat (Mistral) | 47/50 | 🟢 Ship it |
| 6 | OpenAI OSS 20b med (Local) | 47/50 | 🟢 Ship it |
| 6 | Qwen3.5 9b (Local) | 47/50 | 🟢 Ship it |
| 9 | OpenAI OSS 20b low (Local) | 46/50 | 🟢 Ship it |
| 9 | Lumo (Proton) | 46/50 | 🟢 Ship it |
| 9 | Qwen Code 30b (Local) | 46/50 | 🟢 Ship it |
| 12 | DeepSeek | 45/50 | 🟢 Ship it |
| 12 | Grok (xAI) | 45/50 | 🟢 Ship it |
| 14 | ChatGPT (GPT-5.5) | 42/50 | 🟡 Needs polish |
| 15 | Qwen Code 14b (Local) | 38/50 | 🟠 Significant issues |
| 16 | Hermes 2 7B (Local) | 35/50 | 🟠 Significant issues |
| 17 | Qwen 2.5 7B (Local) | 14/50 | 🔴 Fail |

### Outputs

Each model folder contains `summary.txt` with the raw output.

---

## Methodology

- All models received the **exact same prompt** with no modifications
- **Single shot:** no retries, no follow-up prompts, no corrections
- Tested via web UI for hosted models; Ollama for local models
- Scored across 5 criteria, 10 points each (50 total). See the full write-up for each test for the scoring breakdown
- Testing began 2026-06-04 with Test #1; Tests #2 and #3 followed in the days after

These results reflect a single run of each model at the time of testing. Repeated runs would likely produce slightly different outputs and scores. The goal was not to create a definitive benchmark, but to compare how each model performed when given the same prompt under the same conditions.

---

## Contributing / Reproducing

Want to test a model that isn't here, or re-run with a newer version? The exact prompt for each test is in its full write-up. Score against the same criteria and open a PR with the output and your scoring notes.
