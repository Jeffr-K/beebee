from langgraph.checkpoint.memory import MemorySaver

from src.core.graph.bedlock import graph_builder

memory = MemorySaver()

graph = graph_builder.compile()

config = {"configurable": {"thread_id": "1"}}

user_input = "Hi there! My name is Will"

events = graph.stream(
    {"messages": [{"role": "user", "content": user_input}]},
    config,
    stream_mode="values"
)

for event in events:
    event["messages"][-1].pretty_print()


# TODO 4. Ask a follow up question.

user_input = "Remember my name?"

events = graph.stream(
    {"messages": [{"role": "user", "content": user_input}]},
    {"configurable": {"thread_id": "2"}},
    stream_mode="values"
)

for event in events:
    event["messages"][-1].pretty_print()


# TODO 5. Inspect the state

snapshot = graph.get_state(config)
