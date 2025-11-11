# Intro to Agents

### Models - Brain
### Tools - Hands
### Orchestration - Combines Models and Tools

# WHat is AI Agent?
  - An agent can think, take actions, and observe the results of those actions to give you a better answer.An AI Agent takes this one step further. An agent can think, take actions, and observe the results of those actions to give you a better answer.
  `Prompt -> Agent -> Thought -> Action -> Observation -> Final Answer`

# Define your agent
  - Now, let's build our agent. We'll configure an Agent by setting its key properties, which tell it what to do and how to operate.

  These are the main properties we'll set:

  - name and description: A simple name and description to identify our agent.
  - model: The specific LLM that will power the agent's reasoning. We'll use "gemini-2.5-flash-lite".
  - instruction: The agent's guiding prompt. This tells the agent what its goal is and how to behave.
  - tools: A list of tools that the agent can use. To start, we'll give it the google_search tool, which lets it find up-to-date information online.