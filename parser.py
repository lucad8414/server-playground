

def embedding_css(html: str, css: str, phrase: str) -> str:
    """
    Replaces the phrase in html with <style> the css files content </style>.
    
    :param html: Filename of the html document, which is parsed.
    :type html: str
    :param css: Name of the Stylesheet.
    :type css: str
    :param phrase: The exact format the html file uses to href the stylesheet.
    :type phrase: str
    :return: The html code with the css code embedded in the html style segment.
    :rtype: str
    """
    with open(html, "r") as file:
        html_code = file.read()
        with open(css, "r") as design:
            css_code = design.read()
            insertion_index = html_code.find(phrase)
            
            if insertion_index == -1:
                assert False
            
            website = html_code[:insertion_index] + "<style>" + css_code + "</style>" + html_code[insertion_index + len(phrase):]
            return website
