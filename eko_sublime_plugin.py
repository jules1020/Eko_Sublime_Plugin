"""Import modules."""
import sublime
import sublime_plugin


class EkoSublimePluginCommand(sublime_plugin.TextCommand):
    """Eko sublime plugin class."""

    def run(self, edit):
        """Run function."""
        # self.view.insert(edit, 0, "Hello, World!")
        allcontent = sublime.Region(0, self.view.size())
        self.view.replace(edit, allcontent, 'Hello, World')
