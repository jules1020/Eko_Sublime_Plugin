"""Import modules."""
import sublime
import sublime_plugin
from . import get_json
from . import metadatatransformer


class EkoSublimePlugin(sublime_plugin.EventListener):
    """Sublime_plugin.EventListener."""

    def on_query_completions(self, view, prefix, locations):
        """
        Called whenever completions are to be presented to the user.

        The prefix is a unicode string of the text to complete.
        """
        return (metadatatransformer.transform(get_json.url_to_json(
            "https://developer.helloeko.com/api/autocomplete.json")))
