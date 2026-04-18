from crewai import Agent, Task, Crew
from langchain.tools import DuckDuckGoSearchRun

# Tool
search_tool = DuckDuckGoSearchRun()

# Agent
research_agent = Agent(
    role="Due Diligence Analyst",
    goal="Find company information and identify risks",
    backstory="Expert in corporate compliance and risk analysis",
    tools=[search_tool],
    verbose=True
)

# Task
task = Task(
    description="Research the company 'Infosys India' and provide risk insights",
    agent=research_agent
)

# Crew
crew = Crew(
    agents=[research_agent],
    tasks=[task]
)

# Run
result = crew.kickoff()
print(result)

