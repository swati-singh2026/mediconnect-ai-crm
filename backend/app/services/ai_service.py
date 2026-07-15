from app.agents.groq_client import get_llm
from app.prompts.interaction_prompt import interaction_prompt


class AIService:
    def __init__(self) -> None:
        self.llm = get_llm()
        self.chain = interaction_prompt | self.llm

    def generate_summary(
        self,
        *,
        doctor_name: str,
        interaction_type: str,
        interaction_date: str,
        summary: str,
        follow_up: str,
    ) -> str:
        response = self.chain.invoke(
            {
                "doctor_name": doctor_name,
                "interaction_type": interaction_type,
                "interaction_date": interaction_date,
                "summary": summary,
                "follow_up": follow_up,
            }
        )

        return str(getattr(response, "content", response))