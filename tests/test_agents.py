from app.agents.supervisor_agent import (
    SupervisorAgent
)


def test_supervisor_agent():

    agent = SupervisorAgent()

    result = agent.process_case(
        symptoms=[
            "fever",
            "cough"
        ],
        medicines=[
            "Paracetamol"
        ]
    )

    assert result is not None