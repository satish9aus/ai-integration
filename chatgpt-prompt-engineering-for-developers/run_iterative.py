from helper import get_completion

print('RUN: initial prompt')
initial_prompt = '''
Write a short product description for a smartwatch that is simple, friendly, and useful for a busy professional.
'''
initial_response = get_completion(initial_prompt)
print(initial_response)

print('RUN: feedback prompt')
feedback_prompt = f'''
The following product description is intended for a busy professional.
Please do the following:
1. Identify what is good about the description.
2. Suggest two improvements to make it more concise, engaging, and action-oriented.
3. Rewrite the description using those improvements.

Original description:
"""{initial_response}"""
'''
feedback = get_completion(feedback_prompt)
print(feedback)

print('RUN: refined prompt')
refined_prompt = '''
Write a concise, engaging product description for a smartwatch that is designed for a busy professional.
Be action-oriented, highlight the primary benefits, and keep the tone friendly and polished.
Use one paragraph with 2-3 sentences.
'''
refined_response = get_completion(refined_prompt)
print(refined_response)

print('RUN: comparison prompt')
compare_prompt = f'''
Compare the two smartwatch descriptions below.
1. Identify which description is better overall for a busy professional.
2. Explain why.
3. If possible, provide a final polished version that combines the best elements of both.

Description A:
"""{initial_response}"""

Description B:
"""{refined_response}"""
'''
comparison = get_completion(compare_prompt)
print(comparison)
