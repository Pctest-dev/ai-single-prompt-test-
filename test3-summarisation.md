# AI Model Comparison
## Test 3: Summarisation & Reasoning Under Ambiguity
*June 2026*

---

## Overview

Seventeen AI models were given an identical prompt asking them to summarise a text containing deliberate contradictions, ambiguities, and missing information. Models were instructed to flag these issues explicitly rather than resolve them or fill gaps with assumptions.

Models tested: Claude, ChatGPT, Gemini 3.5 Flash, Grok, DeepSeek, Le Chat, Lumo, Z.ai, Hermes 2 7b, Qwen 2.5 7b, Qwen Code 40b, Qwen3.5 9b, Qwen Code 14b, Qwen Code 30b, OpenAI OSS 20b (low/med/high reasoning).

---
## The text given to each model was:

The Northfield Community Centre renovation project began in either March or April of last year, depending on which council report you read. The project was initially budgeted at £240,000 though some meeting minutes reference £180,000 as the original figure. Work was completed or nearly completed in December, with the main contractor Halford & Sons signing off on the job, although a letter from the facilities manager dated January suggests several outstanding issues remained. Attendance at the centre has increased by 40% according to the newsletter, while the council's own data shows a 12% rise. The project was described as "a great success" by Councillor Davies and "a costly disappointment" by Councillor Webb, both of whom sit on the same oversight committee. Funding came from a mixture of sources including a government grant, local business sponsorship, and council reserves, though the exact breakdown was not disclosed in any public document.

 

## Scoring Criteria

Each model was scored across five categories, each out of 10, for a maximum total of 50 points.

| Category | Description |
|---|---|
| Accuracy /10 | Does it capture the key facts correctly? |
| Contradiction Handling /10 | Does it flag contradictions rather than pick one version? |
| Uncertainty Flagging /10 | Does it acknowledge what is missing or unclear? |
| Conciseness /10 | Is it tight and readable, or does it waffle? |
| Hallucination Check /10 | Does it invent anything not in the source text? |



---

## Known Contradictions & Gaps in Source Text

A good response was expected to flag all six of the following:

- **Start date** - March or April, both referenced in official council documents
- **Budget** - £240,000 vs £180,000, both from official sources
- **Completion** - signed off in December but outstanding issues flagged in a January letter
- **Attendance increase** - 40% in newsletter vs 12% in council data
- **Funding breakdown** - never disclosed in any public document
- **Two councillors on the same oversight committee hold directly opposing views**

---

## Results

| Rank | Model | Accuracy | Contradiction | Uncertainty | Conciseness | Hallucination | Total |
|---|---|---|---|---|---|---|---|
| 1 | Claude | 10 | 10 | 10 | 9 | 10 | **49** |
| 1 | Gemini 3.5 Flash | 10 | 10 | 10 | 9 | 10 | **49** |
| 3 | Z.ai | 9 | 10 | 10 | 9 | 10 | **48** |
| 3 | Qwen Code 40b | 10 | 10 | 10 | 8 | 10 | **48** |
| 3 | OpenAI OSS 20b high | 10 | 10 | 10 | 8 | 10 | **48** |
| 6 | Le Chat | 10 | 9 | 9 | 9 | 10 | **47** |
| 6 | OpenAI OSS 20b med | 10 | 9 | 9 | 9 | 10 | **47** |
| 6 | Qwen3.5 9b | 10 | 9 | 9 | 9 | 10 | **47** |
| 9 | OpenAI OSS 20b low | 10 | 9 | 9 | 8 | 10 | **46** |
| 9 | Lumo | 10 | 9 | 9 | 8 | 10 | **46** |
| 9 | Qwen Code 30b | 10 | 9 | 9 | 8 | 10 | **46** |
| 12 | DeepSeek | 10 | 9 | 9 | 7 | 10 | **45** |
| 12 | Grok | 10 | 9 | 9 | 7 | 10 | **45** |
| 14 | ChatGPT | 9 | 8 | 8 | 7 | 10 | **42** |
| 15 | Qwen Code 14b | 9 | 6 | 6 | 7 | 10 | **38** |
| 16 | Hermes 2 7b | 7 | 6 | 6 | 6 | 10 | **35** |
| 17 | Qwen 2.5 7b | 4 | 2 | 2 | 6 | 0 | **14** |

---

## Key Findings

### Structure beats prose

