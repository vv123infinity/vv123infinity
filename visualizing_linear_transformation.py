# @Author: Aubrey
# @Date: 2022/1/28
from manim import *

'''
Part 1: 2D linear transformation
        class: LinearTransformation2D
Part 2: 3D linear transformation
        class: LinearTransformation3D
'''


class Part1(Scene):
    def construct(self):
        title = Text("Visualizing linear transformations",
                               font="Consolas", font_size=48, color="#EEE9BF")
        title.set_color_by_gradient("#FFFFF0", "#FFF8DC", "#FFE4B5", "#FFDEAD", "#EEDD82")
        self.play(Write(title))
        self.wait(0.6)

        subtitle1 = Text("The definition of linear transformation",
             font="Consolas", font_size=35, color="#FFFACD").shift(UP*3)
        self.play(FadeTransform(title, subtitle1, stretch=False))
        self.wait(0.6)

        defini1 = Text("A linear transformation is a function from one vector space to another"+
                       "\nthat respects the underlying (linear) structure of each vector space."+
                       "\n\nA linear transformation is also known as a linear operator or map."+
                       "\nThe range of the transformation may be the same as the domain,"+
                       "\nand when that happens, the transformation is known as an endomorphism"+
                       "\nor, if invertible, an automorphism.\n\nThe two vector spaces must have the same underlying field."
                       ,
                       font_size=22,
                       font="Consolas",
                       color="#E0EEE0").next_to(subtitle1, DOWN*5)

        defini2 = Text("The defining characteristic of a linear transformation is that ",
                       font="Consolas", font_size=25, color="#E0EEE0").next_to(subtitle1, DOWN*6.5)
        defini3 = Tex(r"$T: V \rightarrow W:T(av_1 + bv_2) = aT(v_1) + bT(v_2)$", font_size=35).next_to(defini2, DOWN*2)

        self.play(FadeIn(defini1))
        self.wait(1)
        self.play(FadeTransform(defini1, VGroup(defini2, defini3), stretch=True))
        self.wait(2)
        self.play(FadeOut(VGroup(defini2, defini3, subtitle1)))

        title2 = Text("Visualizing 2D transformations",
                     font="Consolas", font_size=48, color="#EEE9BF")
        self.play(Write(title2))
        text = Text("Transformation in Euclidean geometry",
                    font="Consolas", font_size=45,
                    t2c={"Transformation in Euclidean geometry": "#FFFFF0"})
        text.shift(UP * 1.4)
        formula1 = Tex(
            r"$Rotate(\theta)=\begin{bmatrix}cos\theta && -sin\theta\\ sin\theta && cos\theta \end{bmatrix}v$",
            color="#FFFFE0")
        formula1.next_to(text, DOWN * 2.9)
        self.play(FadeTransform(title2, VGroup(text, formula1), stretch=False))
        self.wait(2)


