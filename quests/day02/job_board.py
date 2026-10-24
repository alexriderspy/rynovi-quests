"""Day 2 · The job board bouncer

Job postings arrive from scrapers and forms, and they're messy. Your job: let the good ones in
as clean Pydantic models, and turn the bad ones away with a clear reason.

Run `python quest.py 2` after each TODO.
"""
from pydantic import BaseModel, HttpUrl, Field, ValidationError, field_validator, model_validator  # noqa: F401


class JobPosting(BaseModel):
    # TODO 2.1 · Add these fields:
    #   title: str
    #   company: str
    #   url: HttpUrl
    #   salary_lpa: a float or None, default None, and it can't be negative (hint: Field(default=None, ge=0))
    #   remote: bool, default False
    #   location: str or None, default None
    pass

    # TODO 2.2 · Clean up the title with a @field_validator("title"):
    #   strip spaces at both ends and squash repeated spaces inside ("  ML   Engineer " -> "ML Engineer").
    #   If nothing is left, raise ValueError("title can't be empty").

    # TODO 2.3 · Add a @model_validator(mode="after"):
    #   an on-site job (remote is False) must have a location.
    #   If it's missing, raise ValueError("location is required for on-site jobs"). Return self otherwise.


def parse_postings(raw: list[dict]) -> tuple[list[JobPosting], list[str]]:
    """TODO 2.4 · Validate every record.

    Return (valid_postings, errors). For each bad record add ONE error string, using the first error
    Pydantic reports, in this exact format:  "record {index}: {field}: {message}"
    e.g. "record 3: url: Input should be a valid URL, relative URL without a base"
    (index starts at 0; field is the first item of the error's "loc", or "posting" if loc is empty)
    """
    raise NotImplementedError
