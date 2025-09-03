from typing import List, Union, Sequence, Callable, Any, Optional, Type, Literal

from langchain_core.language_models import LanguageModelLike
from langchain_core.runnables.base import RunnableLike
from langchain_core.stores import BaseStore
from langchain_core.tools import BaseTool
from langgraph.graph.graph import CompiledGraph
from langgraph.prebuilt import create_react_agent, ToolNode
from langgraph.prebuilt.chat_agent_executor import Prompt, StructuredResponseSchema, StateSchemaType
from langgraph.types import Checkpointer


class AgentFactory:

    @classmethod
    def take(
        cls,
        amount: int,
        model: Union[str, LanguageModelLike],
        tools: Union[Sequence[Union[BaseTool, Callable, dict[str, Any]]], ToolNode],
        **kwargs
    ) -> Union[CompiledGraph, List[CompiledGraph], None]:
        if amount <= 0:
            return None
        if amount == 1:
            return cls._create_agent(model=model, tools=tools, **kwargs)

        agents: List[CompiledGraph] = []
        for i in range(amount):
            agent_kwargs = kwargs.copy()
            if 'name' not in agent_kwargs or agent_kwargs['name'] is None:
                agent_kwargs['name'] = f"agent_{i + 1}"
            agent = cls._create_agent(model=model, tools=tools, **agent_kwargs)
            agents.append(agent)

        return agents

    @classmethod
    def _create_agent(
        cls,
        model: Union[str, LanguageModelLike],
        tools: Union[Sequence[Union[BaseTool, Callable, dict[str, Any]]], ToolNode],
        prompt: Optional[Prompt] = None,
        response_format: Optional[Union[StructuredResponseSchema, tuple[str, StructuredResponseSchema]]] = None,
        pre_model_hook: Optional[RunnableLike] = None,
        post_model_hook: Optional[RunnableLike] = None,
        state_schema: Optional[StateSchemaType] = None,
        config_schema: Optional[Type[Any]] = None,
        checkpointer: Optional[Checkpointer] = None,
        store: Optional[BaseStore] = None,
        interrupt_before: Optional[list[str]] = None,
        interrupt_after: Optional[list[str]] = None,
        debug: bool = False,
        version: Literal["v1", "v2"] = "v2",
        name: Optional[str] = None,
    ) -> CompiledGraph:
        return create_react_agent(
            model=model,
            tools=tools,
            prompt=prompt,
            response_format=response_format,
            pre_model_hook=pre_model_hook,
            post_model_hook=post_model_hook,
            state_schema=state_schema,
            config_schema=config_schema,
            checkpointer=checkpointer,
            store=store,
            interrupt_before=interrupt_before,
            interrupt_after=interrupt_after,
            debug=debug,
            version=version,
            name=name,
        )

