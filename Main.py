from manim import *


class DetailedSunScene(Scene):
    def construct(self):
        # Title Introduction
        title = Text("The Sun: Structure and Fusion", font_size=60, weight=ULTRABOLD)
        self.play(Write(title))
        self.wait(1)
        COLORS = {
            "purple_ring": "#DE7E9E",  # 外层粉色环形
            "blue_ring": "#62A5E2",  # 中间蓝色环形
            "green_ring": "#C7D174",  # 内层绿色环形
            "yellow_core": "#FFCD48",  # 中心左黄色
            "orange_ring": "#FF9A31",  # 中心右下橙色
            "red_ring": "#E74C40",  # 中心右上红色
            "neptune": "#686868",
            "uranus": "#cecccd",
            "saturn": "#952e46",
            "jupiter": "#d3688c",
            "mars": "#e44c47",
            "earth": "#66a3e1",
            "venus": "#c9cf79",
            "mercury": "#ff982f",

        }

        a = 0.87
        orbit_radii = [.75 * a, 1.25 * a, 1.75 * a, 2.25 * a, 2.75 * a, 3.25 * a, 3.75 * a, 4.25 * a]  # 轨道半径
        orbits = VGroup()
        sun = Circle(radius=0.3, color=YELLOW, fill_opacity=1)
        sun_text = Text("SUN", color=BLACK, font_size=20).move_to(sun.get_center())
        # sun_group = VGroup(sun, sun_text)
        for r in orbit_radii:
            orbit = Circle(radius=r, color=GRAY, stroke_opacity=0.5)
            orbits.add(orbit)
        self.play( ReplacementTransform(title, sun), FadeIn(sun_text))

        self.play(Create(orbits), run_time=2)


        m = Dot(color=COLORS["mercury"], radius=0.15).move_to(.75 * RIGHT * a)
        v = Dot(color=COLORS["venus"], radius=0.15).move_to(1.25 * LEFT * a)
        e = Dot(color=COLORS["earth"], radius=0.15).move_to(1.75 * RIGHT * a)
        ma = Dot(color=COLORS["mars"], radius=0.15).move_to(2.25 * LEFT * a)
        j = Dot(color=COLORS["jupiter"], radius=0.15).move_to(2.75 * RIGHT * a)
        s = Dot(color=COLORS["saturn"], radius=0.15).move_to(3.25 * LEFT * a)
        u = Dot(color=COLORS["uranus"], radius=0.15).move_to(3.75 * RIGHT * a)
        n = Dot(color=COLORS["neptune"], radius=0.15).move_to(4.25 * LEFT * a)
        planets = VGroup(m, v, e, j, s, u, n, ma)
        self.play(FadeIn(planets))
        # 4. 标题动画

        mercury = Text("Mercury", color=COLORS["mercury"], font_size=28).move_to(RIGHT * 6 + UP * 2.75)
        mercury_text = Text("Closest planet to\nthe sun", font_size=20).next_to(mercury, DOWN, buff=.2).align_to(
            mercury, RIGHT)
        earth = Text("Earth", color=COLORS["earth"], font_size=28).next_to(mercury_text, DOWN, buff=.65).align_to(
            mercury, RIGHT)
        earth_text = Text("Our home planet", font_size=20).next_to(earth, DOWN, buff=.2).align_to(mercury, RIGHT)
        jupiter = Text("Jupiter", color=COLORS["jupiter"], font_size=28).next_to(earth_text, DOWN, buff=.65).align_to(
            mercury, RIGHT)
        jupiter_text = Text("The largest moon \nin the solar system", font_size=20).next_to(jupiter, DOWN,
                                                                                            buff=.2).align_to(mercury,
                                                                                                              RIGHT)
        uranus = Text("Uranus", color=COLORS["uranus"], font_size=28).next_to(jupiter_text, DOWN, buff=.65).align_to(
            mercury, RIGHT)
        uranus_text = Text("An ice giant \nwith a bluish color", font_size=20).next_to(uranus, DOWN, buff=.2).align_to(
            mercury, RIGHT)

        venus = Text("Venus", color=COLORS["venus"], font_size=28).move_to(LEFT * 6 + UP * 2.75)
        venus_text = Text("Similar to Earth \nwith a toxic \natmosphere", font_size=20).next_to(venus, DOWN,
                                                                                                buff=.2).align_to(venus,
                                                                                                                  LEFT)
        mars = Text("Mars", color=COLORS["mars"], font_size=28).align_to(earth, DOWN).align_to(venus, LEFT)
        mars_text = Text("Known as the \nRed Planet due to \nits iron-rich soil", font_size=20).next_to(mars, DOWN,
                                                                                                        buff=.2).align_to(
            venus, LEFT)
        saturn = Text("Saturn", color=COLORS["saturn"], font_size=28).align_to(jupiter, DOWN).align_to(venus, LEFT)
        saturn_text = Text("Gas giant famous \nfor its beautiful \nring system", font_size=20).next_to(saturn, DOWN,
                                                                                                       buff=.2).align_to(
            venus, LEFT)
        neptune = Text("Neptune", color=COLORS["neptune"], font_size=28).align_to(uranus, DOWN).align_to(venus, LEFT)
        neptune_text = Text("The farthest planet \nfrom the Sun", font_size=20).next_to(neptune, DOWN,
                                                                                        buff=.2).align_to(venus, LEFT)

        self.wait(.5)
        self.play(
            ReplacementTransform(m.copy(), mercury),
            ReplacementTransform(j.copy(), jupiter),
            ReplacementTransform(ma.copy(), mars),
            ReplacementTransform(v.copy(), venus),
            ReplacementTransform(e.copy(), earth),
            ReplacementTransform(s.copy(), saturn),
            ReplacementTransform(u.copy(), uranus),
            ReplacementTransform(n.copy(), neptune),
        )

        self.wait(.5)
        self.play(FadeIn(neptune_text), FadeIn(mercury_text), FadeIn(mars_text), FadeIn(venus_text), FadeIn(saturn_text), FadeIn(uranus_text), FadeIn(earth_text), FadeIn(jupiter_text))
        self.wait(3)
        self.play(
            FadeOut(m),
            FadeOut(v),
            FadeOut(e),
            FadeOut(ma),
            FadeOut(j),
            FadeOut(s),
            FadeOut(u),
            FadeOut(n),

            FadeOut(mercury),
            FadeOut(venus),
            FadeOut(earth),
            FadeOut(mars),
            FadeOut(jupiter),
            FadeOut(sun_text),
            FadeOut(saturn),
            FadeOut(uranus),
            FadeOut(neptune),

            FadeOut(mercury_text),
            FadeOut(venus_text),
            FadeOut(earth_text),
            FadeOut(mars_text),

            FadeOut(jupiter_text),
            FadeOut(saturn_text),
            FadeOut(uranus_text),
            FadeOut(neptune_text),

            FadeOut(*orbits),
            # or individually:
            # FadeOut(orbits[0]), FadeOut(orbits[1]), ..., FadeOut(orbits[7]),
        )

        title_structure = Text("The Sun's structure", weight=BOLD).to_edge(UP)


        purple_ring =  Sector(start_angle=5/180*PI,
        angle=PI/2*3-5/180*PI,
        radius=2.1,
        color=COLORS["purple_ring"],
        fill_opacity=1,
        stroke_width=1,).move_arc_center_to(LEFT * 3.5 + DOWN*0.5)
        # purple_ring = Circle(radius=2.1, color=COLORS["pink_ring"], fill_opacity=1).move_to(LEFT*3 + DOWN*0.5) # 4.5 → 2.25
        blue_ring = Circle(radius=1.9, color=COLORS["blue_ring"], fill_opacity=1).move_to(LEFT*3.5 + DOWN*0.5)  # 4.0 → 2.0
        green_ring = Circle(radius=1.7, color=COLORS["green_ring"], fill_opacity=1).move_to(LEFT*3.5 + DOWN*0.5)  # 3.5 → 1.75
        red_ring = Circle(radius=1.5, color=COLORS["red_ring"], fill_opacity=1).move_to(LEFT*3.5 + DOWN*0.5)  # 3.0 → 1.5
        orange_ring = Circle(radius=1.0, color=COLORS["orange_ring"], fill_opacity=1).move_to(LEFT*3.5 + DOWN*0.5)  # 2.0 → 1.0
        yellow_core = Circle(radius=0.5, color=COLORS["yellow_core"], fill_opacity=1).move_to(LEFT*3.5 + DOWN*0.5)
        yellow_cor = Circle(radius=0.5, color=COLORS["yellow_core"], fill_opacity=1).move_to(LEFT*3.5 + DOWN*0.5)# 1.0 → 0.5
        yellow_ring =  Sector(start_angle=PI/2,
        angle=PI,
        radius=1.911,
        color=COLORS["yellow_core"],
        fill_opacity=1,
        stroke_width=1,).move_arc_center_to(LEFT * 3.5 + DOWN*0.5)
        the_sun = VGroup(
            purple_ring, blue_ring, green_ring, red_ring, orange_ring, yellow_core, yellow_ring
        )
        the_sun_2 = the_sun.copy()
        the_sun_simplified =  Circle(radius=2.1, color=COLORS["yellow_core"], fill_opacity=1).move_to(LEFT*3.5 + DOWN*0.5)

        self.play(ReplacementTransform(sun, the_sun_simplified), run_time=1.5)

        self.play(ReplacementTransform(the_sun_simplified, the_sun), Write(title_structure), run_time=1.5)


        core = Text("Core", color=COLORS["yellow_core"], font_size=35).move_to(UP * 2)
        core_text = Text("The place where \nnuclear fusion \nhappens", font_size=24).next_to(core, DOWN, buff=.2).align_to(core, LEFT)
        photosphere = Text("Photosphere", color=COLORS["green_ring"], font_size=35).next_to(core, RIGHT, buff=3)
        photosphere_text = Text("The visible surface of \nthe sun", font_size=24).next_to(core, DOWN, buff=.2).align_to(photosphere, LEFT)
        radiation_zone = Text("Radiation Zone", color=COLORS["orange_ring"], font_size=35).next_to(core_text, DOWN, buff=0.5).align_to(core, LEFT)
        radiation_zone_text = Text("The energy created by \nthe core diffuses \nthrough the plasma", font_size=24).next_to(radiation_zone, DOWN, buff=.2).align_to(radiation_zone, LEFT)
        chromosphere = Text("Chromosphere", color=COLORS["blue_ring"], font_size=35).next_to(radiation_zone, RIGHT, buff=3).align_to(photosphere_text, LEFT)
        chromosphere_text = Text("The layer above the \nphotosphere, where the \ndensity of plasma \ndrops dramatically", font_size=24).next_to(chromosphere, DOWN, buff=.2).align_to(chromosphere, LEFT)
        convection_zone = Text("Convection Zone", color=COLORS["red_ring"], font_size=35).next_to(radiation_zone_text, DOWN, buff=0.5).align_to(core, LEFT)
        convection_zone_text = Text("Rapid heating of plasma \ncreates currents of \nheated and cooled gas", font_size=24).next_to(convection_zone, DOWN, buff=.2).align_to(convection_zone, LEFT)
        corona = Text("Corona", color=COLORS["purple_ring"], font_size=35).next_to(convection_zone, RIGHT, buff=3).align_to(photosphere_text, LEFT)
        corona_text = Text("The Sun’s outer \natmosphere", font_size=24).next_to(corona, DOWN, buff=.2).align_to(chromosphere, LEFT)

        self.add(the_sun.copy())
        self.wait(.5)
        # self.play(Transform(yellow_core.copy(), core), Transform(green_ring.copy(), photosphere), Transform(orange_ring.copy(), radiation_zone), Transform(blue_ring.copy(), chromosphere), Transform(red_ring.copy(), convection_zone), Transform(purple_ring.copy(), corona))

        self.play(Transform(yellow_core, core), Transform(green_ring, photosphere), Transform(orange_ring, radiation_zone), Transform(blue_ring, chromosphere), Transform(red_ring, convection_zone), Transform(purple_ring, corona))
        self.play(FadeIn(core_text), FadeIn(photosphere_text), FadeIn(radiation_zone_text), FadeIn(chromosphere_text), FadeIn(convection_zone_text), FadeIn(corona_text))
        self.wait(3)

        group = VGroup(*[mob for mob in self.mobjects if isinstance(mob, VMobject) and mob != yellow_cor])
        # self.play( *[FadeOut(mob) for mob in self.mobjects])
        self.add(yellow_cor)
        title_fusion = Text("Fusion", weight=BOLD).to_edge(UP)
        mechanism = Text("3 Steps", font_size=60).move_to(ORIGIN)
        # self.add(group)
        yellow = Circle(radius=2.1, color=COLORS["yellow_core"], fill_opacity=1).move_to(ORIGIN)
        # self.play(ReplacementTransform(yellow_cor, yellow), run_time=1.5)
        self.play(Transform(group, title_fusion), run_time=1.5)
        self.play(ReplacementTransform(yellow_cor, yellow), run_time=1.5)
        self.play(ReplacementTransform(yellow, mechanism))
        self.wait(3)
        step_1= Text("Step 1", font_size=40).move_to(LEFT*3+UP*1.5)
        step_1_formula = Tex(r"$\quad {}^1\mathrm{H} + {}^1\mathrm{H} \rightarrow {}^2\mathrm{H} + e^+ + \nu_e$", font_size=30).next_to(step_1, DOWN, buff=.02).move_to(+UP*.5)
        step_1_text = Text("Two protons fuse, and one turns \ninto a neutron, forming deuterium \nwhile releasing a positron and a \nneutrino.", font_size=30).next_to(step_1_formula, DOWN, buff=.2).align_to(step_1_formula, LEFT).move_to(DOWN*.8+RIGHT*1.42)
        step_2 = Text("Step 2", font_size=40).move_to(LEFT * 3 + UP * 1.5)
        step_2_formula = Tex(r"$\quad {}^2\mathrm{H} + {}^1\mathrm{H} \rightarrow {}^3\mathrm{He} + \gamma$",
                             font_size=30).next_to(step_2, DOWN, buff=.02).move_to(+UP * .5)
        step_2_text = Text(
            "The deuterium nucleus fuses with \nanother proton to form helium-3 \nand emits a gamma-ray photon.",
            font_size=30).next_to(step_2_formula, DOWN, buff=.2).align_to(step_2_formula, LEFT).move_to(
            DOWN * .6 + RIGHT * 1.8)
        step_3 = Text("Step 3", font_size=40).move_to(LEFT * 3 + UP * 1.5)
        step_3_formula = Tex(r"$\quad {}^3\mathrm{He} + {}^3\mathrm{He} \rightarrow {}^4\mathrm{He} + 2\,{}^1\mathrm{H}$",
                             font_size=30).next_to(step_2, DOWN, buff=.02).move_to(+UP * .5)
        step_3_text = Text(
            "Two helium-3 nuclei fuse to create \nhelium-4 and release two protons.",
            font_size=30).next_to(step_3_formula, DOWN, buff=.2).align_to(step_3_formula, LEFT).move_to(
            DOWN * .5 + RIGHT * 1.45)
        overall = Text("Overall", font_size=40).move_to(LEFT * 3 + UP * 1.5)
        overall_formula = Tex(r"$\quad 4\,{}^1\mathrm{H} \rightarrow {}^4\mathrm{He} + 2e^+ + 2\nu_e + \text{energy}$",
                             font_size=30).next_to(step_2, DOWN, buff=.02).move_to(+UP * .5)
        overall_text = Text(
            "The fusion converts four \nhydrogen nuclei into one \nhelium-4 nucleus, releasing \nenergy due to the  mass \ndifference.",
            font_size=30).next_to(step_3_formula, DOWN, buff=.2).align_to(step_3_formula, LEFT).move_to(
            DOWN * 1 + RIGHT*0.3)
        self.play(ReplacementTransform(mechanism, step_1))
        self.play(ReplacementTransform(step_1.copy(), step_1_formula))
        self.play(Write(step_1_text))
        self.wait(3)
        step_1_group = VGroup(step_1, step_1_formula, step_1_text)
        self.play(ReplacementTransform(step_1_group, step_2), run_time=1.5)
        self.play(ReplacementTransform(step_2.copy(), step_2_formula))
        self.play(Write(step_2_text))
        self.wait(3)
        step_2_group = VGroup(step_2, step_2_formula, step_2_text)
        self.play(ReplacementTransform(step_2_group, step_3), run_time=1.5)
        self.play(ReplacementTransform(step_3.copy(), step_3_formula))
        self.play(Write(step_3_text))
        self.wait(3)
        step_3_group = VGroup(step_3, step_3_formula, step_3_text)
        self.play(ReplacementTransform(step_3_group, overall), run_time=1.5)
        self.play(ReplacementTransform(overall.copy(), overall_formula))
        self.play(Write(overall_text))
        self.wait(3)
        end_group = VGroup(*[mob for mob in self.mobjects if isinstance(mob, VMobject)])
        end_1 = Text("THE END", font_size=60, weight=ULTRABOLD)
        end_2 = Text("THANKS FOR WATCHING!", font_size=60, weight=ULTRABOLD)
        END = VGroup(end_1, end_2).arrange(DOWN, aligned_edge=ORIGIN)
        self.play(Transform(end_group, END))
        # neptune_text = VGroup(
        #     Text("Neptune", color=BLACK, font_size=28),
        #     Text("Neptune is the farthest planet from the Sun", font_size=20)
        # ).arrange(DOWN, buff=0.2).to_edge(LEFT, buff=1).align_to(title, DOWN)
        #
        # # 天王星文字
        # uranus_text = VGroup(
        #     Text("Uranus", color=GRAY, font_size=28),
        #     Text("Uranus is the seventh planet from the Sun", font_size=20)
        # ).arrange(DOWN, buff=0.2).to_edge(LEFT, buff=1).align_to(title, DOWN)
        #
        # # 土星文字（调整位置）
        # saturn_text = VGroup(
        #     Text("Saturn", color=BLUE, font_size=28),
        #     Text("Saturn is composed of hydrogen and helium", font_size=20)
        # ).arrange(DOWN, buff=0.2).to_edge(LEFT, buff=1).align_to(uranus_text, DOWN).shift(UP * 0.5)
        #
        # # 左侧文字动画
        # self.play(
        #     Write(mercury_text),
        #     Write(uranus_text),
        #     Write(saturn_text),
        #     Write(neptune_text),
        #     run_time=1.5
        # )
        #
        # # 6. 右侧文字（金星、地球、火星、木星）
        # # 金星文字
        # venus_text = VGroup(
        #     Text("Venus", color=GREEN, font_size=28),
        #     Text("Venus is the second planet from the Sun", font_size=20)
        # ).arrange(DOWN, buff=0.2).to_edge(RIGHT, buff=1).align_to(title, DOWN)
        #
        # # 地球文字
        # earth_text = VGroup(
        #     Text("Earth", color=BLUE, font_size=28),
        #     Text("Earth is the only planet that harbors life", font_size=20)
        # ).arrange(DOWN, buff=0.2).to_edge(RIGHT, buff=1).align_to(title, DOWN)
        #
        # # 火星文字
        # mars_text = VGroup(
        #     Text("Mars", color=RED, font_size=28),
        #     Text("Despite being red, Mars is a very cold place", font_size=20)
        # ).arrange(DOWN, buff=0.2).to_edge(RIGHT, buff=1).align_to(earth_text, DOWN)
        #
        # # 木星文字（调整位置）
        # jupiter_text = VGroup(
        #     Text("Jupiter", color=PINK, font_size=28),
        #     Text("Jupiter is the fifth planet from the Sun", font_size=20)
        # ).arrange(DOWN, buff=0.2).to_edge(RIGHT, buff=1).align_to(mars_text, DOWN).shift(UP * 0.5)
        #
        # # 右侧文字动画
        # self.play(
        #     Write(venus_text),
        #     Write(earth_text),
        #     Write(mars_text),
        #     Write(jupiter_text),
        #     run_time=1.5
        # )

        self.wait(5)  # 停留展示最终效果
        # Add labels with explanations (placed outside with arrows to avoid overlap)
        # def labeled_arrow(text, start_point, end_point, color):
        #     label = Text(text, font_size=28, color=color).next_to(end_point, RIGHT)
        #     arrow = Arrow(start_point, end_point, buff=0.05, color=color)
        #     return VGroup(arrow, label)
        #
        # core_label = labeled_arrow("Core: Fusion occurs here", [3,0,0], core.get_center(), RED)
        # rad_label = labeled_arrow("Radiative Zone: Energy radiates out slowly", [3, -0.5, 0], [0,0,0], ORANGE)
        # conv_label = labeled_arrow("Convective Zone: Hot plasma circulates", [3, -1, 0], [0,0,0], YELLOW)
        # photo_label = labeled_arrow("Photosphere: Visible surface", [-3, 0, 0], photosphere.get_center(), WHITE)
        # chromo_label = labeled_arrow("Chromosphere: Reddish glow", [-3, 0.5, 0], chromosphere.get_center(), PINK)
        # corona_label = labeled_arrow("Corona: Outer atmosphere", [-3, 1, 0], corona.get_center(), BLUE)
        #
        # for label in [core_label, rad_label, conv_label, photo_label, chromo_label, corona_label]:
        #     self.play(FadeIn(label), run_time=0.8)
        #
        # self.wait(1)
        #
        # # Show Fusion Explanation
        # fusion_title = Text("How the Sun Generates Energy", font_size=48).next_to(title, DOWN, buff=0.5)
        # self.play(Write(fusion_title))
        # self.wait(1)
        #
        # # Fusion explanation and equation
        # fusion_eq = MathTex(
        #     "4\\,{}^1\\mathrm{H} \\rightarrow {}^4\\mathrm{He} + 2e^+ + 2\\nu_e + \\text{energy}",
        #     font_size=44
        # ).next_to(fusion_title, DOWN, buff=0.5)
        #
        # fusion_text = Text("Hydrogen nuclei fuse into helium,\nreleasing energy as light and heat.", font_size=32)
        # fusion_text.next_to(fusion_eq, DOWN)
        #
        # self.play(Write(fusion_eq))
        # self.play(FadeIn(fusion_text))
        # self.wait(2)
        #
        # # End with summary
        # summary = Text("The Sun powers life on Earth through nuclear fusion in its core.", font_size=36)
        # summary.to_edge(DOWN)
        # self.play(Write(summary))
        # self.wait(3)
        #
        # self.play(FadeOut(Group(*self.mobjects)))
