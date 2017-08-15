"""Import modules."""
import sublime_plugin
import json
import urllib.request


class EkoSublimePlugin(sublime_plugin.EventListener):
    """Sublime_plugin.EventListener."""

    global retval
    retval = []

    def url_to_json(metadata):
        with urllib.request.urlopen(metadata) as url:
            data = json.loads(url.read().decode())
            return (data)
    url_to_json("https://developer.helloeko.com/api/autocomplete.json")

    def transform(json):
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
        return (retval)
