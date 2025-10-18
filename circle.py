from manim import *

config.pixel_height = 1280
config.pixel_width = 720


class CircleVid(Scene):
    def construct(self):
        # Create shapes
        circle = Circle(radius=4).set_stroke("#ff0000", 8)
        diameter = Line(circle.point_at_angle(PI), circle.point_at_angle(0)).set_stroke("#00ff00", 6)
        center = Dot(circle.get_center(), color=WHITE)

        # Create text
        d_text = MathTex(r"\text{diameter} = 2 \cdot \text{radius}", font_size=60, color="#00ff00")
        d_text.next_to(diameter, UP, buff=0.2)
        circ_text = MathTex(r"\text{Circumference}", color="#ff0000", font_size=60)
        circ_text.next_to(circle, UP, buff=0.2)

        # Group shapes and text separately
        shapes = VGroup(circle, diameter, center)
        texts = VGroup(d_text, circ_text)
        
        circ_group = VGroup(shapes, texts)

        expr = MathTex(r"\frac{\text{Circumference}}{\text{Diameter}}=\pi\approx3.14\approx\frac{22}{7}", font_size=90)
        # Animate shapes first
        self.play(Create(shapes), run_time=3)
        # Animate text with Write
        self.play(Write(texts), run_time=3)
        self.wait(2)
        self.play(Transform(circ_group, expr), run_time=1)
        self.wait(2)
