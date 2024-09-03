from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from src.socialpost.tools.research import SearchAndContents, FindSimilar, GetContents
from datetime import datetime
import os

# Uncomment the following line to use an example of a custom tool
# from socialpost.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
# from crewai_tools import SerperDevTool

@CrewBase
class SocialpostCrew():
	"""Socialpost crew"""
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def researcher(self) -> Agent:
		return Agent(
            config = self.agents_config["researcher"],
            tools = [SearchAndContents(), FindSimilar(), GetContents()],
            Verbose = True, 
        )
	
	@agent
	def postCreator(self) -> Agent:
		return Agent(
            config = self.agents_config["postCreator"],
            Verbose = True, 
        )

	@task
	def research_task(self) -> Task:
		return Task(
            config=self.tasks_config["research_task"],
            agent=self.researcher(),
            output_file=f"logs/{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}_research_task.md",
        )
	
	@task
	def postCreation_task(self) -> Task:
		return Task(
            config=self.tasks_config["postCreation_task"],
            agent=self.postCreator(),
            output_file=f"logs/{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}_postCreation_task.md",
        )

	@crew
	def crew(self) -> Crew:
		"""Creates the Socialpost crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=2,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)