import pytest
from google.adk.evaluation.agent_evaluator import AgentEvaluator


@pytest.mark.asyncio
async def test_time_agent_eval():
    await AgentEvaluator.evaluate(
        agent_module="adk_testbed.agent",
        eval_dataset_file_path_or_dir="evals/simple_time.test.json",
    )
