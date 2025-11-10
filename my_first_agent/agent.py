from google.adk.agents.llm_agent import Agent
from datetime import datetime


def get_instructions() -> str:
    """Returns the instructions."""
    current_time = datetime.now()
    instruction = f"My current time is {current_time} in India, please calculate the time with respect to the timezones for the given city. Please Provide the answer in the format '12th December 2025 HH:MM AM/PM."
    return instruction


root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description="Tells the current time in a specified city.",
    instruction=get_instructions(),  # call the function to pass a string
)