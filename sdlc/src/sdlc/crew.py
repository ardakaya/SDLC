from crewai import Agent, Crew, Task, Process
from crewai.project import agent, crew, task
from sdlc.crew_base import CrewBase
from crewai_tools import SerperDevTool
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

@CrewBase
class Sdlc():
    """Sdlc crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    # === Agents ===

    @agent
    def product_owner(self) -> Agent:
        return Agent(
            config=self.agents_config['product_owner'],
            verbose=True,
            tools=[SerperDevTool()]
        )

    @agent
    def product_manager(self) -> Agent:
        return Agent(
            config=self.agents_config['product_manager'],
            verbose=True,
            tools=[SerperDevTool()]
        )

    @agent
    def scrum_master(self) -> Agent:
        return Agent(
            config=self.agents_config['scrum_master'],
            verbose=True,
            tools=[SerperDevTool()]
        )

    @agent
    def business_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['business_analyst'],
            verbose=True,
            tools=[SerperDevTool()]
        )

    @agent
    def content_designer(self) -> Agent:
        return Agent(
            config=self.agents_config['content_designer'],
            verbose=True,
            tools=[SerperDevTool()]
        )

    @agent
    def software_engineer(self) -> Agent:
        return Agent(
            config=self.agents_config['software_engineer'],
            verbose=True
        )

    @agent
    def tech_lead(self) -> Agent:
        return Agent(
            config=self.agents_config['tech_lead'],
            verbose=True
        )

    @agent
    def qa_engineer(self) -> Agent:
        return Agent(
            config=self.agents_config['qa_engineer'],
            verbose=True
        )

    @agent
    def devops_engineer(self) -> Agent:
        return Agent(
            config=self.agents_config['devops_engineer'],
            verbose=True
        )

    @agent
    def ux_ui_designer(self) -> Agent:
        return Agent(
            config=self.agents_config['ux_ui_designer'],
            verbose=True
        )

    @agent
    def architect(self) -> Agent:
        return Agent(
            config=self.agents_config['architect'],
            verbose=True
        )

    @agent
    def security_engineer(self) -> Agent:
        return Agent(
            config=self.agents_config['security_engineer'],
            verbose=True
        )

    @agent
    def business_stakeholder(self) -> Agent:
        return Agent(
            config=self.agents_config['business_stakeholder'],
            verbose=True
        )

    @agent
    def customer(self) -> Agent:
        return Agent(
            config=self.agents_config['customer'],
            verbose=True
        )

    # === Helper method ===

    def _create_task(self, name: str) -> Task:
        conf = self.tasks_config[name]
        return Task(
            description=conf['description'],
            expected_output=conf['expected_output'],
            agent=conf['agent'],  # should be Agent object
            tools=conf.get('tools', [])
        )
    # === Tasks ===

    @task
    def define_product_vision_task(self) -> Task:
        return self._create_task('define_product_vision')

    @task
    def prioritize_product_backlog_task(self) -> Task:
        return self._create_task('prioritize_product_backlog')

    @task
    def elicit_business_requirements_task(self) -> Task:
        return self._create_task('elicit_business_requirements')

    @task
    def create_initial_content_guidelines_task(self) -> Task:
        return self._create_task('create_initial_content_guidelines')

    @task
    def validate_product_direction_task(self) -> Task:
        return self._create_task('validate_product_direction')

    @task
    def define_system_architecture_task(self) -> Task:
        return self._create_task('define_system_architecture')

    @task
    def create_detailed_technical_design_task(self) -> Task:
        return self._create_task('create_detailed_technical_design')

    @task
    def design_user_experience_task(self) -> Task:
        return self._create_task('design_user_experience')

    @task
    def define_security_requirements_task(self) -> Task:
        return self._create_task('define_security_requirements')

    @task
    def clarify_user_stories_task(self) -> Task:
        return self._create_task('clarify_user_stories')

    @task
    def facilitate_sprint_planning_task(self) -> Task:
        return self._create_task('facilitate_sprint_planning')

    @task
    def develop_software_components_task(self) -> Task:
        return self._create_task('develop_software_components')

    @task
    def review_code_and_mentor_team_task(self) -> Task:
        return self._create_task('review_code_and_mentor_team')

    @task
    def embed_security_in_code_task(self) -> Task:
        return self._create_task('embed_security_in_code')

    @task
    def set_up_ci_cd_pipeline_task(self) -> Task:
        return self._create_task('set_up_ci_cd_pipeline')

    @task
    def design_and_execute_tests_task(self) -> Task:
        return self._create_task('design_and_execute_tests')

    @task
    def conduct_security_testing_task(self) -> Task:
        return self._create_task('conduct_security_testing')

    @task
    def coordinate_uat_task(self) -> Task:
        return self._create_task('coordinate_uat')

    @task
    def participate_in_uat_task(self) -> Task:
        return self._create_task('participate_in_uat')

    @task
    def manage_release_pipeline_task(self) -> Task:
        return self._create_task('manage_release_pipeline')

    @task
    def perform_release_readiness_check_task(self) -> Task:
        return self._create_task('perform_release_readiness_check')

    @task
    def approve_release_task(self) -> Task:
        return self._create_task('approve_release')

    @task
    def finalize_product_documentation_task(self) -> Task:
        return self._create_task('finalize_product_documentation')

    @task
    def monitor_system_health_task(self) -> Task:
        return self._create_task('monitor_system_health')

    @task
    def monitor_security_posture_task(self) -> Task:
        return self._create_task('monitor_security_posture')

    @task
    def analyze_product_kpis_task(self) -> Task:
        return self._create_task('analyze_product_kpis')

    @task
    def facilitate_retrospective_task(self) -> Task:
        return self._create_task('facilitate_retrospective')

    @task
    def refine_product_backlog_task(self) -> Task:
        return self._create_task('refine_product_backlog')

    @task
    def conduct_usability_studies_task(self) -> Task:
        return self._create_task('conduct_usability_studies')

    @task
    def update_product_documentation_task(self) -> Task:
        return self._create_task('update_product_documentation')

    @task
    def provide_continuous_feedback_task(self) -> Task:
        return self._create_task('provide_continuous_feedback')

    @task
    def report_full_sdlc_task(self) -> Task:
        return self._create_task('report_full_sdlc')

    # === Crew ===

    @crew
    def crew(self) -> Crew:
        """Creates the Sdlc crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )
