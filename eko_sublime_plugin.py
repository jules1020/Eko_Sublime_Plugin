"""Import modules."""
import sublime
import sublime_plugin
from . import utils
from . import MetadataTransformer


class EkoSublimePlugin(sublime_plugin.EventListener):
    """Sublime_plugin.EventListener."""

    def __init__(self):
        """
        Access the super of sublime_plugin.EventListener.

        Load and transform JSON.
        """
        super().__init__()
        self.transformed_json = \
            MetadataTransformer.metadatatransformer.transform(
                utils.get_json.url_to_json(
                    "https://developer.helloeko.com/api/autocomplete.json"))

    def on_query_completions(self, view, prefix, locations):
        """
        Called whenever completions are to be presented to the user.

        The prefix is a unicode string of the text to complete.
        """
        return self.transformed_json
