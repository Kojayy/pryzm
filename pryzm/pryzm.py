
from pryzm import text_attributes

class Pryzm(object):
    """pz = pryzm.Pryzm(); warn = pz._italic().yellow().red; warn("Achtung!")
        ASCII FORMAT:
            ESC[AT;FG;BGm<text>ESC[0m
    """
    _text_attributes = text_attributes
    def __init__(self, *text, echo=False):
        self.text = " ".join(text) 
        self.features = []
        self.ASC = u"\u001b["
        self.CLR = u"\u001b[0m"
        self.echo = echo

        for feature, ansi_code in self._text_attributes.items():
            self._add_color(feature, ansi_code)

    def reset(self):
        self.features = []
        return self

    def _add_color(self, feature, ansi_code):
        """Add dynamic function to insert color code.
            feature: string, the name of the function to add
            ansi_code: integer, the code value to insert

            return: function, adds a function named 'color' wrapping test with ascii code.
        """
        def fn(self, *text):
            text = " ".join(text)
            self.features.append(str(ansi_code))

            if text:
                self.text = text
                saved_return = self.show()
                if self.echo: print(self.show())
                self.reset()
                if self.echo:
                    return saved_return
                else:
                    return
            else:
                return self

        fn.__name__ = feature
        fn.__doc__ = "Apply {0} to text".format(feature)
        setattr(Pryzm, feature, fn)

    def show(self):
        return u"{}{}m{}{}".format(self.ASC, ";".join(self.features), self.text, self.CLR)

    def __str__(self):
        return self.show()

    def __repr__(self):
        return self.show()
