"""Import modules."""
import sublime
import sublime_plugin
import threading
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
        # Communicate to server in seperate thread to not block this one.
        load_json_thread = threading.Thread(
            group=None,
            target=self.populate_transformed_json,
            args=())
        load_json_thread.start()

    def populate_transformed_json(self):
        """
        Create thread to load and transform json.

        Populate the trasnformed json.
        """
        self.transformed_json = \
            MetadataTransformer.metadatatransformer.transform(
                utils.get_json.url_to_json(
                    "https://developer.helloeko.com/api/autocomplete.json"))

    def on_query_completions(self, view, prefix, locations):
        """
        Called whenever completions are to be presented to the user.

        The prefix is a unicode string of the text to complete.
        """
        try:
            return self.transformed_json
        except AttributeError:
            return None
