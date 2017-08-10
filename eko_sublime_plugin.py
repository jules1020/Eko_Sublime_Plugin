"""Import modules."""
import sublime
import sublime_plugin


class EkoSublimePluginCommand(sublime_plugin.TextCommand):
    """sublime_plugin.TextCommand Class."""

    def run(self, edit):
        """Called when the command is run."""
        # self.view.insert(edit, 0, "Hello, World!")
        allcontent = sublime.Region(0, self.view.size())
        self.view.replace(edit, allcontent, 'You rock Julian')
