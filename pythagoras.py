from manim import *

config.pixel_height = 1280
config.pixel_width = 720

class PythagorasProof(Scene):
    def construct(self):
        # Create squares
        square1 = Square(8, color=BLUE)
        square2 = Square(8/(2**0.5), color=RED).rotate(PI/4)

        # Get corners
        c1 = square1.get_vertices()
        c2 = square2.get_vertices()

        # Define labels with position relative to lines
        label_data = [
            ("a", c1[0], c2[0], UP),
            ("b", c1[1], c2[0], UP),
            ("a", c1[1], c2[1], LEFT),
            ("b", c1[2], c2[1], LEFT),
            ("a", c1[2], c2[2], DOWN),
            ("b", c1[3], c2[2], DOWN),
            ("a", c1[3], c2[3], RIGHT),
            ("b", c1[0], c2[3], RIGHT),
            ("c^2", square2.get_center(), None, UP)
        ]

        labels = []
        for text, start, end, direction in label_data:
            if end is not None:
                line = Line(start, end)
                label = MathTex(text, font_size=120).next_to(line, direction)
            else:
                label = MathTex(text, font_size=120).next_to(start, direction)
            labels.append(label)

        # Group squares and labels
        diagram = VGroup(square1, square2, *labels)

        # Animate squares and labels
        self.play(Create(square1), Create(square2))
        self.play(*[Write(label) for label in labels], run_time=2)
        self.wait(1)

        # Shift diagram up to make space for derivation
        self.play(diagram.animate.shift(UP*5))
        self.wait(1)

        # Derivation lines (English + math separated)
        derivation_lines = [
            r"\text{Area(lg-square)} = (a+b)^2", 
            r"\text{Area(lg-square)} = \text{Area(triangles)} + \text{Area(square)}", 
            r"(a+b)^2 = 4 \cdot \frac{1}{2} ab + c^2",
            r"a^2 + b^2 + 2ab = 2ab + c^2",
            r"a^2 + b^2 = c^2"
        ]

        derivation_mobjects = []
        # Start writing derivation below diagram
        prev_line = None
        for line in derivation_lines:
            if prev_line is None:
                mobj = MathTex(line, font_size=60).next_to(diagram, DOWN, buff=0.7)
            else:
                mobj = MathTex(line, font_size=60).next_to(prev_line, DOWN, buff=0.4)
            self.play(Write(mobj))
            derivation_mobjects.append(mobj)
            prev_line = mobj

        # Box around the final result
        final_box = SurroundingRectangle(derivation_mobjects[-1], color=YELLOW, buff=0.2)
        self.play(Create(final_box))
        self.wait(2)
