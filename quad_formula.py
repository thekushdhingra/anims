from manim import *
from utils.line_adder import LineAdder
class Quadratic(Scene):
    def construct(self):
        # Write and position heading and equation
        heading = Text("Quadratic formula", font_size=35, color=PURE_GREEN, stroke_width=0).next_to(UP*3, UP)
        
        derivation = LineAdder(self, heading)
        
        # Derive
        self.play(Write(heading))
        derivation.add_line(r"ax^2+bx+c=0")
        derivation.add_line(r"\text{To Prove:-  } x=\frac{-b \pm \sqrt{b^2-4ac}}{2a}", font_size=24)
        derivation.add_line(r"ax^2+bx=-c", font_size=28)
        derivation.edit_line(2, r"\text{Divide both side by a}")
        derivation.edit_line(2, r"\frac{ax^2+bx}{a}=\frac{-c}{a}")
        derivation.edit_line(2, r"x^2+\frac{bx}{a}=\frac{-c}{a}")
        derivation.edit_line(2, r"\text{Add } \left(\frac{b}{2a}\right)^2 \text{to both sides}")
        derivation.edit_line(2, r"x^2+\frac{bx}{a}+\left(\frac{b}{2a}\right)^2=\left(\frac{b}{2a}\right)^2-\frac{c}{a}")
        derivation.edit_line(2, r"\left(x+\frac{b}{2a}\right)^2=\left(\frac{b}{2a}\right)^2-\frac{c}{a}")
        derivation.edit_line(2, r"\left(x+\frac{b}{2a}\right)^2=\frac{b^2}{4a^2}-\frac{c}{a}")
        derivation.edit_line(2, r"\left(x+\frac{b}{2a}\right)^2=\frac{b^2-4ac}{4a^2}")
        derivation.edit_line(2, r"\sqrt{\left(x+\frac{b}{2a}\right)^2}=\sqrt{\frac{b^2-4ac}{4a^2}}")
        derivation.edit_line(2, r"x+\frac{b}{2a}=\sqrt{\frac{b^2-4ac}{4a^2}}")
        derivation.edit_line(2, r"x+\frac{b}{2a}=\pm\frac{\sqrt{b^2-4ac}}{2a}")
        derivation.edit_line(2, r"x=-\frac{b}{2a}\pm\frac{\sqrt{b^2-4ac}}{2a}")
        derivation.edit_line(2, r"x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}")
        rect = SurroundingRectangle(derivation.lines[2], color=YELLOW, buff=0.1)
        self.play(Create(rect))
        