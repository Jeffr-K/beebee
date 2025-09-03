from langsmith import evaluate

# TODO: ?
def accuracy_evaluator(run, example):
    prediction = run.outputs["answer"]
    reference = example.outputs["answer"]
    return {"score": 1 if prediction.lower() == reference.lower() else 0}

# TODO: ?
result = evaluate(
    lambda inputs: "<your_chain.invoke(inputs)>",
    data="my-qa-dataset",
    evaludator=[accuracy_evaluator],
    experiment_prefix="my-experiment"
)