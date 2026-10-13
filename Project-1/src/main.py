import csv
import Models
from pydantic import ValidationError
from AI import ai_generation


source_file = "../data/incoming_feedback.csv"
list_feedbacks=[]
with open(source_file, mode="r", encoding="utf-8") as file_in:
    reader = csv.DictReader(file_in, delimiter=",")
    for line in reader:
        try:
            text_response = ai_generation(line)
            data = Models.AnalyzeFeedback.model_validate_json(text_response)
            list_feedbacks.append(data.model_dump())
        except ValidationError as e:
            print("\n❌ Pydantic blocked the AI! We caught the following error:")
            print(e)
            continue


destination_file="../data/output_feedback.csv"
with open(destination_file, mode="w", encoding="utf-8") as file_out:
    source_headers = ["feeling", "customer_service_rating", "short_summary","name"]
    mock_writer = csv.DictWriter(file_out, fieldnames=source_headers)
    mock_writer.writeheader()
    mock_writer.writerows(list_feedbacks)

