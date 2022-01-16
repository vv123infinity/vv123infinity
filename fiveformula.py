# @Author: Aubrey
# @Date: 2022/1/16
from manim import *
class FiveFormula(Scene):
    def construct(self):
        r1 = self.cover()      # cover
        self.f1(r1)     # Eular's formula
        self.f2()       # The Pythagorean Theorem
        self.f3()        # Squared triangular number
        self.f4()         # Plot (sin(1.1x)+sin(x)+sin(0.9x))^{2}
        # self.f5dot1()
        self.f5()        # The Explicit Formula for the Fibonacci Sequence

    def cover(self):
        # 5 interesting mathematical formulas
        five_f = Text("5 interesting mathematical formulas", font="Century").set_color_by_gradient(WHITE, "#FFE4E1","#FFC1C1", "#EEB4B4",)
        self.play(Write(five_f), run_time=2.5)
        return five_f

    def f1(self, pre_f):
        text = Text("Euler's formula", font="Consolas", font_size=95,
                    t2c={"Euler's formula": "#EEB4B4"})
        self.play(FadeTransform(pre_f, text, stretch=True), run_time=1.5)
        self.wait(0.5)
        lines = VGroup(
            Tex("e^{ix}", "=", "cos\ x", "+", "i\ sin\ x"),
            Tex("e^{i\pi}", "+", "1", "=", "0", "\qquad where", "\ \ ", "x", "=", r"\pi"),
            font_size=50
        )
        lines.arrange(DOWN, buff=0.6)
        self.play(text.shift, UP*1.3)
        VGroup(text, lines).arrange(DOWN, buff=1)
        self.add(lines[0])
        self.play(Write(lines[0]))
        self.add(lines[1])
        self.play(Write(lines[1]))
        self.play(FadeOut(VGroup(text, lines)))
        self.wait(0.5)
        axes = Axes(
            # x-axis ranges from -1 to 10, with a default step size of 1
            x_range=(-2, 2, 1),
            # y-axis ranges from -2 to 2 with a step size of 0.5
            y_range=(-2, 2, 1),
            # The axes will be stretched so as to match the specified
            # height and width
            height=6,
            width=6,
            # Axes is made of two NumberLine mobjects.  You can specify
            # their configuration with axis_config
            axis_config={
                "stroke_color": GREY_A,
                # "stroke_width": 2,
                "include_numbers": True,
            },
            # Alternatively, you can specify configuration for just one
            # of them, like this.
            y_axis_config={
                "include_tip": False,
                # "y_axis_label": "hello",
            }

        )
        labels = axes.get_axis_labels(x_label_tex='Re', y_label_tex='Im').set_color(BLUE)
        circle = Circle(radius=1.5, color=BLUE).shift(UR * 0.1).shift(UP * 0.2).shift(RIGHT * 0.01)
        arrow_1 = Arrow(start=UR * (-0.05) + UP * 0.2 + RIGHT * 0.01, end=UR * 1.35 + UP * 0.2 + RIGHT * 0.01,
                        color=GOLD)

        helloWorld = Tex(r"\theta", font_size=30, color=GREEN).shift(UR * 0.5 + DOWN * 0.07)
        cos_theta = Tex(r"cos\ \theta", font_size=28, color=YELLOW).shift(RIGHT * 0.7 + UP * 0.02)
        sin_theta = Tex(r"sin\ \theta", font_size=28, color=YELLOW).shift(RIGHT * 1.6 + UP * 0.8)
        line = Line(RIGHT * 1.2 + UP * 0.3, RIGHT * 1.2 + UP * 1.3)

        self.play(ShowCreation(VGroup(axes, labels)))
        self.play(GrowFromCenter(circle))
        self.add(arrow_1)
        self.play(ShowCreation(arrow_1))

        self.play(FadeIn(helloWorld))
        self.wait(0.05)
        self.add(line, cos_theta, sin_theta)
        self.play(FadeIn(VGroup(cos_theta, line, sin_theta)))
        self.wait(1)
        self.play(ScaleInPlace(VGroup(axes, labels, circle, arrow_1, helloWorld, cos_theta, line, sin_theta),
                               0.6, run_time=1))
        self.play(VGroup(axes, labels, circle, arrow_1, helloWorld, cos_theta, line, sin_theta).shift,
                  UL * 1.5 + LEFT * 2.3)
        proof = VGroup(
            Tex("Verification\ \ using\ \ Taylor\ \ series", color=GREEN),
            Tex("e^{x}", "=", "1", "+", "x", "+", r"\frac{x^2}{2!}", "+", r"\frac{x^3}{3!}", "+", "..."),
            Tex("cos", "x", "=", "1", "-", r"\frac{x^2}{2!}", "+", r"\frac{x^4}{4!}", "-", r"\frac{x^6}{6!}", "+",
                "..."),
            Tex("sin", "x", "=", "x", "-", r"\frac{x^3}{3!}", "+", r"\frac{x^5}{5!}", "-", r"\frac{x^7}{7!}", "+",
                "..."),
            font_size=30
        )
        proof2 = VGroup(
            Tex("Substituting\ \ x = iz\ \ into\ \ e^{x}", color=GREEN),
            Tex("e^{x}", "=", "1", "+", "iz", "+", r"\frac{(iz)^2}{2!}", "+", r"\frac{(iz)^3}{3!}", "+",
                r"\frac{(iz)^4}{4!}", "+", "..."),
            Tex("=", "1", "+", "iz", "-", r"\frac{z^2}{2!}", "-",
                r"\frac{(iz)^3}{3!}", "+", r"\frac{z^4}{4!}", "+", "..."),
            Tex("=", "(", "1", "-", r"\frac{z^2}{2!}", "+", r"\frac{z^4}{4!}", "-", r"\frac{z^6}{6!}", "+", "...", ")"),
            Tex("+", "i", "(", "z", "-", r"\frac{z^3}{3!}", "+", r"\frac{z^5}{5!}", "-", r"\frac{z^7}{7!}", "+", "...",
                ")"),
            Tex("=", "cos", "z", "+", "i", "sin", "z"),
            font_size=25
        )
        proof.arrange(DOWN, buff=0.5)
        proof.shift(UR * 1 + RIGHT)
        self.play(FadeIn(proof))
        self.wait(2)
        self.play(FadeOut(VGroup(axes, labels, circle, arrow_1, helloWorld, cos_theta, line, sin_theta)))
        self.play(ScaleInPlace(proof, 0.6, run_time=1))
        self.play(proof.shift, LEFT * 6 + DOWN * 1)
        proof2.arrange(DOWN, buff=0.4)
        proof2.shift(UR * 0.3 + RIGHT * 2.2)
        self.play(Write(proof2), run_time=5)
        self.wait(2.5)
        self.play(FadeOut(VGroup(proof, proof2)))

    def f2(self):
        pytha_txt = Text("The Pythagorean Theorem", font="Consolas", font_size=60,
                         t2c={"The Pythagorean Theorem": "#EEB4B4"})
        self.play(Write(pytha_txt))
        self.wait(0.5)
        f2 = VGroup(
            Tex("a^2", "+", "b^2", "=", "c^2"),
            font_size=50
        )
        self.play(pytha_txt.shift, UP*0.8)
        VGroup(pytha_txt, f2).arrange(DOWN, buff=1)
        self.play(Write(f2[0]))
        self.wait(1)

        self.play(FadeOut(VGroup(pytha_txt, f2)))

        # plot graph
        intro_words = Text("a = 3  b = 4  c = 5")
        intro_words.to_edge(UP)
        grid = NumberPlane((-10, 10), (-5, 5))
        self.play(ShowCreation(grid))
        self.play(Write(intro_words), run_time=0.6)
        e1 = Line(ORIGIN, RIGHT * 4, color=RED)
        e2 = Line(RIGHT * 4, UP * 3 + RIGHT * 4, color=RED)
        e3 = Line(ORIGIN, UP * 3 + RIGHT * 4, color=RED)
        e1_txt = Text("b").shift(RIGHT * 2 + DOWN * 0.5)
        e2_txt = Text("a").shift(RIGHT * 4.5 + UP * 1.5)
        e3_txt = Text("c").shift(RIGHT * 1.8 + UP * 2)
        edge_labels = VGroup(e1_txt, e2_txt, e3_txt)
        tri3 = VGroup(e1, e2, e3)
        self.play(ShowCreation(VGroup(tri3, edge_labels)))
        self.wait(1.5)
        self.play(FadeOut(VGroup(grid, intro_words, tri3, edge_labels)), run_time=0.5)

    def f3(self):
        squared_title = Text("Squared triangular number",
                               font="Consolas", font_size=60, color="#EEB4B4", )
        self.play(Write(squared_title))
        self.wait(0.5)
        squared_formula = VGroup(
            Tex("1^3", "+", "2^3", "+", "3^3", "+", "...", "+", "n^3", "=", "(", "1", "+", "2", "+",
                "3", "+", "...", "+n", ")^2"),
            Tex("\sum_{k=1}^{n}k^3"),
            Tex("=(\sum_{k=1}^{n}k)^2"),
            Tex("\sum_{k=1}^{n}k^3"),
            Tex("=1+8+27+64+...+n^3"),
            Tex(r"=\underbrace{1}_{1^3}+\underbrace{3+5}_{2^3}+\underbrace{7+9+11}_{3^3}+...+\underbrace{(n^2-n+1)+...+(n^2+n-1)}_{n^3}"),
            Tex(r"=\underbrace{\underbrace{\underbrace{\underbrace{1}_{1^2}+3}_{2^2}+5}_{3^2}+...+(n^2+n-1)}_{(\frac{n^2+n}{2})^2}"),
            Tex("=(1+2+3+...+n^2)"),


            # Tex("where\ \ "),
            # Tex(r"\varphi", "=", r"\frac{1+\sqrt{5}}{2}"),
            font_size=55
        )
        self.play(squared_title.shift, UP*0.8)
        VGroup(squared_title, squared_formula[0]).arrange(DOWN, buff=1)
        # VGroup(squared_title, VGroup(squared_formula[1], squared_formula[2])).arrange(DOWN, buff=1)
        VGroup(squared_formula[1], squared_formula[2]).arrange(RIGHT, buff=0.1)
        self.play(Write(squared_formula[0]))
        self.wait(1)
        self.play(FadeTransform(squared_formula[0], VGroup(squared_formula[1], squared_formula[2]).shift(DOWN)))
        # VGroup(squared_formula[3], squared_formula[4]).arrange(RIGHT, buff=0.1)
        # VGroup(VGroup(squared_formula[3], squared_formula[4]), squared_formula[5:]).arrange(DOWN, buff=1)
        squared_formula[3].to_edge(UP+LEFT)
        self.wait(1)
        self.play(FadeOut(VGroup(squared_title, squared_formula[2])),
                  FadeTransform(squared_formula[1], squared_formula[3]))
        self.play(Write(squared_formula[4].to_edge(UP*1.5).shift(LEFT*1.8+DOWN*0.15)))
        self.play(Write(squared_formula[5].to_edge(UP*4+LEFT)))
        self.play(Write(squared_formula[6].to_edge(UP * 7 + LEFT)))
        self.wait(1)
        self.play(FadeOut(VGroup(squared_formula[3], squared_formula[4], squared_formula[5])))
        self.play(squared_formula[6].shift, UP*3)
        self.play(Write(squared_formula[7].to_edge(8.8*UP+LEFT)))
        self.play(Write(squared_formula[2].to_edge(10.8*UP+LEFT)))
        self.wait(1)
        self.play(FadeOut(VGroup(squared_formula[2], squared_formula[7], squared_formula[6])))

    def f4(self):
        sin_txt = Tex("(sin(1.1x)+sin(x)+sin(0.9x))^{2}", font="Consolas", font_size=90,
                    color="#EEB4B4")
        self.play(Write(sin_txt))
        self.wait(1.7)
        sin_axes = Axes((-62.83, 62.83), (0, 10))   # range
        self.play(FadeTransform(sin_txt, sin_axes, stretch=False), run_time=1)
        # plot function
        sin_graph = sin_axes.get_graph(
            lambda x: ((math.sin(1.1*x)+math.sin(x)+math.sin(0.9*x))*(math.sin(1.1*x)+math.sin(x)+math.sin(0.9*x))),
            color="#B9D3EE",
        )

        sin_l = Text("x from -62.83 to 62.83", font_size=20, color="#EEB4B4").shift(DOWN*3.3+RIGHT*3.9)   # add label
        self.play(
            ShowCreation(sin_graph),
            FadeIn(sin_l),
        )
        self.wait(2)
        self.play(FadeOut(VGroup(sin_axes, sin_graph, sin_l)), run_time=0.7)

    def f5dot1(self):
        # Plot a Fibonacci spiral
        fibo_spiral_txt = VGroup(
            Text("A Fibonacci spiral approximates the golden spiral", font_size=30).set_color_by_gradient(WHITE, "#F5F5DC","#FFE7BA", "#F5DEB3", "#CDBA96"),
            Text("using quarter-circle arcs inscribed in squares", font_size=30).set_color_by_gradient(WHITE, "#F5F5DC", "#FFE7BA", "#F5DEB3", "#CDBA96"),
            Text("derived from the Fibonacci sequence.", font_size=30).set_color_by_gradient(WHITE, "#F5F5DC", "#FFE7BA","#F5DEB3", "#CDBA96"),

        )
        VGroup(fibo_spiral_txt[0], fibo_spiral_txt[1], fibo_spiral_txt[2]).arrange(DOWN, buff=0.6)
        fibo_spiral_txt.to_edge(UP)
        self.play(FadeIn(fibo_spiral_txt))
        self.wait(1)
        fibo_spiral_txt_trans = Text("A Fibonacci spiral").set_stroke(BLACK, 10, background=True).to_edge(UP)
        grid = NumberPlane((-1, 35), (-1, 23))

        self.play(ShowCreation(grid))
        self.play(FadeTransform(fibo_spiral_txt, fibo_spiral_txt_trans, stretch=False))

        rect1 = Rectangle(width=6.8, height=4.2, color="#FFC1C1")

        # 21 * 21
        rect21 = Rectangle(width=4.2, height=4.2, color=RED).shift(1.3*LEFT)
        rect21_txt = Text("21×21", color=WHITE, font_size=28).move_to(rect21.get_center())
        rect21.set_fill(color=RED, opacity=0.2)
        part_circle1 = Sector(outer_radius=4.2, inner_radius=4.2, color="#E6E6FA").shift((1.3+2.1)*LEFT+2.1*DOWN).flip(UP)

        self.play(ShowCreation(rect1))
        # 13 * 13
        rect13 = Rectangle(width=2.6, height=2.6, color="#C1FFC1").set_fill(color="#C1FFC1", opacity=0.2).shift(2.1*RIGHT+0.79*UP)
        rect13_txt = Text("13×13", color=WHITE, font_size=23).move_to(rect13.get_center())
        part_circle2 = Sector(outer_radius=2.6, inner_radius=2.6, color=WHITE).shift(0.8*RIGHT+0.5*DOWN)

        # 8 * 8
        rect8 = Rectangle(width=1.6, height=1.6, color="#CDBA96").set_fill(color="#CDBA96", opacity=0.2).shift(
            2.6 * RIGHT + 1.3 * DOWN)
        rect8_txt = Text("8×8", color=WHITE, font_size=15).move_to(rect8.get_center())
        part_circle3 = Sector(outer_radius=1.6, inner_radius=1.6, color=WHITE).shift(2.6 * RIGHT + 1.3 * DOWN+ DL*0.8).flip(RIGHT)

        # 5 * 5
        rect5 = Rectangle(width=1, height=1, color="#9370DB").set_fill(color="#9370DB", opacity=0.2).shift(
            1.3 * RIGHT + 1.6 * DOWN)
        rect5_txt = Text("5×5", color=WHITE, font_size=12).move_to(rect5.get_center())
        part_circle4 = Sector(outer_radius=1, inner_radius=1, color=WHITE).shift(0.8 * RIGHT + 2.1 * DOWN).flip(RIGHT).flip(DOWN)

        # 3 * 3
        rect3 = Rectangle(width=0.6, height=0.6, color="#C1CDC1").set_fill(color="#C1CDC1", opacity=0.2).shift(
            1.1 * RIGHT + 0.8 * DOWN)
        part_circle5 = Sector(outer_radius=0.6, inner_radius=0.6, color=WHITE).shift(0.8 * RIGHT + 1.1 * DOWN).flip(UP)

        # 2 * 2
        rect2 = Rectangle(width=0.4, height=0.4, color="#C1CDC1").set_fill(color="#C1CDC1", opacity=0.2).shift(
            1.6 * RIGHT + 0.7 * DOWN)
        part_circle6 = Sector(outer_radius=0.4, inner_radius=0.4, color=WHITE).shift(1.4 * RIGHT + 0.9 * DOWN)

        # 1 * 1
        rect1_1 = Rectangle(width=0.2, height=0.2, color="#C1CDC1").set_fill(color="#C1CDC1", opacity=0.2).shift(
            1.7 * RIGHT + 1 * DOWN)
        part_circle7 = Sector(outer_radius=0.2, inner_radius=0.2, color=WHITE).shift(1.6 * RIGHT + 1.1 * DOWN).flip(RIGHT)

        rect1_2 = Rectangle(width=0.2, height=0.2, color="#C1CDC1").set_fill(color="#C1CDC1", opacity=0.2).shift(
            1.5 * RIGHT + 1 * DOWN)
        part_circle8 = Sector(outer_radius=0.2, inner_radius=0.2, color=WHITE).shift(1.4 * RIGHT + 1.1 * DOWN).flip(RIGHT).flip(DOWN)
        the_first = VGroup(rect1_1, part_circle7)
        self.play(FadeIn(the_first))

        self.play(ShowCreationThenFadeOut(Text("The first square(1×1) derived\n\n from the Fibonacci sequence.", font_size=19,).set_stroke(BLACK, 10, background=True).next_to(the_first, RIGHT)))
        the_second = VGroup(rect1_2, part_circle8)
        self.play(FadeIn(the_second))
        self.play(ShowCreationThenFadeOut(Text("The second square(1×1) derived\n\n from the Fibonacci sequence.", font_size=19,).set_stroke(BLACK, 10, background=True).next_to(the_second, LEFT)))
        the_third= VGroup(rect2, part_circle6)
        self.play(FadeIn(the_third),
                  ShowCreationThenFadeOut(Text("The third square(2×2) derived\n\n from the Fibonacci sequence.",
                                               font_size=19, ).set_stroke(BLACK, 10, background=True).next_to(
                      the_third, UP), run_time=2)
                  )
        self.play(FadeIn(rect3), Write(part_circle5))
        self.play(FadeIn(VGroup(rect5, rect5_txt)),Write(part_circle4))
        self.play(FadeIn(VGroup(rect8, rect8_txt)), Write(part_circle3))
        self.play(FadeIn(VGroup(rect13, rect13_txt)), Write(part_circle2))
        self.play(FadeIn(VGroup(rect21, rect21_txt)), Write(part_circle1))
        fibo_spirals2 = Text("Golden spirals are self-similar.\n\nThe shape is infinitely repeated when magnified.", font_size=25).set_stroke(BLACK, 10, background=True).to_edge(DOWN)
        self.play(Write(fibo_spirals2))
        # FadeOut grid | text info | all graph
        self.wait(2)
        all_circle_curve = VGroup(part_circle1, part_circle2, part_circle3, part_circle4,
                                  part_circle5, part_circle6, part_circle7, part_circle8)
        all_squares = VGroup(rect21, rect13, rect8, rect5, rect3,
                             rect21_txt, rect13_txt, rect8_txt, rect5_txt,
                             rect2, rect1_1, rect1_2, rect1)
        self.play(FadeOut(VGroup(grid, fibo_spiral_txt_trans,fibo_spirals2, all_squares, all_circle_curve)))

    def f5(self):
        # The Explicit Formula for the Fibonacci Sequence
        fibonacci_title = Text("Fibonacci Sequence Formula",
                               font="Consolas", font_size=60, color="#EEB4B4",)
        self.play(Write(fibonacci_title))
        self.wait(0.5)
        fibo_formula = VGroup(
            Tex("F(n)", "=", r"\frac{(\varphi)^n-(-\frac{1}{\varphi})^n}{\sqrt{5}"),
            Tex("where\ \ "),
            Tex(r"\varphi", "=", r"\frac{1+\sqrt{5}}{2}"),
            font_size=55
        )
        self.play(fibonacci_title.shift, UP*2.2)
        VGroup(fibo_formula[1], fibo_formula[2]).arrange(RIGHT, buff=1)
        VGroup(fibo_formula[0], VGroup(fibo_formula[1], fibo_formula[2])).arrange(DOWN, buff=0.8)
        VGroup(fibonacci_title, fibo_formula).arrange(DOWN, buff=1)
        self.play(Write(fibo_formula[0]))
        self.play(Write(VGroup(fibo_formula[1], fibo_formula[2])))
        framebox1 = SurroundingRectangle(fibo_formula[2], buff=.1, color="#EEE8AA")
        gold_ratio = Text("Golden Ratio", color="#EEE8AA", font_size=26, font="Comic Sans MS")
        self.play(ShowCreation(framebox1))
        gold_ratio.next_to(framebox1, RIGHT)
        self.play(Write(gold_ratio))
        self.wait(1.5)
        fibo_seq = VGroup(
            Text("The first 21 Fibonacci numbers are:", font_size=35, font="Comic Sans MS", color="#EEE8AA", t2c={"21":RED}),
            Tex("0\ 1\ 1\ 2\ 3\	5\ 8\ 13\ 21\ 34\ 55", font_size=45),
            Tex("89\ 144\ 233\ 377\ 610\ 987\ 1597\ 2584\ 4181\ 6765",font_size=45)
        )
        VGroup(fibo_seq[0], fibo_seq[1], fibo_seq[2]).arrange(DOWN, buff=0.8)
        self.play(FadeTransform(VGroup(fibonacci_title, fibo_formula, gold_ratio, framebox1), fibo_seq, stretch=True))
        self.wait(2)
        self.play(FadeOut(fibo_seq))
        self.f5dot1()
