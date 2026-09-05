# Prompt Engineering Comparison

## Objective

The objective of this experiment is to compare different prompt
engineering techniques for customer review sentiment classification.

## Customer Review

"The phone looks premium and the delivery was very fast, but the
battery drains quickly and the customer support team took three
days to respond."

## Expected Sentiment

Negative

## Techniques Tested

1. Zero-shot
2. Clear Zero-shot
3. One-shot
4. Few-shot
5. CoT-style

## Comparison

| Technique | Examples | Result | Observation |
|---|---:|---|---|
| Zero-shot | 0 | Negative | Correctly classified the review without any examples. |
| Clear Zero-shot | 0 | Negative | Clear instructions and output format made the response more controlled. |
| One-shot | 1 | Negative | One example helped Gemini understand the expected classification pattern. |
| Few-shot | 3 | Negative | Multiple examples covering Positive, Negative, and Neutral gave the strongest guidance. |
| CoT-style | 0 | Negative | Step-by-step instructions produced a structured analysis, but were more detailed than necessary for this simple task. |

## Best Performing Technique

### Few-shot Prompting

For this customer review sentiment-classification experiment,
Few-shot prompting performed best.

The prompt provided three examples covering Positive, Negative,
and Neutral sentiment. These examples gave Gemini a clear pattern
to follow when classifying the new review.

## Conclusion

The experiment showed that different prompt designs can affect the
quality, structure, and consistency of LLM responses.

Zero-shot prompting worked without examples. Clear Zero-shot improved
the instructions and output format. One-shot provided one example,
while Few-shot provided multiple examples. CoT-style prompting
structured the task into sequential decision steps.

For this particular sentiment-classification task, Few-shot
prompting was selected as the best-performing technique because
the examples provided clear guidance for all three sentiment
categories.

CoT-style prompting can be more useful for complex tasks that
require multiple reasoning steps, while Few-shot prompting was more
suitable for this classification task.