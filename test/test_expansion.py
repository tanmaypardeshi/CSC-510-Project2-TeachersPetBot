###########################
# Tests attendance functionality
###########################


import unittest
from unittest.mock import AsyncMock, MagicMock

# Import the function or method that you want to test.
from bot import on_member_join

class TestDiscordBot(unittest.IsolatedAsyncioTestCase):
    async def test_on_member_join(self):
        # Create a mock member and guild objects.
        member = MagicMock()
        guild = MagicMock()
        guild.name = "TestServer"
        member.guild = guild

        # Create a mock text channel and set its name.
        text_channel = MagicMock()
        text_channel.name = "general"

        # Create a mock important-links channel.
        important_links_channel = MagicMock()
        important_links_channel.name = "important-links"

        # Create a mock message with important links.
        message = MagicMock()
        message.content = "Link1: https://example1.com\nLink2: https://example2.com"

        # Set up the necessary methods and attributes for the mocks.
        guild.text_channels = [text_channel, important_links_channel]
        important_links_channel.history = AsyncMock(return_value=[message])
        import re

        # Mock the send method for the member.
        member.send = AsyncMock()

        # Call the on_member_join event handler.
        await on_member_join(member)

        # Define your expectations and assertions.
        expected_message = "Hello TestMember! Welcome to TestServer :) These are the important links, please follow it: .\n"
        expected_message += "**Link1](https://example1.com)\n**[Link2](https://example2.com)\n"

        # Assert that the member.send method was called with the expected message.
        member.send.assert_called_once_with(expected_message)

if __name__ == '__main__':
    unittest.main()