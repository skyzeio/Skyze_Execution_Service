"""Created on 16/10/2017
   @author: michaelnew"""

# Third Party Imports

# Skyze Imports
from Skyze_Messaging_Service.Messages.MessageSkyzeAbstract import *


class MessageSchedulerTest(MessageSkyzeAbstract):
  """Sheduler will send a series of test messages"""

  def __init__(self):
    """Constructor"""
    message_content = "Scheduler Test"
    super().__init__(SkyzeMessageType.SCHEDULER_TEST, message_content)

  def getJSON(self):
    """Return object as JSON"""
    return super().getJSON() + "}"
