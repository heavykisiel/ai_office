from agents.Agent import Agent

class Room:
    def __init__(self, name, api_token):
        self.name = name
        self.agents = []
        self.conversations = []# Stores the history of messages
        self.api_token = api_token

    def add_agent(self, agent):
        """Adds an agent to the room."""
        self.agents.append(agent)

    def remove_agent(self, agent):
        """Removes an agent from the room."""
        self.agents.remove(agent)

    def broadcast_message(self, agent_name, message):
        """Sends a message from one agent to all others."""
        formatted_message = f"[{agent_name}]: {message}"
        self.conversations.append(formatted_message)
        return formatted_message

    def show_conversation(self):
        """Displays the conversation history."""
        for msg in self.conversations:
            print(msg)
    def start(self):
        agent = Agent(name="Larry", api_token=self.api_token)
        self.add_agent(agent)
        idea_prompt = "Create detailed plan for making simple but profitable app. Based on recent social and technological trends. Build a plan and idea for app in structured and documented way. Take it as seriously as possible."
        idea = self.agents[0].generate_idea(idea_prompt)
        print(f"Generated Idea: {idea}")

