# Linkedin Post Crew

Linkedin Post project leverages AI to automatically search for the latest and most relevant news in AI, machine learning, and generative AI technologies. It then generates concise and engaging posts tailored for LinkedIn feeds, helping professionals stay updated and share industry insights effortlessly. The project uses a multi-agent AI system to delegate tasks between different AI agents to leverage LLM's capabilities to complete a task more efficiently by making them working together and maximizes efficiency.

## Installation

Ensure you have Python >=3.10 <=3.13 installed on your system. This project uses [Poetry](https://python-poetry.org/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install Poetry:

```bash
pip install poetry
```

Next, navigate to your project directory and install the dependencies:

1. First lock the dependencies and then install them:
```bash
poetry lock
```
```bash
poetry install
```
### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

- Modify `src/socialpost/config/agents.yaml` to define your agents
- Modify `src/socialpost/config/tasks.yaml` to define your tasks
- Modify `src/socialpost/crew.py` to add your own logic, tools and specific args
- Modify `src/socialpost/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
poetry run socialpost
```

This command initializes the socialpost Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will run the create a `report.md` file with the output of a research on LLMs in the root folder.

## Understanding Your Crew

The socialpost Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

## Support

For support, questions, or feedback regarding the Socialpost Crew or crewAI.
- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.
