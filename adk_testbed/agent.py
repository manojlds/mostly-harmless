from google.adk.agents.llm_agent import Agent


def get_current_time(city: str) -> dict:
    """Returns a canned time for a requested city."""
    return {"status": "success", "city": city, "time": "10:30 AM"}


root_agent = Agent(
    model="opencode/zen-glm-4.7-free",
    name="root_agent",
    description="Tells the current time in a specified city.",
    instruction=(
        "You are a helpful assistant that tells the current time in cities. "
        "Always use the get_current_time tool to answer time questions. "
        "Respond with a single sentence that includes the city name and time."
    ),
    tools=[get_current_time],
)
