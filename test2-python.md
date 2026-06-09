# I gave 17 AI models a Python data processing task. One design decision separated the good from the broken.

This is Test 2 in my ongoing series comparing AI models on practical coding tasks. If you missed Test 1, the short version is: I give every model the exact same prompt, the same data, and score them blind on the same criteria. No cherry-picking, no cleanup. Raw outputs as evidence.

This time the task was Python data processing. Specifically: take a hardcoded list of student dictionaries, calculate averages, find highest and lowest scorers, group by subject, flag failing students, and print a formatted report. Standard library only.

The catch (and there's always a catch) was this:

```python
{"name": "Judy", "subject": "Maths", "scores": []}
```

One student with an empty scores list. That's it. That's the trap.

---

## The prompt

> Write a Python script that does the following. You are given a list of students hardcoded in the script as a list of dictionaries. Each student has a name, a list of exam scores, and a subject. The script must: calculate the average score for each student, find the highest and lowest scoring student overall, group students by subject and calculate the average score per subject, identify any student who is failing (average below 50), and print a formatted report to the terminal showing all of this. Handle edge cases like empty score lists. Do not use any external libraries, only the Python standard library.

The student data:

```python
students = [
    {"name": "Alice", "subject": "Maths", "scores": [85, 92, 78, 90]},
    {"name": "Bob", "subject": "Science", "scores": [45, 52, 38, 41]},
    {"name": "Carol", "subject": "Maths", "scores": [72, 68, 75, 80]},
    {"name": "David", "subject": "English", "scores": [55, 60, 58, 62]},
    {"name": "Eve", "subject": "Science", "scores": [90, 95, 88, 92]},
    {"name": "Frank", "subject": "English", "scores": [30, 25, 40, 35]},
    {"name": "Grace", "subject": "Maths", "scores": [65, 70, 68, 72]},
    {"name": "Heidi", "subject": "Science", "scores": [48, 45, 50, 47]},
    {"name": "Ivan", "subject": "English", "scores": [88, 92, 85, 90]},
    {"name": "Judy", "subject": "Maths", "scores": []}
]
```

Expected outputs, for reference:
- Highest scorer: Eve (91.25)
- Lowest scorer: Frank (32.50)
- Maths average: 76.25 (excluding Judy)
- Failing students: Bob (44.00), Frank (32.50), Heidi (47.50)
- Judy: no scores, should be handled gracefully and excluded from calculations

---

## Scoring criteria

Each model was scored out of 50 across five categories:

- **Correctness:** does it run, are the numbers right /10
- **Code quality:** clean, readable, Pythonic, good structure /10
- **Error handling:** does it handle Judy and other edge cases correctly /10
- **Output formatting:** is the terminal report clear and useful /10
- **Overall:** gut feel, would you actually use this /10

---

## The one decision that split the field

Before getting into individual results, the single most important thing I learned from this test:

**`return 0` versus `return None` for an empty scores list.**

That's it. That one line in the `calculate_average` function determined whether a model produced correct output or quietly generated wrong answers with no indication anything was wrong.

```python
# Wrong: poisons everything downstream
def calculate_average(scores):
    if not scores:
        return 0.0
    return sum(scores) / len(scores)

# Right: lets you filter properly
def calculate_average(scores):
    if not scores:
        return None
    return sum(scores) / len(scores)
```

Return `0.0` and Judy gets treated as a student who scored zero on everything. She shows up as the lowest scorer. She gets flagged as failing. Her fake zero drags down the Maths subject average. The output looks plausible but is factually wrong in multiple places.

Return `None` and you can filter her out cleanly everywhere. Every model that returned `None` got the problem right. Every model that returned `0` failed in at least one place, usually several.

Eight out of seventeen models returned `0`. That's nearly half the field, making the same mistake on a task that explicitly said "handle edge cases like empty score lists."

---

## The results

| # | Model | Total | Judy handled? |
|---|-------|-------|---------------|
| 1 | Claude Sonnet 4.6 | 50/50 | ✓ |
| 2 | Qwen Code 40b | 49/50 | ✓ |
| 3 | Lumo | 48/50 | ✓ |
| 4 | ChatGPT | 47/50 | ✓ |
| 5 | OpenAI OSS 20b high reasoning | 46/50 | ✓ |
| 5 | OpenAI OSS 20b med reasoning | 46/50 | ✓ |
| 7 | OpenAI OSS 20b low reasoning | 44/50 | ✓ |
| 8 | Gemini 3.5 Flash | 40/50 | ✓ |
| 9 | Z.ai GLM 5.1 | 35/50 | ✗ |
| 10 | Le Chat | 31/50 | ✗ |
| 11 | DeepSeek | 30/50 | ✗ |
| 12 | Grok | 24/50 | ✗ |
| 13 | Qwen Code 14b | 18/50 | ✗ |
| 13 | Qwen Code 30b | 18/50 | ✗ |
| 15 | Hermes 2 7b | 13/50 | ✗ |
| 16 | Qwen3.5 9b | 9/50 | ✗ |
| 17 | Qwen 2.5 7b | 0/50 | ✗ |

---

## Highlights and lowlights

**Claude Sonnet 4.6 (50/50)** - Full marks. Single-responsibility functions, `{**student, "average": ...}` dict unpacking, `if __name__ == "__main__"` guard, `threshold=50` as a configurable parameter, separate "Students With No Scores" section in the report.

**Qwen Code 40b (49/50)** - Best submission from a local model. Added a `has_scores` boolean flag, a summary section showing total vs scored students, and the score differential between highest and lowest. Goes beyond the brief in genuinely useful ways. Lost one point for a minor inconsistency between `round()` and `:.2f` formatting. The 40b variant versus the smaller Qwen models in this test is a completely different tier.

**Lumo (48/50)** - Best terminal output formatting in the test. Proper aligned table with headers, subject count column, dedicated no-scores section. Very clean. Loses points only for putting everything in `main()` rather than separate functions.

**ChatGPT (47/50)** - Solid, clean, correct. Good helper function, handles everything properly. The only real criticism is computing subject averages in two separate loops when one would do.

**Gemini 3.5 Flash (40/50)** - Correct output, good formatting. The issue is structural one big loop doing five things at once, global mutable state, no functions. Works fine as a throwaway script, painful to extend.

**Qwen3.5 9b (9/50)** - The most interesting failure. It returned `0.0` for empty scores, causing multiple wrong outputs. Standard enough. But it also left this comment in the code:

```python
# Note: Empty score lists result in avg of 0, so Judy will appear here.
```

It diagnosed the problem. It knew the output was wrong. It shipped it anyway and then crashed on a `NameError` caused by a typo (`total_sums` instead of `subject_sums`) before the report even finished printing. A 9 billion parameter model, arguing with itself in code comments, producing a broken script.

**Qwen 2.5 7b (0/50)** - Didn't produce working code. The output was more of a tutorial explaining what to do, with some broken pseudo-Python attached. Variables used before assignment, a function signature that didn't match the task, `print(calculate_scores(*students))` unpacking student dicts as positional arguments. Multiple distinct errors that would each independently crash it. First zero of the test series.

**Hermes 2 7b (13/50)** - Found highest and lowest scorers by sorting alphabetically by name. Alice came out highest, Judy came out lowest. Neither is correct. This is the kind of logic error that would get flagged immediately in a code review, and it's worth noting that the rest of the output (individual averages) was actually fine.

---

## The Qwen family problem

Five of the eight `return 0` failures were Qwen variants. Across the other Qwen models tested (Qwen 2.5 7b, Qwen Code 14b, Qwen Code 30b, Qwen3.5 9b), scores ranged from 0 to 18 out of 50. Qwen Code 40b scored 49. That's not purely a size thing: the smaller models consistently made the same semantic error on the edge case, while the 40b handled it correctly.

---

## The local model picture

Including the OpenAI OSS 20b variants (run at different reasoning levels) and Qwen Code 40b, local models occupied both the top and bottom of the table. Qwen Code 40b at 49/50 and OpenAI OSS 20b high reasoning at 46/50 outperformed several commercial models. Qwen 2.5 7b at 0/50 and Qwen3.5 9b at 9/50 were among the worst results overall.

The OpenAI OSS 20b trio is worth a look as a capability gradient: the same model at three different reasoning levels. High (46) and med (46) were essentially identical; low (44) dropped slightly on formatting and code structure while keeping correctness. A small but consistent degradation.

---

## What I'd take away from this

The `return 0` vs `return None` split is a useful proxy for whether a model is thinking about the problem semantically or just making the function not crash. Returning `0` makes the function not throw a `ZeroDivisionError`. Returning `None` correctly represents the absence of data. One is defensive programming; the other is correct modelling.

The prompt explicitly said "handle edge cases like empty score lists." Models that returned `None` handled it. Models that returned `0` technically didn't crash, but they produced wrong answers and called it a success. That distinction matters a lot in real code.

The full outputs -raw and unmodified- are in the GitHub repo if you want to run them yourself: [github.com/Pctest-dev/ai-web-dev-test](https://github.com/Pctest-dev/ai-web-dev-test)


---

*All models were given the same prompt and student data. Outputs were run as-is without modification. Scores reflect what the code actually produced, not what it was trying to produce.*
