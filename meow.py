import os
import random

# I know how terrible this looks


class meow():
    def __init__(self):
        self.tex_file_name = "meowbook.tex"

        self.min_chapter_count = 10
        self.max_chapter_count = 20

        self.min_paragraph_count = 4
        self.max_paragraph_count = 30

        self.min_paragraph_length = 10
        self.max_paragraph_length = 400

        # these are from xcolor latex, some pastel colors
        self.pastelcolors = ("Apricot", "Aquamarine", "Bittersweet", "Black",
                             "Blue", "BlueGreen", "BlueViolet", "BrickRed", "Brown",
                             "BurntOrange", "CadetBlue", "CarnationPink", "Cerulean",
                             "CornflowerBlue", "Cyan", "Dandelion", "DarkOrchid",
                             "Emerald", "ForestGreen", "Fuchsia", "Goldenrod", "Gray",
                             "Green", "GreenYellow", "JungleGreen", "Lavender",
                             "LimeGreen", "Magenta", "Mahogany", "Maroon", "Melon",
                             "MidnightBlue", "Mulberry", "NavyBlue", "OliveGreen",
                             "Orange", "OrangeRed", "Orchid", "Peach", "Periwinkle",
                             "PineGreen", "Plum", "ProcessBlue", "Purple",
                             "RawSienna", "Red", "RedOrange", "RedViolet",
                             "Rhodamine", "RoyalBlue", "RoyalPurple", "RubineRed",
                             "Salmon", "SeaGreen", "Sepia", "SkyBlue", "SpringGreen",
                             "Tan", "TealBlue", "Thistle", "Turquoise", "Violet",
                             "VioletRed", "White", "WildStrawberry", "Yellow",
                             "YellowGreen", "YellowOrange")
        self.pastelcolor = random.choice(self.pastelcolors)

    def main(self):
        if os.path.isfile(self.tex_file_name):
            print("tex file already exists, deleting it and creating a new one")
            os.remove(self.tex_file_name)

        with open(self.tex_file_name, "a+") as f:
            f.write(self.latex_start())

            for chapter in range(random.randint(self.min_chapter_count,
                                                self.max_chapter_count)):

                f.write(r"\chapter{" + "meow " * random.randint(1, 6) + r"}",)

                for paragraph in range(random.randint(self.min_paragraph_count,
                                                      self.max_paragraph_count)):
                    f.write(self.meow_paragraph(self.min_paragraph_length // 5,
                                                self.max_paragraph_length // 5))
                    f.write("\n\n")

                f.write("\n\n")

            f.write(self.latex_finish())

        self.latex_render()

        self.cleanup()

    def latex_start(self):
        start = [
            r"\documentclass[12pt, a5paper, openany]{book}",
            r"\usepackage[utf8]{inputenc}",
            r"\usepackage[english]{babel}",
            r"\usepackage[usenames,dvipsnames]{xcolor}",
            r"\usepackage[a5paper]{geometry}",
            r"",
            r"\usepackage{mathptmx} % something like new times roman",
            r"",
            r"\usepackage{fancyhdr}",
            r"\fancyhf{} % clear all header and footers",
            r"\renewcommand{\headrulewidth}{0pt} % remove the header rule",
            r"\fancyfoot[LE,RO]{\thepage} % Left side on Even pages; Right side on Odd pages",
            r"\pagestyle{fancy}",
            r"\fancypagestyle{plain}{%",
            r"  \fancyhf{}%",
            r"  \renewcommand{\headrulewidth}{0pt}%",
            r"  \fancyhf[lef,rof]{\thepage}%",
            r"}",
            r"  ",
            r"\usepackage[T1]{fontenc}",
            r"\title{" + "Meow " * random.randint(1, 5) + r"}",
            r"\addto\captionsenglish{\renewcommand{\contentsname}{Meow}}",
            r"",
            r"\setlength\oddsidemargin{\dimexpr(\paperwidth-\textwidth)/2 - 1in\relax}",
            r"\setlength\evensidemargin{\oddsidemargin}",
            r"",
            r"\usepackage{titlesec}",
            r"\titleformat{\chapter}[display]",
            r"  {\normalfont\bfseries}{}{0pt}{\Huge}",
            r"",
            r"",
            r"%",
            r"%",
            r"% i'm begging begging youuoouuuuuu",
            r"%",
            r"%",
            r"\begin{document}",
            r"\pagenumbering{gobble}",
            r"",
            r"%cover page",
            r"\pagecolor{" + self.pastelcolor + r"}",
            r"\thispagestyle{empty}",
            r"\maketitle",
            r"\pagecolor{white}",
            r"",
            r"%toc",
            r"\tableofcontents",
            r"\clearpage",
            r"",
            r"\pagenumbering{arabic}",
            r"\setcounter{page}{1}",
            r"",
            r""
        ]

        return "\n".join(start)

    def latex_finish(self):
        end = [
            "\n",
            r"\cleardoublepage",
            r"\pagecolor{" + self.pastelcolor + r"}",
            r"\mbox{}",
            r"\vfill",
            r"\begin{flushright}",
            r"\pagenumbering{gobble}",
            r" ",
            "meow " * random.randint(3, 8),
            r" ",
            r"\end{flushright}",
            r"\end{document}"
        ]

        return "\n".join(end)

    @staticmethod
    def meow_paragraph(minlength: int, maxlength: int):
        """max and min length as `meow ` count"""
        return "M" + ("meow " * random.randint(minlength, maxlength))[1:] + "."

    def latex_render(self):
        # os.system("ls")
        print("render it yourself")

    def cleanup(self):
        # os.remove(self.tex_file_name)
        pass


if __name__ == "__main__":
    meow().main()
