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
    Run the crew and generate a report.md file.
    """
    inputs = {
        'topic': 'AI Agents',
        'current_year': str(datetime.now().year)
    }

    try:
        # Create Sdlc instance
        sdlc_instance = Sdlc()

        print(">>> Sdlc instance created. Now running the crew...")

        # Run the crew and capture results
        results = sdlc_instance.crew().kickoff(inputs=inputs)

        print(">>> Crew run completed. Now generating report.md...")

        # Generate Markdown report
        with open("report.md", "w", encoding="utf-8") as report_file:
            report_file.write(f"# CrewAI Report\n")
            report_file.write(f"**Topic:** {inputs['topic']}  \n")
            report_file.write(f"**Run Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  \n\n")

            if isinstance(results, dict):
                # Sequential mode returns a dict of {task_name: output}
                for task_name, output in results.items():
                    report_file.write(f"## Task: {task_name}\n")
                    report_file.write(f"**Output:**\n\n")
                    report_file.write(f"{output}\n\n")
            elif isinstance(results, list):
                # Some Crew versions can return list of results (depends on process type)
                for idx, output in enumerate(results, 1):
                    report_file.write(f"## Task {idx}\n")
                    report_file.write(f"**Output:**\n\n")
                    report_file.write(f"{output}\n\n")
            else:
                # Unknown format fallback
                report_file.write(f"**Raw Output:**\n\n{results}\n")

        print(">>> Report generated: report.md")

    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        'idea': 'I want to create an AI-powered learning assistant for corporate training that adapts to each employee’s learning style.',
        'current_year': str(datetime.now().year)
    }

    try:
        Sdlc().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        Sdlc().crew().replay(task_id=sys.argv[1])
    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and return the results.
    """
    inputs = {
        'idea': 'I want to create an AI-powered learning assistant for corporate training that adapts to each employee’s learning style.',
        'current_year': str(datetime.now().year)
    }

    try:
        Sdlc().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

if __name__ == "__main__":
    run()
