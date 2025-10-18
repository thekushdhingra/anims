from manim import *
from utils.line_adder import LineAdder

class GPQuestion(Scene):
    def construct(self):
        expr = MathTex(r"S=5+7+13+31+85+\dots\text{ }T_n", font_size=24)
        heading = MathTex(r"S = \text{?}", font_size=24).next_to(expr, UP)
        q = VGroup(expr, heading)
        self.play(Write(q))
        self.play(q.animate.shift(UP*3))

        sol = LineAdder(self, q, gap=DOWN, font_size=24)

        sol.add_line(r"S=0+5+7+13+31+\dots\text{ }T_n")
        sol.edit_line(0, r"-S=0+5+7+13+31+\dots\text{ }T_n")

        line = Line(
            sol.lines[0].get_bottom() + LEFT * sol.lines[0].width/2 + DOWN * 0.1,
            sol.lines[0].get_bottom() + RIGHT * sol.lines[0].width/2 + DOWN * 0.1,
            color=YELLOW
        )
        self.play(Create(line))

        # Add lines, reduce font size for multiline ones
        sol.add_line(r"0=5+2+6+18+\dots\text{ }(T_n-T_{n-1})\\-T_n", font_size=20)
        sol.add_line(r"T_n=5+2+6+18+\dots\text{ }(T_n-T_{n-1})")
        sol.add_line(r"T_n=5+\underline{2+2\times3+2\times3^2+\dots}\\\underline{(T_n-T_{n-1})}", font_size=20)
        sol.add_line(r"T_n=5+\frac{2(1-3^{n-1})}{1-3}")
        sol.edit_line(4, r"T_n=5+\frac{2(1-3^{n-1})}{-2}")
        sol.edit_line(4, r"T_n=5+3^{n-1}-1")
        sol.edit_line(4, r"T_n=4+3^{n-1}")

        sol.add_line(r"S = \sum T_n")
        sol.add_line(r"\sum T_n = \sum (4+3^{n-1})")
        sol.edit_line(6, r"\sum T_n = \sum 4+ \sum 3^{n-1}")
        sol.edit_line(6, r"\sum T_n = 4n+\frac{3^n-1}{2}")

        sol.add_line(r"S = 4n+\frac{3^n-1}{2}")
        rect = SurroundingRectangle(sol.lines[7], buff=0.1)
        self.play(Create(rect))
