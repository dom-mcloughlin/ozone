import numpy as np
import os

from matplotlib import pyplot as plt


def add_spines_to_axes(ax, c, thickness=5):
    for spine in ax.spines.values():
        spine.set_color(c)
        spine.set_linewidth(thickness)
    return


def save_figure(path, fc=None):
    print("Saving plot: ", path)
    root, extension = os.path.splitext(path)
    assert(extension == ".png")
    path2 = root + ".pdf"
    fig = plt.gcf()
    if fc is None:
        fc = fig.get_facecolor()
    plt.savefig(
        path, bbox_inches='tight', dpi=400,
        facecolor=fc)
    plt.savefig(
        path2, bbox_inches='tight', dpi=400,
        facecolor=fc)
    return


def moving_average(a, n=2):
    ret = np.cumsum(a, dtype=float)
    ret[n:] = ret[n:] - ret[:-n]
    return ret[n - 1:] / n


def tomorrow_ozone_x(model, x: int):
    return
