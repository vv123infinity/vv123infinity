# @Author: Aubrey
# @Date: 2022/1/28
import math
import random
# from Manim_002.manim.manimlib.constants import TAU, YELLOW, UP, RIGHT, GOLD
from manim import *
import numpy as np


class BonusCover(Scene):
    def construct(self):
        cover = Text("Bonus Scene", font_size=60,
                     font="Consolas").set_color_by_gradient("#F0FFFF", "#C6E2FF", "#87CEFF", "#00BFFF", "#009ACD")
        self.play(Write(cover))
        self.wait(1)
        self.play(FadeOut(cover))

GRAVITY = np.array([0, 0, -0.002])


class Particle(Sphere):
    CONFIG = {
        "radius": random.random() * 0.02 + 0.04
    }

    def __init__(self, x, y, speed, r, **kwargs):
        super().__init__(**kwargs)
        self.speed = np.array([0, 0, speed])
        self.pos = np.array([x, y, 0])
        self.r = r
        self.isBoom = False
        self.isMove = True

    def draw(self):
        if not self.isMove:
            return
        # Gravity
        self.speed += GRAVITY
        if not self.isBoom and self.speed[2] <= 0:
            # Boom!
            self.isBoom = True
            a = random.random() * 2 * PI
            r = self.r * (random.random() * 0.5 + 0.5)
            self.speed += (
                    r * np.cos(a) * RIGHT +
                    r * np.sin(a) * UP
            )
        # Friction
        self.speed *= 0.98
        self.pos += self.speed

        # Bouncing
        if self.pos[2] <= 0:
            self.pos[2] = 0
            self.speed[2] *= -0.9

        # move to
        self.move_to(self.pos)

        if self.isBoom and \
                np.linalg.norm(self.speed) < 0.01:
            self.isMove = False


class Firework(Mobject):
    def __init__(self, x, y, speed, r, colors, **kargs):
        super().__init__(**kargs)
        n = math.ceil(speed * 300)
        for i in range(n):
            p = Particle(x, y, speed, r)
            p.set_color(random.choice(colors))
            self.add(p)

    def isActive(self):
        for p in self.submobjects:
            if p.isMove:
                return True
        return False

    def draw(self):
        for p in self.submobjects:
            p.draw()



class BonusScene(ThreeDScene):
    def construct(self):
        frame = self.camera.frame
        frame.focal_distance = 10
        frame.set_phi(70 * DEGREES)
        frame.add_updater(lambda m, dt: \
                              m.increment_theta(-0.1 * dt))
        self.add(frame)

        grid = NumberPlane([-20, 20, 2], [-20, 20, 2])
        self.play(ShowCreation(grid), run_time=5)
        self.wait(1)

        palettes = [
            [BLUE_A, BLUE_B, BLUE_C, BLUE_D, BLUE_E],
            [TEAL_A, TEAL_B, TEAL_C, TEAL_D, TEAL_E],
            [GREEN_A, GREEN_B, GREEN_C, GREEN_D, GREEN_E],
            [YELLOW_A, YELLOW_B, YELLOW_C, YELLOW_D, YELLOW_E],
            [GOLD_A, GOLD_B, GOLD_C, GOLD_D, GOLD_E],
            [RED_A, RED_B, RED_C, RED_D, RED_E],
            [MAROON_A, MAROON_B, MAROON_C, MAROON_D, MAROON_E],
            [PURPLE_A, PURPLE_B, PURPLE_C, PURPLE_D, PURPLE_E]
        ]

        fireworks = []
        # 欢乐过新年，烟花灿九天。
        happy_new_year = Text("2022", font_size=50, font="黑体").to_edge(UP)
        happy_new_year.set_color_by_gradient("#FFFFFF", "#FFF0F5", "#FFE4E1", "#FFB5C5", "#EEA9B8", "#CD919E")
        self.play(ShowCreation(happy_new_year))

        for i in range(18):
            if i == 2:
                text_3 = Text("新春已至，平安喜乐。", font_size=40, font="黑体").to_edge(DOWN).rotate(-TAU / 4)
                text_3.set_color_by_gradient("#FFFFE0", "#EEEED1", "#FFF68F", "#FFEC8B",)

                self.play(Write(text_3))
            if i == 5:
                text_3 = Text("欢乐过新年，烟花灿九天。", font_size=40, font="黑体").to_edge(LEFT).rotate(-TAU / 4)
                text_3.set_color_by_gradient("#C1FFC1", "#FFFFF0", "#FFBBFF",
                                             "#F5FFFA", "#FFF0F5", "#FFE4E1", "#E0FFFF", "#BBFFFF")
                self.play(Write(text_3))

            waitTime = 1.5
            firework = Firework(
                random.random() * 10 - 5,
                random.random() * 10 - 5,
                random.random() * 0.025 + 0.075,
                random.random() * 0.06 + 0.06,
                random.choice(palettes)
            )
            firework.add_updater(lambda m: m.draw())
            self.add(firework)
            fireworks.append(firework)
            if i > 25:
                f = fireworks[0]
                fireworks.remove(f)
                self.play(FadeOut(f))
                waitTime = 1.0
            self.wait(random.random() * waitTime)
