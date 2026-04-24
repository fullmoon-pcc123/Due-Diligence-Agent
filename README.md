# Due Diligence Agent

This project uses **CrewAI** to run a **multi-agent due diligence workflow** for a target company.

## What it does

The script creates four collaborating agents:

1. **Corporate Research Analyst**: collects company profile facts.
2. **Financial Risk Analyst**: looks for financial red flags.
3. **Compliance & Legal Analyst**: checks legal/regulatory concerns.
4. **Due Diligence Lead**: synthesizes all outputs into one final report.

All research is performed using a DuckDuckGo search tool and then combined into a final recommendation.

## Quick start

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Set your model API key (example with OpenAI):

   ```bash
   export OPENAI_API_KEY="your_api_key_here"
   ```

3. Run the script:

   ```bash
   python agent.py
   ```

4. Enter a company name when prompted.

## What you should do next

If you're asking "what now?", follow this order:

1. **Run it on 2-3 known companies** (one low risk, one high risk) and confirm output quality.
2. **Verify every source manually** before making decisions; treat agent output as draft research.
3. **Add a scoring rubric** (e.g., 1-5 for financial/compliance/reputation risk) so outcomes are consistent.
4. **Add hard filters** for risky findings (sanctions, major lawsuits, fraud allegations).
5. **Log outputs to a file** (`json`/`md`) so reports are auditable and repeatable.
6. **Decide your go/no-go policy** based on your risk tolerance and industry requirements.

## Important limitations

- DuckDuckGo snippets can be incomplete or outdated.
- The workflow does not yet guarantee source credibility ranking.
- This project is not legal, compliance, or investment advice.
