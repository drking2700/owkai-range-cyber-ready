from pydantic import BaseModel, Field
from typing import Literal

RubricDimension = Literal["accuracy", "risk_reasoning", "fix_justification", "verification", "communication"]

class AIWorkRecord(BaseModel):
    mission_id: int = Field(ge=1, le=16)
    prompts_or_tasks: list[str] = Field(min_length=1)
    accepted_outputs: list[str] = Field(default_factory=list)
    rejected_outputs: list[str] = Field(default_factory=list)
    verification_evidence: list[str] = Field(min_length=1)
    human_decision: str = Field(min_length=10)

class AssistRequest(BaseModel):
    learner_id: str
    mission_id: int = Field(ge=1, le=16)
    question: str = Field(min_length=3, max_length=4000)

class AssistResponse(BaseModel):
    answer: str
    caution: str
    estimated_input_tokens: int
    estimated_output_tokens: int
    estimated_cost_usd: float

class AARSubmission(BaseModel):
    learner_id: str
    mission_id: int = Field(ge=1, le=16)
    answers: dict[str, str]
    ai_work_record: AIWorkRecord

class AARResult(BaseModel):
    scores: dict[str, int]
    total_average: float
    feedback: str
    estimated_cost_usd: float

class ProgressUpdate(BaseModel):
    learner_id: str
    mission_id: int = Field(ge=1, le=16)
    status: Literal["not_started", "in_progress", "verified", "aar_complete", "human_reviewed"]
    verifier_passed: bool = False
    aar_score: float | None = None
