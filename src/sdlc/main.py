#!/usr/bin/env python
import sys
import warnings
from datetime import datetime

from crewai import Agent, Task, Crew
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool

from .crew import Sdlc

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """
    Run the crew and progressively append each task result to report.md.
    """
    inputs = {
        'topic': 'AI Agents',
        'current_year': str(datetime.now().year)
    }

    try:
        print("DEBUG: Creating Sdlc() instance...")
        sdlc_instance = Sdlc()
        print("DEBUG: Sdlc() instance created.")

        print("DEBUG: Calling crew()...")
        crew_instance = sdlc_instance.crew()
        print("DEBUG: crew() created.")

        print(">>> Sdlc instance created. Now running the crew tasks one by one...")

        # Set report filename
        report_filename = "report.md"

        # Clean (overwrite) report.md at the start of run
        with open(report_filename, "w", encoding="utf-8") as report_file:
            report_file.write(f"# CrewAI Report\n")
            report_file.write(f"**Topic:** {inputs['topic']}  \n")
            report_file.write(f"**Run Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  \n\n")

        # Run tasks one by one
        for task in crew_instance.tasks:
            print(f"\n>>> Running task: {task.name} ({task.description[:50]}...)")

            try:
                print(f"DEBUG: Starting execute_sync() for task {task.name}...")
                result = task.execute_sync()  # Run the single task
                print(f"DEBUG: Finished execute_sync() for task {task.name}.")

                # Append result to report.md after each task
                with open(report_filename, "a", encoding="utf-8") as report_file:
                    # Dynamically get agent role (name)
                    agent_name = task.agent.role if task.agent else "Unknown Agent"

                    report_file.write(f"# Agent: {agent_name}\n")
                    report_file.write(f"## Final Answer:\n")
                    report_file.write(f"{result}\n\n")

                print(f">>> Task completed and written to report.md: {task.name}")

            except Exception as task_error:
                print(f"!!! Error running task {task.name}: {task_error}")
                # Optionally log the error to report.md too:
                with open(report_filename, "a", encoding="utf-8") as report_file:
                    agent_name = task.agent.role if task.agent else "Unknown Agent"

                    report_file.write(f"# Agent: {agent_name}\n")
                    report_file.write(f"## Final Answer:\n")
                    report_file.write(f"ERROR: {task_error}\n\n")

        print(">>> All tasks completed and report.md updated.")

    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

if __name__ == "__main__":
    run()
