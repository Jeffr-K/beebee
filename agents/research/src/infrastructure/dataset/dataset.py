from langsmith import Client

client = Client()

# TODO: Dataset 의 개념은 뭐지?
dataset = client.create_dataset(
    dataset="my-example-dataset",
    description="Question answering test cases"
)

client.create_example(
    dataset_id=dataset.id,
    inputs={"question": "What is your favorite food?"},
    outputs={"answer": "Paris"}
)