class LinearTransformation2D(LinearTransformationScene):
    '''
    Transformation in Euclidean geometry
    '''
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=True,
            leave_ghost_vectors=False,
            i_hat_color="#FF8C69",
            j_hat_color="#CAFF70",
        )

    def construct(self):
        self.wait(0.5)
        formula_group = VGroup(
            Tex(r"$Rotate(\theta)=\begin{bmatrix}cos\ \theta && -sin\ \theta\\ sin\ \theta && cos\ \theta \end{bmatrix}v$",
                 font_size=33, color="#EEDD82").set_stroke(BLACK, 10, background=True),
            Tex(r"$\theta = \frac{\pi}{3}$",
                color="#EEDD82", font_size=37).set_stroke(BLACK, 10, background=True),
            Tex(r"$v=\begin{bmatrix}1&&0\\0&&1\end{bmatrix}$",
                color="#EEDD82", font_size=33).set_stroke(BLACK, 10, background=True),
        )
        formula_group[0].shift(UL*3+LEFT)
        formula_group[1].next_to(formula_group[0], DOWN*1.5)
        formula_group[1].shift(LEFT*1.8)
        formula_group[2].next_to(formula_group[1], RIGHT*1.5)
        self.play(FadeIn(formula_group))
        rect = SurroundingRectangle(formula_group[1], buff=.1, color="#EEE8AA")
        text2 = VGroup(
            Tex(r"$\theta$", font_size=30, color="#EEDD82").set_stroke(BLACK, 10, background=True),
            Text("can also be", font_size=25, font="Consolas", color="#EEDD82").set_stroke(BLACK, 10, background=True),
            Tex(r"$\frac{\pi}{6},\ \frac{\pi}{4},\ \frac{\pi}{2},\ ...$", font_size=30, color="#EEDD82").set_stroke(BLACK, 10, background=True),
        )
        VGroup(text2[0], text2[1], text2[2]).arrange(RIGHT, buff=0.25)
        text2.next_to(rect, DOWN*1.5+RIGHT*1.5)
        self.play(Write(VGroup(rect, text2)))
        self.play(FadeOut(VGroup(rect, text2)))
        self.wait(1)
        theta = np.pi / 3
        matrix = [[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]]
        self.apply_matrix(matrix)
        self.wait(2)
        inv_text = VGroup(
            Text("Apply the inverse matrix on the\n\nbasis of the existing coordinate system",
                 font_size=23, font="Consolas", color="#EEDD82").set_stroke(BLACK, 10, background=True),
            Tex(r"$Rotate'(\theta)=\begin{bmatrix}cos\frac{\pi}{3} && -sin\frac{\pi}{3}\\ sin\frac{\pi}{3} && cos\frac{\pi}{3} \end{bmatrix}^{-1}\begin{bmatrix}cos\frac{\pi}{3} && -sin\frac{\pi}{3}\\ sin\frac{\pi}{3} && cos\frac{\pi}{3} \end{bmatrix}v=v$",
                font_size=30, color="#EEDD82").set_stroke(BLACK, 5, background=True),
        )
        inv_text[0].shift(UL*2+UP)
        inv_text[1].next_to(inv_text[0], DOWN*1.3)
        # VGroup(inv_text[0], inv_text[1]).arrange(DOWN, buff=0.7)
        self.play(FadeTransform(formula_group, inv_text))
        self.wait(0.6)
        self.apply_inverse(matrix)
        self.wait(2)

        # A type of transformation that occurs when a figure is enlarged or reduced, the transformation is called a dilation
        dilation_text = VGroup(
            Text("Apply a dilation, which is a type of transformation\n\nthat occurs when a figure is enlarged or reduced",
                 font_size=20, font="Consolas", color="#EEDD82").set_stroke(BLACK, 10, background=True),
            Tex(
                r"$A=\begin{bmatrix}2.5&&0\\0&&2.5\end{bmatrix}\qquad v=\begin{bmatrix}1&&0\\0&&1\end{bmatrix}$",
                font_size=30, color="#EEDD82").set_stroke(BLACK, 5, background=True),
        )
        dilation_text[0].shift(UP*3+LEFT*3)
        dilation_text[1].next_to(dilation_text[0], DOWN*1.3)
        self.play(FadeTransform(inv_text, dilation_text))
        matrix2 = [[2.5, 0], [0, 2.5]]
        self.wait(0.6)
        self.apply_matrix(matrix2)
        self.wait(2)
        dilation_inv = Tex(
            r"$A^{-1}=\begin{bmatrix}0.4&&0\\0&&0.4\end{bmatrix}$",
            font_size=30, color="#EEDD82").set_stroke(BLACK, 5, background=True)
        dilation_inv_text = Text("Apply the inverse matrix",
                                 font_size=20, font="Consolas", color="#FF6A6A").set_stroke(BLACK, 10, background=True)
        dilation_inv_text.shift(LEFT*5+UP)
        dilation_inv.next_to(dilation_inv_text, RIGHT)
        self.play(Write(VGroup(dilation_inv_text, dilation_inv)))
        self.wait(0.6)
        self.apply_inverse(matrix2)
        self.wait(2)

        d_r_text = VGroup(
            Text(
                "Apply rotation and dilation",
                font_size=20, font="Consolas", color="#EEDD82").set_stroke(BLACK, 10, background=True),
            Tex(
                r"$A=\begin{bmatrix}1.25&&-2.16\\2.16&&1.25\end{bmatrix}\qquad v=\begin{bmatrix}1&&0\\0&&1\end{bmatrix}$",
                font_size=30, color="#EEDD82").set_stroke(BLACK, 5, background=True),
        )
        d_r_text[0].shift(UP * 3.5 + LEFT * 3.3)
        d_r_text[1].next_to(d_r_text[0], DOWN * 1.3)
        self.play(FadeTransform(VGroup(dilation_text, VGroup(dilation_inv, dilation_inv_text)), d_r_text))
        self.wait(0.6)
        matrix3 = [[1.25, -2.16506351], [2.16506351, 1.25]]
        self.apply_matrix(matrix3)
        self.wait(2)
        d_r_inv = Text("Apply the inverse matrix of A",
                       font_size=20, font="Consolas", color="#FF6A6A").set_stroke(BLACK, 10, background=True)
        d_r_inv.next_to(d_r_text[1], DOWN)
        self.play(Write(d_r_inv))
        self.wait(0.5)
        self.apply_inverse(matrix3)
        self.wait(2)


