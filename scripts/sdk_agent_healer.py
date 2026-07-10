import asyncio
import os
from google.antigravity import Agent, LocalAgentConfig
from google.antigravity.hooks.policy import deny, allow, ask_user

async def main():
    # Windows-hardened deny-by-default execution policy
    policies = [
        deny("*"),
        allow("view_file"),
        ask_user("run_command")
    ]
    
    config = LocalAgentConfig()
    async with Agent(config) as agent:
        response = await agent.chat("Analyze our workspace rules and print our project self-healing protocol.")
        print(await response.text())

if __name__ == "__main__":
    asyncio.run(main())
