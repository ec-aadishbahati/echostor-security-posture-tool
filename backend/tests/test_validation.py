import pytest
from pydantic import ValidationError

from app.schemas.assessment import AssessmentResponseCreate, ConsultationRequest
from app.schemas.user import UserCreate


class TestUserValidation:
    def test_password_strength_too_short(self):
        with pytest.raises(ValidationError) as exc_info:
            UserCreate(
                email="test@example.com",
                full_name="Test User",
                company_name="Test Company",
                password="Short1!",
            )
        assert "at least 8 characters" in str(exc_info.value)

    def test_password_strength_no_uppercase(self):
        with pytest.raises(ValidationError) as exc_info:
            UserCreate(
                email="test@example.com",
                full_name="Test User",
                company_name="Test Company",
                password="lowercase1!",
            )
        assert "uppercase letter" in str(exc_info.value)

    def test_password_strength_no_lowercase(self):
        with pytest.raises(ValidationError) as exc_info:
            UserCreate(
                email="test@example.com",
                full_name="Test User",
                company_name="Test Company",
                password="UPPERCASE1!",
            )
        assert "lowercase letter" in str(exc_info.value)

    def test_password_strength_no_number(self):
        with pytest.raises(ValidationError) as exc_info:
            UserCreate(
                email="test@example.com",
                full_name="Test User",
                company_name="Test Company",
                password="NoNumber!",
            )
        assert "number" in str(exc_info.value)

    def test_password_strength_no_special(self):
        with pytest.raises(ValidationError) as exc_info:
            UserCreate(
                email="test@example.com",
                full_name="Test User",
                company_name="Test Company",
                password="NoSpecial1",
            )
        assert "special character" in str(exc_info.value)

    def test_password_strength_valid(self):
        user = UserCreate(
            email="test@example.com",
            full_name="Test User",
            company_name="Test Company",
            password="ValidPass123!",
        )
        assert user.password == "ValidPass123!"

    def test_string_length_limits(self):
        with pytest.raises(ValidationError):
            UserCreate(
                email="test@example.com",
                full_name="x" * 101,
                company_name="Test Company",
                password="ValidPass123!",
            )

        with pytest.raises(ValidationError):
            UserCreate(
                email="test@example.com",
                full_name="Test User",
                company_name="x" * 201,
                password="ValidPass123!",
            )


class TestAssessmentValidation:
    def test_answer_value_cannot_be_none(self):
        with pytest.raises(ValidationError) as exc_info:
            AssessmentResponseCreate(
                section_id="section1", question_id="q1", answer_value=None
            )
        assert "cannot be None" in str(exc_info.value)

    def test_answer_value_string_length_limit(self):
        with pytest.raises(ValidationError) as exc_info:
            AssessmentResponseCreate(
                section_id="section1", question_id="q1", answer_value="x" * 5001
            )
        assert "cannot exceed 5000 characters" in str(exc_info.value)

    def test_answer_value_empty_string(self):
        with pytest.raises(ValidationError) as exc_info:
            AssessmentResponseCreate(
                section_id="section1", question_id="q1", answer_value="   "
            )
        assert "cannot be empty" in str(exc_info.value)

    def test_answer_value_list_length_limit(self):
        with pytest.raises(ValidationError) as exc_info:
            AssessmentResponseCreate(
                section_id="section1", question_id="q1", answer_value=["item"] * 101
            )
        assert "cannot exceed 100 items" in str(exc_info.value)

    def test_comment_length_limit(self):
        with pytest.raises(ValidationError):
            AssessmentResponseCreate(
                section_id="section1",
                question_id="q1",
                answer_value="yes",
                comment="x" * 2001,
            )


class TestConsultationValidation:
    def test_consultation_details_required_when_interest_true(self):
        with pytest.raises(ValidationError) as exc_info:
            ConsultationRequest(consultation_interest=True, consultation_details=None)
        assert "required when consultation interest is true" in str(exc_info.value)

    def test_consultation_details_word_count_minimum(self):
        short_text = " ".join(["word"] * 100)
        with pytest.raises(ValidationError) as exc_info:
            ConsultationRequest(
                consultation_interest=True, consultation_details=short_text
            )
        assert "at least 200 words" in str(exc_info.value)

    def test_consultation_details_word_count_maximum(self):
        long_text = " ".join(["word"] * 350)
        with pytest.raises(ValidationError) as exc_info:
            ConsultationRequest(
                consultation_interest=True, consultation_details=long_text
            )
        assert "must not exceed 300 words" in str(exc_info.value)

    def test_consultation_details_valid_word_count(self):
        valid_text = " ".join(["word"] * 250)
        request = ConsultationRequest(
            consultation_interest=True, consultation_details=valid_text
        )
        assert request.consultation_details == valid_text

    def test_consultation_details_not_required_when_interest_false(self):
        request = ConsultationRequest(
            consultation_interest=False, consultation_details=None
        )
        assert request.consultation_interest is False
        assert request.consultation_details is None
