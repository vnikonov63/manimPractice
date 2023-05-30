from manim import *


class Lol(Scene):
    def get_integral(self, left, right):
        return (-left ** 4 + right ** 4 + left ** 3 - right ** 3 + left ** 2 - right ** 2)

    def construct(self):
        axes = Axes(
            x_range=[-1, 1.5, 1],
            y_range=[-0.5, 1.2, 1],
            x_length=10,
            axis_config={"color": GREEN},
            tips=False,
        )

        polynomial1_graph = axes.plot(lambda x: -x**3 + x**2 + x, color=RED)

        t1 = ValueTracker(0.3)
        t2 = ValueTracker(0.8)

        vert_line1 = axes.get_vertical_line(
            axes.i2gp(t1.get_value(), polynomial1_graph), color=YELLOW, line_func=Line
        )

        vert_line2 = axes.get_vertical_line(
            axes.i2gp(t2.get_value(), polynomial1_graph), color=YELLOW, line_func=Line
        )

        line1_label = axes.get_graph_label(
            axes.get_x_axis(), "a", x_val=t1.get_value(), direction=1.5 * DOWN, color=YELLOW
        )

        line2_label = axes.get_graph_label(
            axes.get_x_axis(), "b", x_val=t2.get_value(), direction=DOWN, color=YELLOW
        )

        area = axes.get_area(polynomial1_graph, [
                             t1.get_value(), t2.get_value()],  color=GREY, opacity=0.5)

        polynomial1_label = axes.get_graph_label(
            polynomial1_graph, label="\\-x^3 + x^2 + x",
            direction=1.5 * DOWN
        )

        plot = VGroup(axes, polynomial1_graph, polynomial1_label,
                      vert_line1, line1_label,  vert_line2, line2_label, area)

        self.play(Create(axes), run_time=1)
        self.play(Create(polynomial1_graph), run_time=2)
        self.play(Write(polynomial1_label), run_time=1)
        self.play(Create(vert_line1, run_time=1.5))
        self.play(Write(line1_label, run_time=0.5))
        self.play(Create(vert_line2, run_time=1.5))
        self.play(Write(line2_label, run_time=0.5))
        self.play(DrawBorderThenFill(area), run_time=2)
        self.play(Transform(plot, plot.copy().scale(0.5)), run_time=2)
        self.play(ApplyMethod(plot.shift, 4.5 * LEFT), run_time=2)
        self.play(FadeOut(polynomial1_label), FadeOut(
            line1_label), FadeOut(line2_label))

        title = Tex("Geometric meaning", font_size=36, color=GOLD_B)

        title.next_to(plot, direction=(UP))

        self.play(Write(title), run_time=2)
        self.wait(2)

        title1 = Tex("Calculus meaning", font_size=36, color=GOLD_B)

        title1.next_to(title, direction=19 * RIGHT)

        self.play(Write(title1), run_time=2)
        self.wait(2)

        equation = MathTex(
            r"\int_a^b -x^3 + x^2 + x \, dx =",
        )

        equation.next_to(title1, direction=DOWN)

        self.play(Write(equation), run_time=3)

        equation1 = MathTex(
            r"-\frac{x^4}{4} + \frac{x^3}{3} + \frac{x^2}{2} \Big|_a^b ="
        )

        equation1.next_to(equation, direction=DOWN)

        self.play(Write(equation1), run_time=3)

        self.wait(2)

        self.play(FadeOut(equation1))

        equation2 = MathTex(
            r"\frac{a^4 - b^4}{4} + \frac{b^3 - a^3}{3} + \frac{b^2 - a^2}{2} =",
        )

        equation2.next_to(equation, direction=DOWN)

        self.play(Write(equation2.copy().scale(0.8)), run_time=3)

        equation3 = MathTex(
            "{:.3f}".format(self.get_integral(t2.get_value(), t1.get_value()))
        )

        equation3.next_to(equation2, direction=1.5 *
                          DOWN).set_color(GREY).scale(1.4)

        equation4 = MathTex(
            "a = {:.2f}, b = {:.2f}".format(
                t1.get_value(), t2.get_value())
        )

        equation4.next_to(equation3, direction=1.5 *
                          DOWN)

        self.play(Write(equation3), Write(equation4), run_time=1)

        self.play(
            t1.animate.set_value(0.5),
            t2.animate.set_value(0.6),
            UpdateFromFunc(vert_line1, lambda line: line.become(axes.get_vertical_line(
                axes.i2gp(t1.get_value(), polynomial1_graph),
                color=YELLOW,
                line_func=Line
            ))),
            UpdateFromFunc(vert_line2, lambda line: line.become(axes.get_vertical_line(
                axes.i2gp(t2.get_value(), polynomial1_graph),
                color=YELLOW,
                line_func=Line
            ))),
            UpdateFromFunc(equation3, lambda m: m.become(MathTex("{:.3f}".format(self.get_integral(
                t2.get_value(), t1.get_value()))).next_to(equation2, direction=1.5*DOWN).set_color(BLUE_A).scale(1.4))),
            UpdateFromFunc(equation4, lambda m: m.become(MathTex("a = {:.2f}, b = {:.2f}".format(
                t1.get_value(), t2.get_value())).next_to(equation3, direction=1.5*DOWN))),
            UpdateFromFunc(area, lambda a: a.become(axes.get_area(
                polynomial1_graph, [t1.get_value(), t2.get_value()],
                color=BLUE_A, opacity=0.5
            ))),
            run_time=5
        )

        self.wait(2)

        self.play(
            t1.animate.set_value(0.1),
            t2.animate.set_value(1.2),
            UpdateFromFunc(vert_line1, lambda line: line.become(axes.get_vertical_line(
                axes.i2gp(t1.get_value(), polynomial1_graph),
                color=YELLOW,
                line_func=Line
            ))),
            UpdateFromFunc(vert_line2, lambda line: line.become(axes.get_vertical_line(
                axes.i2gp(t2.get_value(), polynomial1_graph),
                color=YELLOW,
                line_func=Line
            ))),
            UpdateFromFunc(equation3, lambda m: m.become(MathTex("{:.3f}".format(
                self.get_integral(t2.get_value(), t1.get_value())
            )).next_to(equation2, direction=1.5*DOWN).set_color(BLUE_A).scale(1.4))),
            UpdateFromFunc(equation4, lambda m: m.become(MathTex("a = {:.2f}, b = {:.2f}".format(
                t1.get_value(), t2.get_value())).next_to(equation3, direction=1.5*DOWN))),
            UpdateFromFunc(area, lambda a: a.become(axes.get_area(
                polynomial1_graph, [t1.get_value(), t2.get_value()],
                color=BLUE_A, opacity=0.5
            ))),
            run_time=3
        )
