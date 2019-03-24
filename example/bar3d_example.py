# coding=utf-8
import random

from pyecharts import options as opts
from pyecharts.charts import Bar3D, Page

from example.commons import Faker

charts = []


def collect_charts(fn):
    charts.append((fn, fn.__name__))
    return fn


@collect_charts
def bar3d_base() -> Bar3D:
    data = [(i, j, random.randint(0, 12)) for i in range(6) for j in range(24)]
    c = (
        Bar3D()
        .add(
            "",
            [[d[1], d[0], d[2]] for d in data],
            xaxis3d=opts.Axis3DOpts(Faker.clock, type_="category"),
            yaxis3d=opts.Axis3DOpts(Faker.week_en, type_="category"),
            zaxis3d=opts.Axis3DOpts(type_="value"),
        )
        .set_global_opts(
            visualmap_opts=opts.VisualMapOpts(max_=20),
            title_opts=opts.TitleOpts(title="Bar3D-基本示例"),
        )
    )
    return c


Page().add(*[fn() for fn, _ in charts]).render()