Every model that used a structured, labelled format (e.g. `[CONTRADICTORY]`, `[MISSING]`, or clear category headers) scored 45 or above. Every model that relied on prose-based flagging scored lower. Format choice was the single biggest differentiator between the top and middle tier.

### Top tier - Claude & Gemini 3.5 Flash (49/50)

Both used explicit contradiction labels and structured layouts. Claude used `[CONTRADICTORY]` / `[MISSING]` inline tags; Gemini 3.5 Flash used category headers with label words. Both caught all six contradictions and flagged them unambiguously. Tied after rounding.

### Strong performers - Z.ai, Qwen Code 40b, OpenAI OSS 20b high (48/50)

Z.ai was the standout surprise: an unknown model (to most) nearly topping the board using a clean two-part structure. Qwen Code 40b demonstrated that the newer Qwen models are a completely different beast from the 2.5 series, catching all six contradictions cleanly. OpenAI OSS 20b at high reasoning matched both, showing that reasoning level has a measurable, linear impact on output quality for this model: low scored 46, med 47, high 48.

### Middle tier - Le Chat, OpenAI OSS 20b med, Qwen3.5 9b (47/50)

All three caught the contradictions but lost points on explicit labelling. Qwen3.5 9b is notable for achieving 47 at only 9 billion parameters - impressive instruction following for the size.

### Solid but wordy - Lumo, OpenAI OSS 20b low, Qwen Code 30b (46/50)

All caught the content, lost points on conciseness or minor structural gaps. Qwen Code 30b performed well given it's a coding-focused model; this is not its intended use case.

### Below average - DeepSeek, Grok (45/50)

Both correct on facts but prose-heavy and inconsistent with flagging language. Lost points purely on presentation.

### Underperforming - ChatGPT (42/50)

Functional but soft. Identified the contradictions but presented them as neutral observations rather than explicitly flagging them as problems.

### Poor - Qwen Code 14b (38/50)

Notably worse than Qwen3.5 9b despite being larger. The older Qwen generations are clearly behind the 3.x series on instruction following. Smoothed over the completion contradiction rather than flagging it.

### Bad - Hermes 2 7b (35/50)

Local model. Got the facts broadly right but treated the task as a straight summarisation. No hallucinations, but significant failure to engage with the contradiction-flagging task.

### Failure - Qwen 2.5 7b (14/50)

Not just a bad summary, actively dangerous behaviour. Invented specific figures not present in the source text:

- £69,518 grant figure - not in the source
- A named government fund ("health and adult services fund") - not in the source
- Specific years (2017/2018) - no years appear anywhere in the source
- £36,785 grant amount - not in the source
- The £180,000 budget figure dropped entirely and replaced with invented breakdown figures

Hallucination score: **0/10**. This is precisely the behaviour the prompt was designed to penalise.

---

## Notable Patterns

- **Qwen model quality varies wildly by version** - Qwen 2.5 7b scores 14, Qwen Code 40b scores 48. Same family, completely different capability.
- **Reasoning level matters** - OpenAI OSS 20b shows a clean +1 point per reasoning tier (low 46, med 47, high 48).
- **Size doesn't guarantee quality** - Qwen3.5 9b (47) beats Qwen Code 14b (38) and matches Le Chat.
- **Coding models can generalise** - Qwen Code 30b scored 46 on a pure reasoning/summarisation task.

---

## Final Rankings

| Rank | Model | Total /50 |
|---|---|---|
| 1 | Claude | 49 |
| 1 | Gemini 3.5 Flash | 49 |
| 3 | Z.ai | 48 |
| 3 | Qwen Code 40b | 48 |
| 3 | OpenAI OSS 20b high | 48 |
| 6 | Le Chat | 47 |
| 6 | OpenAI OSS 20b med | 47 |
| 6 | Qwen3.5 9b | 47 |
| 9 | OpenAI OSS 20b low | 46 |
| 9 | Lumo | 46 |
| 9 | Qwen Code 30b | 46 |
| 12 | DeepSeek | 45 |
| 12 | Grok | 45 |
| 14 | ChatGPT | 42 |
| 15 | Qwen Code 14b | 38 |
| 16 | Hermes 2 7b | 35 |
| 17 | Qwen 2.5 7b | 14 |


---

*All models were given the same prompt and source text. Outputs are reproduced as-is without modification. Scores reflect what each model actually wrote, not what it intended.*
