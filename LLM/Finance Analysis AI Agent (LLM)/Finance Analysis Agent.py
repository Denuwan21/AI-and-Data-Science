from phi.agent import Agent 
from phi.model.groq import Groq 
from phi.model.openai import OpenAIChat
from dotenv import load_dotenv
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools

load_dotenv()

Finance = Agent(
    name = 'Finance Agent',
    model = Groq(id = 'llama-3.3-70b-versatile'),
    tools = [YFinanceTools(stock_price = True, analyst_recommendations = True)],
    show_tool_calls = True,
    markdown = True,
    instructions = ['Use Table display data']
)

Web = Agent(
    name="Web Agent",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True
)


All_Agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    team = [Finance, Web],
    instructions = ['Use Table display data', 'Always include sources'],
    markdown = True,
    show_tool_calls = True
)

User = input("Type Here: " )

All_Agent.print_response(User, stream = True)
