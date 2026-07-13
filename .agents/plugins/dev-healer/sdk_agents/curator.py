import asyncio
import os
from pathlib import Path
from google.antigravity import Agent, LocalAgentConfig

async def main():
    print("DevHealer SDK Curator Agent starting...")
    
    # We configure an agent with the local tools (file editing, etc.)
    config = LocalAgentConfig()
    
    # Use the Antigravity SDK to spin up a background agent
    async with Agent(config) as agent:
        prompt = """
        You are the DevHealer Autonomous Curator.
        Your job is to read the recent episodic logs in .agents/memory/episodic/
        and compress them into semantic rules if a recurring failure pattern is found.
        If no new patterns are needed, do nothing.
        """
        response = await agent.chat(prompt)
        print("Curator Agent finished cycle:")
        print(await response.text())

if __name__ == "__main__":
    asyncio.run(main())
