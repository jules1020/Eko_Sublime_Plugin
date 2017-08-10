"""Import modules."""
import sublime
import sublime_plugin


class EkoSublimePlugin(sublime_plugin.EventListener):
    """Sublime_plugin.EventListener."""

    def on_query_completions(self, view, prefix, locations):
        """Called whenever completions are to be presented to the user."""
        longname = ''.join(['o', 'b', 'j', 'e', 'c', 't', 'w', 'i', 't', 's', 'h', 'o', 'r', 't', 'n', 'a', 'm', 'e'])
        return ([
            ["me1\teko player method", "method1()"],
            ["me2\tmethod", "method2()"],
            [longname, longname],
            ["fn", "def ${1:name}($2) { $0 }"],
            ["for", "for ($1; $2; $3) { $0 }"],
        ])

    def metadata2array(self, metadata):
        """Take in metadata and outputs an array to be used in autocomplete."""
        array = ["isFull", "isFullscreenSupported"]
        return array
