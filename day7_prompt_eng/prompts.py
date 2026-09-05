CUSTOMER_REVIEW = """
The phone looks premium and the delivery was very fast, but the battery drains quickly and the customer support team took three days to respond
"""
TASK = """
Analyze the customer review and classify its overall sentiment
as Positive, Negative, or Neutral.
"""


def zero_shot_prompt():
    return f"""
{TASK}

Review:
{CUSTOMER_REVIEW}
"""


def one_shot_prompt():
    return f"""
{TASK}

Here is an example:

Review:
"The laptop is fast and lightweight, but the keyboard stopped working."

Classification:
Negative

Reason:
The laptop has positive qualities, but the broken keyboard is a
significant negative issue.

Now analyze this review:

{CUSTOMER_REVIEW}
"""


def few_shot_prompt():
    return f"""
{TASK}

Here are some examples:

Example 1:

Review:
"The headphones have excellent sound quality and arrived earlier than expected."

Classification:
Positive

Reason:
The customer is satisfied with the product quality and delivery.


Example 2:

Review:
"The phone stopped working after two days and customer service did not help."

Classification:
Negative

Reason:
The customer experienced a product failure and poor customer service.


Example 3:

Review:
"The product is okay and works as expected. Nothing special."

Classification:
Neutral

Reason:
The customer does not express strong positive or negative feelings.


Now analyze this review:

{CUSTOMER_REVIEW}
"""


# ADD THIS HERE
def clear_zero_shot_prompt():
    return f"""
You are analyzing customer feedback.

Classify the following review as Positive, Negative, or Neutral.

Consider the overall sentiment of the customer.

Return the answer in this format:

Sentiment:
Reason:

Review:
{CUSTOMER_REVIEW}
"""

def cot_prompt():
    return f"""
Analyze the following customer review.

Review:
{CUSTOMER_REVIEW}

Use these decision steps:

1. Identify the positive aspects.
2. Identify the negative aspects.
3. Compare the positive and negative aspects.
4. Determine the overall sentiment.
5. Give the final classification and a short reason.

Show only the key decision points.
"""