"""Import modules."""
import sublime
import sublime_plugin
import urllib.request
import json


class EkoSublimePlugin(sublime_plugin.EventListener):
    """Sublime_plugin.EventListener."""

    def on_query_completions(self, view, prefix, locations):
        return ([
            ["on\tEko InterludePlayer Method", "on"],
            ["update\tEko Repository Method", "update"],
            ["pluginInited\tEko InterludePlayer Method", "pluginInited"],
            ["once\tEko Node Method", "once"],
            ["trigger\tEko Node Method", "trigger"],
            ["version\tEko InterludePlayer Member", "version"]])

