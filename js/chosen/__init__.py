import fanstatic
import js.jquery

library = fanstatic.Library('chosen', 'resources')

chosen_css = fanstatic.Resource(library, 'chosen.css')

chosen_jquery = fanstatic.Resource(library, 'chosen.jquery.js',
    minified='chosen.jquery.min.js', depends=[js.jquery.jquery, chosen_css])
