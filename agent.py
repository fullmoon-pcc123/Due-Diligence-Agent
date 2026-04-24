from crewai import Agent, Task, Crew, Process
from crewai.tools import BaseTool
from duckduckgo_search import DDGS


class SearchTool(BaseTool):
    name: str = "Company Search Tool"
    description: str = "Search the internet for company information"

    def _run(self, query: str) -> str:
        results = []
        with DDGS() as ddgs:
            for item in ddgs.text(query, max_results=8):
                title = item.get("title", "")
                body = item.get("body", "")
                href = item.get("href", "")
                results.append(f"- {title}\n  {body}\n  Source: {href}")
        return "\n".join(results)


search_tool = SearchTool()
company_name = input("Enter company name: ").strip()


research_agent = Agent(
    role="Corporate Research Analyst",
    goal="Collect accurate company profile data and key facts",
    backstory="Specialist in finding reliable company background information.",
    tools=[search_tool],
    verbose=True,
)

finance_agent = Agent(
    role="Financial Risk Analyst",
    goal="Identify financial red flags and stability signals",
    backstory="Expert in debt risk, profitability trends, and liquidity clues.",
    tools=[search_tool],
    verbose=True,
)

compliance_agent = Agent(
    role="Compliance & Legal Analyst",
    goal="Detect legal, regulatory, and reputational concerns",
    backstory="Experienced in sanctions, lawsuits, and governance checks.",
    tools=[search_tool],
    verbose=True,
)

reporting_agent = Agent(
    role="Due Diligence Lead",
    goal="Synthesize specialist findings into one actionable report",
    backstory="Turns fragmented research into decision-ready recommendations.",
    verbose=True,
)


company_profile_task = Task(
    description=(
        f"Research '{company_name}' and summarize core facts: legal name, headquarters, "
        "industry, leadership, ownership hints, and business model. Include source links."
    ),
    expected_output=(
        "Structured company profile in bullet points with source URLs and confidence notes."
    ),
    agent=research_agent,
)

financial_task = Task(
    description=(
        f"Assess financial health signals for '{company_name}'. Search for revenue trends, "
        "debt/insolvency concerns, fundraising or public filing signals, and major risk indicators. "
        "Flag any uncertain claims."
    ),
    expected_output=(
        "Financial risk summary with red/yellow/green flags and source URLs."
    ),
    agent=finance_agent,
)

compliance_task = Task(
    description=(
        f"Check legal/compliance risks for '{company_name}': lawsuits, penalties, sanctions, "
        "data/privacy incidents, ESG controversies, and adverse media."
    ),
    expected_output=(
        "Compliance and legal risk findings with severity levels and source URLs."
    ),
    agent=compliance_agent,
)

final_report_task = Task(
    description=(
        f"Combine all previous outputs into a final due diligence report for '{company_name}'. "
        "Include: executive summary, key risks, open questions, and go/no-go recommendation."
    ),
    expected_output=(
        "Final report in markdown with sections, risk scoring table, and recommendation rationale."
    ),
    agent=reporting_agent,
)


crew = Crew(
    agents=[research_agent, finance_agent, compliance_agent, reporting_agent],
    tasks=[company_profile_task, financial_task, compliance_task, final_report_task],
    process=Process.sequential,
    verbose=True,
)


result = crew.kickoff()
print("\nFINAL OUTPUT:\n")
print(result)
