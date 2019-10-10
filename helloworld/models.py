import logging
from pymacaron_core.models import get_model


log = logging.getLogger(__name__)


class Question():
    """Any instance of the OpenAPI schema object 'Question' is made to inherit
    from this python class, by way of the 'x-parent' declaration in the schema"""

    def to_reply(self):
        return get_model('Hello')(message="You said: %s" % self.question)
