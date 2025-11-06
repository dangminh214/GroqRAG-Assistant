def send_message_to_agent(agent, prompt: str):
    messages = {
        "messages": [
            {
                "role": "user",
                "content": f"{prompt}"
            }
        ]
    }

    response = agent.invoke(messages)
    return response