# This is an auto-generated file - DO NOT EDIT!!!
from pymacaron.model import PymacaronBaseModel
from pydantic import BaseModel
from typing import List, Optional, Literal
from datetime import datetime

__all_models = ["Error", "Ok", "Version"]



class Version(PymacaronBaseModel, BaseModel):
    def get_property_names(self):
        return ["name", "version", "apis", "pym_env"]
    def get_model_api(self):
        return "ping"
    def get_nullable_properties(self):
        return []
    name: Optional[str] = None
    version: Optional[str] = None
    apis: Optional[List[str]] = None
    pym_env: Optional[str] = None


class Ok(PymacaronBaseModel, BaseModel):
    def get_property_names(self):
        return ["ok"]
    def get_model_api(self):
        return "ping"
    def get_nullable_properties(self):
        return []
    ok: Optional[str] = None


class Error(PymacaronBaseModel, BaseModel):
    def get_property_names(self):
        return ["status", "error", "error_description", "error_id", "error_caught", "user_message"]
    def get_model_api(self):
        return "ping"
    def get_nullable_properties(self):
        return []
    status: Optional[int] = None
    error: Optional[str] = None
    error_description: Optional[str] = None
    error_id: Optional[str] = None
    error_caught: Optional[str] = None
    user_message: Optional[str] = None

