import logging
import pymacaron.models


log = logging.getLogger(__name__)


class Question():
    """Any instance of the OpenAPI schema object 'Question' is made to inherit
    from this python class, by way of the 'x-parent' declaration in the schema"""

    def to_reply(self):
        return pymacaron.models.Hello(message="You said: %s" % self.question)
