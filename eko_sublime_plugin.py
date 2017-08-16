"""Import modules."""
import sublime
import sublime_plugin
from . import utils
from . import MetadataTransformer


class EkoSublimePlugin(sublime_plugin.EventListener):
    """Sublime_plugin.EventListener."""

    def on_query_completions(self, view, prefix, locations):
        """
        Called whenever completions are to be presented to the user.

        The prefix is a unicode string of the text to complete.
        """
        return (MetadataTransformer.metadatatransformer.transform(
            utils.get_json.url_to_json(
                "https://developer.helloeko.com/api/autocomplete.json")))
