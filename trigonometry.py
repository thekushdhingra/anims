from manim import *

config.pixel_height = 1280
config.pixel_width = 720

class Trigonometry(Scene):
    def construct(self):
        A = UP * 4 + RIGHT * 3
        B = RIGHT * 3
        C = LEFT * 3
        AB = Line(A, B, color=YELLOW)
        BC = Line(B, C, color=BLUE)
        CA = Line(C, A, color=RED)
        right_angle = RightAngle(AB, BC, 0.7, quadrant=(-1, 1))
        theta_angle = Angle(BC, CA, 1.1, quadrant=(-1, 1))

        labels = [
            (r"\theta", LEFT * 1.9 + UP * 0.45, RIGHT),
            ("A", A, UP),
            ("B", B, RIGHT),
            ("C", C, LEFT),
            ("Perpendicular", AB, RIGHT),
            ("Base", BC, DOWN),
            ("Hypotenuse", (UP * 2.1 + RIGHT * 0.9), UP + DOWN),
        ]

        label_objs = []
        for label_text, label_point, label_pos in labels:
            if label_text == "Hypotenuse":
                label = MathTex(label_text, font_size=50).next_to(label_point, label_pos).rotate_about_origin(0.6)
            else:
                label = MathTex(label_text, font_size=50).next_to(label_point, label_pos)
            label_objs.append(label)

        diagram = VGroup(AB, BC, CA, right_angle, theta_angle, *label_objs)
        heading = Text("Trigonometry", color="#ff2c92", font_size=60).next_to(UP * 5, UP)

        # Helper to add math lines
        lines: list[MathTex] = []
        prev_line: MathTex | None = None
        def add_line(line: str):
            nonlocal prev_line
            line_obj = MathTex(line, font_size=50, color=WHITE)
            if prev_line:
                line_obj.next_to(prev_line, DOWN*1.5)
            else:
                line_obj.next_to(BC, DOWN * 6)
            prev_line = line_obj
            lines.append(line_obj)
            self.play(Write(line_obj))
            
        def change_line(line_num: int, new_text: str, wait_time: float = 1.0):
            if line_num < 0 or line_num >= len(lines):
                raise ValueError(f"Invalid line index: {line_num}")

            self.wait(wait_time)

            # Get current text
            old_line = lines[line_num]

            # Create new text in the same position
            new_line = MathTex(new_text, font_size=50, color=WHITE)
            new_line.move_to(old_line)

            # Fade out old and write new
            self.play(FadeOut(old_line))
            self.play(Write(new_line))

            # Update list reference
            lines[line_num] = new_line



            

        # Draw diagram
        self.play(Create(AB), Create(BC), Create(CA), Write(heading))
        self.play(Create(right_angle), Create(theta_angle), heading.animate.shift(UP * 5), run_time=0.5)

        for label in label_objs:
            self.play(Create(label), run_time=0.8)
        self.play(diagram.animate.shift(UP * 5))

        
        add_line(r"\sin(\theta) = \frac{P}{H}")
        add_line(r"\cos(\theta) = \frac{B}{H}")
        add_line(r"\tan(\theta) = \frac{P}{B}")
        add_line(r"\cot(\theta) = \frac{B}{P}")
        add_line(r"\sec(\theta) = \frac{H}{B}")
        add_line(r"\csc(\theta) = \frac{H}{P}")

        ratio_lines = VGroup(*lines)
        self.wait(1)

        
        self.play(FadeOut(ratio_lines))
        self.wait(0.5)

        
        lines.clear()
        prev_line = None
        add_line(r"P^2 + B^2 = H^2 [\text{Pythagoras theorem}]")
        change_line(0, r"\frac{P^2}{H^2} + \frac{B^2}{H^2} = \frac{H^2}{H^2}")
        change_line(0, r"\frac{P^2}{H^2} + \frac{B^2}{H^2} = 1")
        change_line(0, r"\left(\frac{P}{H}\right)^2 + \left(\frac{B}{H}\right)^2 = 1")
        change_line(0, r"\sin^2(\theta) + \cos^2(\theta) = 1")
        
        add_line(r"\sec^2(\theta)-\tan^2(\theta)")
        change_line(1, r"\frac{1}{\cos^2(\theta)}-\frac{\sin^2(\theta)}{\cos^2(\theta)}")
        change_line(1, r"\frac{1 - \sin^2(\theta)}{\cos^2(\theta)}")
        change_line(1, r"\frac{\cos^2(\theta)}{\cos^2(\theta)} = 1")
        change_line(1, r"\sec^2(\theta)-\tan^2(\theta) = 1")
        
        add_line(r"\csc^2(\theta)-\cot^2(\theta)")
        change_line(2, r"\frac{1}{\sin^2(\theta)}-\frac{cos^2(\theta)}{\sin^2(\theta)}")
        change_line(2, r"\frac{1-cos^2(\theta)}{\sin^2(\theta)}")
        change_line(2, r"\frac{sin^2(\theta)}{\sin^2(\theta)} = 1")
        change_line(2, r"\csc^2(\theta)-\cot^2(\theta) = 1")
        rect = SurroundingRectangle(*lines, color=YELLOW, buff=0.4)
        self.play(Create(rect))
        self.wait(2)
