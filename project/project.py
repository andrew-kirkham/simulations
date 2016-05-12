#!/bin/python3
import numpy as np
import plotly
from plotly.graph_objs import Scatter, Layout
from random import random
from growth import growth
from pad import pad


def main():
    l = 10
    k = 1
    n = l ** 2
    mu = 0.5
    nu = 1
    h0 = np.zeros((l, l))
    gamma = 4
    rho = 1 + (k * np.exp((gamma / 2) * 2 - mu))

    # yes lambda is spelled wrong, but it is a reserved keyword in python
    lamda = 1 / (n * rho)
    num_tests = 10

    t = 0
    t_index = 1

    times = np.zeros((10 ** 5, 1))
    while t <= 20:
        times[t_index] = t
        t_index += 1
        temp = -np.log(random()) / (1 / lamda)
        t += temp
    times = times[:t_index]
    times = np.squeeze(times)

    avg_list = np.zeros((t_index, num_tests))
    avg_vs_gamma = np.zeros((t_index, num_tests, 1))
    rough_list = np.zeros((t_index, num_tests))
    rough_vs_gamma = np.zeros((t_index, num_tests, 1))
    mono_layer_list = np.zeros((t_index, num_tests))
    mono_layer_vs_gamma = np.zeros((t_index, num_tests, 1))
    coverage_list = np.zeros((t_index, num_tests))
    coverage_vs_gamma = np.zeros((t_index, num_tests, 1))

    for iGamma in range(1):

        for iTest in range(num_tests):
            grid = growth(t_index, h0, gamma, k, mu)
            h_pad = np.zeros((l + 2, l + 2, t_index))

            for i in range(t_index - 1):
                h_pad[:, :, i] = pad(grid[:, :, i])

            end_x = h_pad.shape[0] - 1
            end_y = h_pad.shape[1] - 1
            north = h_pad[0:end_x - 1, 1:end_y, :]
            south = h_pad[2:end_x + 1, 1:end_y, :]
            east = h_pad[1:end_x, 2:end_y + 1, :]
            west = h_pad[1:end_x, 0:end_y - 1, :]
            r = np.sum(
                np.abs(grid - north) +
                np.abs(grid - south) +
                np.abs(grid - east) +
                np.abs(grid - west), 0)
            r1 = np.sum(r, 0) / (2 * l ** 2)
            rough = np.squeeze(r1)
            rough_list[:, iTest] = np.squeeze(rough)

            grid[grid < 0] = 0
            avg_list[:, iTest] = np.squeeze(np.mean(np.mean(grid, 0), 0))
            mono_layer_list[:, iTest] = np.squeeze(np.floor((np.sum(np.sum(grid, 0), 0) / l ** 2)))
            coverage_list[:, iTest] = np.squeeze(np.sum(np.sum(grid >= nu, 0), 0 / l ** 2))

        mono_layer_vs_gamma[:, :, iGamma] = mono_layer_list
        avg_vs_gamma[:, :, iGamma] = avg_list
        rough_vs_gamma[:, :, iGamma] = rough_list
        coverage_vs_gamma[:, :, iGamma] = coverage_list

    plot(avg_vs_gamma, mono_layer_vs_gamma, rough_vs_gamma, coverage_vs_gamma, times)


def plot(avg_vs_gamma, mono_layer_vs_gamma, rough_vs_gamma, coverage_vs_gamma, times):
    # plot stuff
    avg_layer = np.mean(avg_vs_gamma[:, :, 0], 1)
    plotly.offline.plot({
        "data": [Scatter(x=times, y=avg_layer)],
        "layout": Layout(title="avg layer height vs time")
    }, filename="layer.html")

    mono_layer = np.mean(mono_layer_vs_gamma[:, :, 0], 1)
    plotly.offline.plot({
        "data": [Scatter(x=times, y=mono_layer)],
        "layout": Layout(title="number of mono layers vs time")
    }, filename="mono.html")

    rough_layer = np.mean(rough_vs_gamma[:, :, 0], 1)
    plotly.offline.plot({
        "data": [Scatter(x=times, y=rough_layer)],
        "layout": Layout(title="surface roughness vs time")
    }, filename="surface.html")

    coverage_layer = np.mean(coverage_vs_gamma[:, :, 0], 1)
    plotly.offline.plot({
        "data": [Scatter(x=times, y=coverage_layer)],
        "layout": Layout(title="step coverage vs time")
    }, filename="step.html")


if __name__ == '__main__':
    main()
