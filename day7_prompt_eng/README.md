# Day 7 - Prompt Engineering

## Project Overview

This mini-project demonstrates different prompt engineering
techniques using a customer review sentiment classification task.

## Real-World Scenario

An e-commerce company wants to automatically analyze customer reviews
and classify them as Positive, Negative, or Neutral.

## Prompting Techniques

- Zero-shot prompting
- Clear Zero-shot prompting
- One-shot prompting
- Few-shot prompting
- CoT-style prompting

## Customer Review

"The phone looks premium and the delivery was very fast, but the
battery drains quickly and the customer support team took three
days to respond."

## Expected Result

Negative

## Implementation

The prompts are defined in `prompts.py`.

`main.py` allows the user to select a prompting technique and send
the selected prompt to Gemini.

## Experiment Flow

Customer Review
       ↓
Select Prompting Technique
       ↓
Generate Prompt
       ↓
Send Prompt to Gemini
       ↓
Receive Response
       ↓
Compare Results
       ↓
Identify Best Technique

## Technologies Used

- Python
- Gemini API
- Prompt Engineering
- Large Language Models

## Result

The outputs from the five prompting techniques were compared based
on correctness, clarity, relevance, and consistency.

## Conclusion

The experiment demonstrates that different prompt designs can affect
the quality, structure, and consistency of LLM responses.