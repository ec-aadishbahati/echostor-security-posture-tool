from typing import Annotated, Literal

from pydantic import BaseModel, Field, field_validator


class Recommendation(BaseModel):
    """Structured recommendation with traceability"""

    action: Annotated[str, Field(min_length=10, max_length=500)]
    rationale: Annotated[str, Field(min_length=20, max_length=1000)]
    linked_signals: Annotated[list[str], Field(min_length=1)]
    effort: Literal["Low", "Medium", "High"]
    impact: Literal["Low", "Medium", "High", "Critical"]
    timeline: Literal["30-day", "60-day", "90-day"]
    references: Annotated[list[str], Field(default_factory=list)]

    @field_validator("linked_signals")
    @classmethod
    def validate_signal_format(cls, v: list[str]) -> list[str]:
        for signal in v:
            if not signal.startswith("Q"):
                raise ValueError(f"Signal must start with 'Q': {signal}")
        return v


class Gap(BaseModel):
    """Identified security gap with severity"""

    gap: Annotated[str, Field(min_length=10, max_length=500)]
    linked_signals: Annotated[list[str], Field(min_length=1)]
    severity: Literal["Low", "Medium", "High", "Critical"]

    @field_validator("linked_signals")
    @classmethod
    def validate_signal_format(cls, v: list[str]) -> list[str]:
        for signal in v:
            if not signal.startswith("Q"):
                raise ValueError(f"Signal must start with 'Q': {signal}")
        return v


class Benchmark(BaseModel):
    """Industry benchmark comparison"""

    control: Annotated[str, Field(min_length=1, max_length=200)]
    status: Literal["Implemented", "Partial", "Missing", "Not Applicable"]
    framework: Annotated[str, Field(min_length=1, max_length=50)]
    reference: Annotated[str, Field(default="", max_length=100)]


class SectionAIArtifact(BaseModel):
    """Schema version 1.0 for AI section analysis"""

    schema_version: str = "1.0"
    risk_level: Literal["Low", "Medium", "Medium-High", "High", "Critical"]
    risk_explanation: Annotated[str, Field(min_length=50, max_length=1000)]
    strengths: Annotated[list[str], Field(min_length=1, max_length=5)]
    gaps: Annotated[list[Gap], Field(min_length=1, max_length=5)]
    recommendations: Annotated[list[Recommendation], Field(min_length=1, max_length=5)]
    benchmarks: Annotated[list[Benchmark], Field(min_length=1, max_length=10)]
    confidence_score: Annotated[float, Field(default=0.8, ge=0.0, le=1.0)]

    @field_validator("gaps")
    @classmethod
    def validate_gaps_have_signals(cls, gaps: list[Gap]) -> list[Gap]:
        for gap in gaps:
            if not gap.linked_signals:
                raise ValueError(f"Gap must reference at least one signal: {gap.gap}")
        return gaps

    @field_validator("recommendations")
    @classmethod
    def validate_recommendations_have_signals(
        cls, recs: list[Recommendation]
    ) -> list[Recommendation]:
        for rec in recs:
            if not rec.linked_signals:
                raise ValueError(f"Recommendation must reference signals: {rec.action}")
        return recs

    @field_validator("risk_level")
    @classmethod
    def validate_risk_matches_gaps(cls, risk_level: str, info) -> str:
        if "gaps" in info.data:
            critical_gaps = sum(
                1 for g in info.data["gaps"] if g.severity == "Critical"
            )
            if critical_gaps > 0 and risk_level not in ["High", "Critical"]:
                raise ValueError(
                    "Risk level must be High/Critical when critical gaps exist"
                )
        return risk_level
