# This is an auto-generated file - DO NOT EDIT!!!
from pymacaron.model import PymacaronBaseModel
from pydantic import BaseModel
from typing import List, Optional, Literal
from datetime import datetime
from helloworld.models import Question as ParentQuestion

__all_models = ["Code", "Error", "Hello", "Question"]



class Hello(PymacaronBaseModel, BaseModel):
    def get_property_names(self):
        return ["message"]
    def get_model_api(self):
        return "helloworld"
    def get_nullable_properties(self):
        return []
    message: Optional[str] = None


class Question(ParentQuestion, PymacaronBaseModel, BaseModel):
    def get_property_names(self):
        return ["question"]
    def get_model_api(self):
        return "helloworld"
    def get_nullable_properties(self):
        return []
    question: Optional[str] = None


class Code(PymacaronBaseModel, BaseModel):
    def get_property_names(self):
        return ["code"]
    def get_model_api(self):
        return "helloworld"
    def get_nullable_properties(self):
        return []
    code: Optional[str] = None


class Error(PymacaronBaseModel, BaseModel):
    def get_property_names(self):
        return ["status", "error", "error_description", "error_id", "error_caught", "user_message"]
    def get_model_api(self):
        return "helloworld"
    def get_nullable_properties(self):
        return []
    status: Optional[int] = None
    error: Optional[str] = None
    error_description: Optional[str] = None
    error_id: Optional[str] = None
    error_caught: Optional[str] = None
    user_message: Optional[str] = None

