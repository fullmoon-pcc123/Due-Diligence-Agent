from crewai import Agent, Task, Crew
from duckduckgo_search import DDGS

# -------- TOOL --------
def search_tool(query):
    results = []
    with DDGS() as ddgs:
        for r in ddgs.text(query, max_results=5):
            results.append(r['body'])
    return "\n".join(results)

# -------- INPUT --------
company_name = input("Enter company name: ")

# -------- AGENT --------
research_agent = Agent(
    role="Due Diligence Analyst",
    goal="Find company information and identify risks",
    backstory="Expert in corporate compliance and risk analysis",
    tools=[search_tool],
    verbose=True
)

# -------- TASK --------
task = Task(
    description=f"Research the company '{company_name}' and provide risk insights",
    agent=research_agent
)

# -------- CREW --------
crew = Crew(
    agents=[research_agent],
    tasks=[task]
)

# -------- RUN --------
result = crew.kickoff()
print("\nFINAL OUTPUT:\n")
print(result)
