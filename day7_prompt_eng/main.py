from google import genai

from prompts import (
    zero_shot_prompt,
    clear_zero_shot_prompt,
    one_shot_prompt,
    few_shot_prompt,
    cot_prompt
)


client = genai.Client()


print("===== PROMPT ENGINEERING EXPERIMENT =====")
print()
print("1. Zero-shot")
print("2. Clear Zero-shot")
print("3. One-shot")
print("4. Few-shot")
print("5. CoT-style")


choice = input("\nEnter your choice: ")


if choice == "1":
    technique = "Zero-shot"
    prompt = zero_shot_prompt()

elif choice == "2":
    technique = "Clear Zero-shot"
    prompt = clear_zero_shot_prompt()

elif choice == "3":
    technique = "One-shot"
    prompt = one_shot_prompt()

elif choice == "4":
    technique = "Few-shot"
    prompt = few_shot_prompt()

elif choice == "5":
    technique = "CoT-style"
    prompt = cot_prompt()

else:
    print("Invalid choice.")
    exit()


print("\n===== SELECTED TECHNIQUE =====")
print(technique)

print("\n===== PROMPT SENT TO GEMINI =====")
print(prompt)

response = client.models.generate_content(
    model="gemini-3.1-flash-lite",
    contents=prompt
)



print("\n===== GEMINI RESPONSE =====")
print(response.text)