import asyncio
from browser_use import Agent, Browser, ChatBrowserUse

async def evaluate_task_determinism():
    """
    Evaluates a browser-use agent by running a deterministic task and validating the output.
    """
    print("Starting deterministic browser-use evaluation...")
    browser = Browser(headless=True)
    llm = ChatBrowserUse()
    
    # A highly deterministic task: Extracting a specific static element
    test_task = "Go to https://example.com and extract the exact text of the main <h1> heading."
    
    agent = Agent(
        task=test_task,
        llm=llm,
        browser=browser,
    )
    
    try:
        result = await agent.run()
        
        # Validation
        if result and "Example Domain" in str(result):
            print("✅ Evaluation Passed: Agent successfully navigated and extracted the expected content.")
            return True
        else:
            print(f"❌ Evaluation Failed: Expected 'Example Domain', got: {result}")
            return False
            
    except Exception as e:
        print(f"❌ Evaluation Failed with exception: {e}")
        return False
    finally:
        await browser.close()

if __name__ == "__main__":
    asyncio.run(evaluate_task_determinism())