# Copyright 2016 Mycroft AI, Inc.
#
# This file is part of Mycroft Core.
#
# Mycroft Core is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Mycroft Core is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Mycroft Core.  If not, see <http://www.gnu.org/licenses/>.

from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_handler
from mycroft.skills import resting_screen_handler
from mycroft.skills.skill_loader import load_skill_module

class Ziggy(MycroftSkill):
    def __init__(self):
        """ The __init__ method is called when the Skill is first constructed.
        It is often used to declare variables or perform setup actions, however
        it cannot utilise MycroftSkill methods as the class does not yet exist.
        """
        super(Ziggy, self).__init__(name="ZiggyAI")

    def initialize(self):
        # Make Import For TimeData
        try:
            time_date_path = "/opt/mycroft/skills/skill-date-time.builderjer/__init__.py"
            time_date_id = "timedateskill"
            datetimeskill = load_skill_module(time_date_path, time_date_id)
            from datetimeskill import TimeSkill
            self.dt_skill = TimeSkill()

        except:
            print("Failed To Import DateTime Skill")

    @intent_handler(IntentBuilder('ShowHomeScreen').require('HomeScreenKeyword'))
    def handle_show_home_screen_intent(self, message):
        """ This is an Adapt intent handler, it is triggered by a keyword."""
        self.speak("show home screen")

    @intent_handler('HomeScreen.intent')
    def handle_how_are_you_intent(self, message):
        """ This is a Padatious intent handler.
        It is triggered using a list of sample phrases."""
        self.speak("home screen intent")

    @resting_screen_handler("ZiggyMain")
    def handle_idle(self, message):
        self.log.info("Ziggy main home screen")
        self.gui.clear()
        self.gui["title"] = self.name
        self.gui["time"] = self.dt_skill.get_display_current_time()
        self.gui["date"] = self.dt_skill.get_display_date()
        self.gui["weekday"] = self.dt_skill.get_weekday()
        self.gui.show_page("idle.qml")
    #
    # @intent_handler(IntentBuilder('HelloWorldIntent')
    #                 .require('HelloWorldKeyword'))
    # def handle_hello_world_intent(self, message):
    #     """ Skills can log useful information. These will appear in the CLI and
    #     the skills.log file."""
    #     self.log.info("There are five types of log messages: "
    #                   "info, debug, warning, error, and exception.")
    #     self.speak_dialog("hello.world")

    def stop(self):
        pass


def create_skill():
    return Ziggy()
