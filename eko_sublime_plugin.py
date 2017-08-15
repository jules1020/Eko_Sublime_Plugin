"""Import modules."""
import sublime_plugin
import urllib.request
import json


class EkoSublimePlugin(sublime_plugin.EventListener):
    """Sublime_plugin.EventListener."""

    global retval
    retval = []

    def url_to_json(metadata):
        """Load the JSON file from a URL."""
        with urllib.request.urlopen(metadata) as url:
            data = json.loads(url.read().decode())
            return (data)
    url_to_json("https://developer.helloeko.com/api/autocomplete.json")

    def transform(json):
        """Transform JSON data into lists for on_query_completions listener."""
        for the_object in json:
            autocomplete = []

            kind = ""
            for value in the_object:
                if the_object["memberof"] != "urls":
                    memberof = the_object["memberof"].capitalize()
            if the_object["kind"] == "function":
                kind = "Method"
            elif the_object["kind"] == "member":
                kind = "Member"

            trigger = the_object["name"] + "\t" + "Eko" + " " \
                + memberof + " " + kind

            autocomplete.append(trigger)
            autocomplete.append(the_object["name"])
            retval.append(autocomplete)
        return retval
    transform(url_to_json(
        "https://developer.helloeko.com/api/autocomplete.json"))

    def on_query_completions(self, view, prefix, locations):
        """
        Called whenever completions are to be presented to the user.

        The prefix is a unicode string of the text to complete.
        """
        return(retval)
