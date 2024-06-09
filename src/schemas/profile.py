from pydantic import BaseModel
from typing import List, Optional
from .certification import Certification
from .contact import Contact
from .past_experience import PastExperience
from .programming_skill import ProgrammingSkill
from .project import Project
from .resume import Resume
from .soft_skill import SoftSkill
from .tech_stack import TechStack

class ProfileBase(BaseModel):
    name: str
    description: str

class ProfileCreate(ProfileBase):
    pass

class Profile(ProfileBase):
    id: int

    class Config:
        orm_mode = True

class ProfileDetail(Profile):
    certifications: List[Certification] = []
    contacts: List[Contact] = []
    past_experiences: List[PastExperience] = []
    programming_skills: List[ProgrammingSkill] = []
    projects: List[Project] = []
    resumes: List[Resume] = []
    soft_skills: List[SoftSkill] = []
    tech_stacks: List[TechStack] = []
