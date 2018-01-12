"""Created on 12/10/2017
   @author: michaelnew"""

# Third Party Imports

# Skyze Imports
from Skyze_Messaging_Service.Messages.MessageSkyzeAbstract import *


class MessageSchedulerRun(MessageSkyzeAbstract):
  """Prompts scheduler to run"""

  def __init__(self):
    """Constructor"""
    message_content = "Scheduler Run"
    super().__init__(SkyzeMessageType.SCHEDULER_RUN, message_content)

  def getJSON(self):
    """Return object as JSON"""
    return super().getJSON() + "}"
