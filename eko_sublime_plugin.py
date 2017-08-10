"""Import modules."""
import sublime
import sublime_plugin
import re


# class EkoSublimePluginCommand(sublime_plugin.TextCommand):
#     """sublime_plugin.TextCommand Class."""

#     def run(self, edit):
#         """Called when the command is run."""
#         # self.view.insert(edit, 0, "Hello, World!")
#         allcontent = sublime.Region(0, self.view.size())
#         self.view.replace(edit, allcontent, 'You rock Julian')

class EkoSublimePlugin(sublime_plugin.EventListener):
    """Sublime_plugin.EventListener."""

    def on_query_completions(self, view, prefix, locations):
        """Called whenever completions are to be presented to the user."""
        if is_relevant(view.scope_name(locations[0])):
            return [
                ["you rock", "you rock Julian"],
                ["onP", "onPlayerInit"]
            ]

    def is_relevant(self, scope):
        """Check to see if point is relevant."""
        return True