class Part2(Scene):
    def construct(self):
        # title1 #EEE9BF
        # title2 #FFFACD   	#FFFFF0
        title = Text("Visualizing 3D transformation",
                               font="Consolas", font_size=48, color="#EEE9BF")
        self.play(Write(title))
        self.play(FadeOut(title))
        formulas = VGroup(
            Tex(r"$T:\ \mathbb{R}^3\to \mathbb{R}^3$"),
            Tex(r"$T\begin{bmatrix}x\\y\\z\end{bmatrix}=AI_3$"),
            Tex(r"$where\ \ A=\begin{bmatrix}2&&2&&-1\\-2&&1&&2\\3&&1&&0\end{bmatrix},I_3=\begin{bmatrix}1&&0&&0\\0&&1&&0\\0&&0&&1\end{bmatrix}$")
        )
        VGroup(formulas[0], formulas[1], formulas[2]).arrange(DOWN, buff=1)
        self.play(Write(formulas))
        self.wait(1)


class LinearTransformation3D(ThreeDScene):

    CONFIG = {
        "x_axis_label": "$x$",
        "y_axis_label": "$y$",
        # "basis_i_color": GREEN,
        # "basis_j_color": RED,
        # "basis_k_color": GOLD
    }

    def create_matrix(self, np_matrix):

        m = Matrix(np_matrix)

        m.scale(0.5)
        m.set_column_colors("#FAF0E6", "#7FFFD4", "#87CEFF")

        m.to_corner(UP + LEFT)

        return m

    def construct(self):

        M = np.array([
            [2, 2, -1],
            [-2, 1, 2],
            [3, 1, -0]
        ])

        axes = ThreeDAxes()
        # 	#B4CDCD
        axes.set_color(GRAY)
        axes.add(axes.get_axis_labels())

        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)

        # basis vectors i,j,k
        basis_vector_helper = Tex("$i$", ",", "$j$", ",", "$k$")
        basis_vector_helper[0].set_color("#FAF0E6")
        basis_vector_helper[2].set_color("#7FFFD4")
        basis_vector_helper[4].set_color("#87CEFF")

        basis_vector_helper.to_corner(UP + RIGHT)

        self.add_fixed_in_frame_mobjects(basis_vector_helper)

        # matrix
        matrix = self.create_matrix(M)

        self.add_fixed_in_frame_mobjects(matrix)

        # axes & camera
        self.add(axes)

        self.begin_ambient_camera_rotation(rate=0.2)

        cube = Cube(side_length=1, fill_color=BLUE, stroke_width=2, fill_opacity=0.1)
        cube.set_stroke(BLUE_E)

        i_vec = Vector(np.array([1, 0, 0]), color="#8B658B")
        j_vec = Vector(np.array([0, 1, 0]), color="#EEB4B4")
        k_vec = Vector(np.array([0, 0, 1]), color="#EEDD82")

        i_vec_new = Vector(M @ np.array([1, 0, 0]), color="#9400D3")
        j_vec_new = Vector(M @ np.array([0, 1, 0]), color="#CD5555")
        k_vec_new = Vector(M @ np.array([0, 0, 1]), color="#DAA520")
        # self.add(cube)
        self.play(
            # ShowCreation(cube),
            Create(cube),
            GrowArrow(i_vec),
            GrowArrow(j_vec),
            GrowArrow(k_vec),
            Write(basis_vector_helper)
        )

        self.wait()

        matrix_anim = ApplyMatrix(M, cube)

        self.play(
            matrix_anim,
            Transform(i_vec, i_vec_new, rate_func=matrix_anim.get_rate_func(),
                      run_time=matrix_anim.get_run_time()),
            Transform(j_vec, j_vec_new, rate_func=matrix_anim.get_rate_func(),
                      run_time=matrix_anim.get_run_time()),
            Transform(k_vec, k_vec_new, rate_func=matrix_anim.get_rate_func(),
                      run_time=matrix_anim.get_run_time())
        )

        self.wait()

        self.wait(7)

