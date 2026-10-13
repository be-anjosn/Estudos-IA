import ollama
from Models import AnalyzeFeedback


def ai_generation(argument):
    message = {
    'role': 'user',
    'content': 
    f"""
        You are an expert customer feedback analyzer. Output ONLY a valid JSON object matching this exact schema:
        "feeling": "positive" | "negative" | "neutral",
        "customer_service_rating": 1 | 2 | 3 | 4 | 5,
        "short_summary": "one-sentence factual summary",
        "name": "full name or 'Unknown'"
        

        STRICT CLASSIFICATION RULES:
        - "positive" (rating 4 or 5): Overall satisfied customer, compliments, or successful resolution.
        - "negative" (rating 1 or 2): Broken items, unanswered complaints, delays, or severe dissatisfaction. Rating 1 for total failure, 2 for minor/partial issues.
        - "neutral" (rating 3): Standard experience, meeting basic expectations without strong emotion, OR mixed reviews where positive and negative points balance out.
        - "short_summary": Must reflect ONLY facts explicitly stated in the text. Do NOT invert compliments into complaints.
        - "name": Extract ONLY explicit real names (e.g., "My name is X", "This is Y"). Never invent names. Default to "Unknown".

        FEW-SHOT EXAMPLES:
        Text: "This is John Doe. Amazing service and fast shipping! Loved it."
        Output: "feeling": "positive", "customer_service_rating": 5, "short_summary": "Customer loved the service and fast shipping.", "name": "John Doe"

        Text: "Awful experience. Package was completely damaged and no one answers the phone."
        Output: "feeling": "negative", "customer_service_rating": 1, "short_summary": "Package arrived broken and support was unreachable.", "name": "Unknown"

        Text: "The sound quality is crisp and clear, but the ear cups hurt after 30 minutes."
        Output: "feeling": "neutral", "customer_service_rating": 3, "short_summary": "Audio quality is great, but the cushions become uncomfortable over time.", "name": "Unknown"

        Text: "I am Sarah Jenkins. The device works as described in the specs. Standard delivery."
        Output: "feeling": "neutral", "customer_service_rating": 3, "short_summary": "Product works as advertised and shipping was standard.", "name": "Sarah Jenkins"

        Now analyze the following text:
        Text: {argument}
    """
    }

    awnser = ollama.chat(
        model='llama3.2:1b', 
        messages=[message],
        format=AnalyzeFeedback.model_json_schema(),
        options={'temperature': 0.1}
    )

    return awnser['message']['content']

