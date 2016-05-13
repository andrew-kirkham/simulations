#!/bin/python3
import numpy as np
import plotly
from plotly.graph_objs import Scatter, Layout
from random import random
from growth import growth
from pad import pad


def main():
    test_gamma()
    test_mu()


def test_gamma():
    gamma_list = [2, 3, 4]
    avg_traces = []
    mono_traces = []
    rough_traces = []
    coverage_traces = []

    for gamma in gamma_list:
        print("gamma: ", gamma)
        [avg_plot, mono_plot, rough_plot, coverage_plot] = evaluate(gamma, .5)
        avg_traces.append(avg_plot)
        mono_traces.append(mono_plot)
        rough_traces.append(rough_plot)
        coverage_traces.append(coverage_plot)
    plot(avg_traces, mono_traces, rough_traces, coverage_traces)


def test_mu():
    mu_list = {.1, .3, .5}
    avg_traces = []
    mono_traces = []
    rough_traces = []
    coverage_traces = []
    for mu in mu_list:
        print("mu:, ", mu)
        [avg_plot, mono_plot, rough_plot, coverage_plot] = evaluate(4, mu)
        avg_traces.append(avg_plot)
        mono_traces.append(mono_plot)
        rough_traces.append(rough_plot)
        coverage_traces.append(coverage_plot)
    plot(avg_traces, mono_traces, rough_traces, coverage_traces)


def evaluate(gamma, mu):
    l = 10
    k = 1
    n = l ** 2
    nu = 1
    h0 = np.zeros((l, l))
    rho = 1 + (k * np.exp((gamma / 2) * 2 - mu))

    # yes lambda is spelled wrong, but it is a reserved keyword in python
    lamda = 1 / (n * rho)
    num_tests = 10

    t = 0
    t_index = 1

    times = np.zeros((10 ** 6, 1))
    while t <= 20:
        times[t_index] = t
        t_index += 1
        time = -np.log(random()) / (1 / lamda)
        t += time
    times = times[:t_index]
    times = np.squeeze(times)

    avg_list = np.zeros((t_index, num_tests))
    rough_list = np.zeros((t_index, num_tests))
    mono_layer_list = np.zeros((t_index, num_tests))
    coverage_list = np.zeros((t_index, num_tests))

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
        rough = np.sum(r, 0) / (2 * (l ** 2))
        rough_list[:, iTest] = np.squeeze(np.squeeze(rough))

        grid[grid < 0] = 0
        avg_list[:, iTest] = np.squeeze(np.mean(np.mean(grid, 0), 0))
        mono_layer_list[:, iTest] = np.squeeze(np.floor((np.sum(np.sum(grid, 0), 0)) / l ** 2))
        coverage_list[:, iTest] = np.squeeze(np.sum(np.sum(grid >= nu, 0), 0) / l ** 2)

    avg_plot = Scatter(x=times, y=np.mean(avg_list, 1), name="gamma = " + str(gamma) + " mu = " + str(mu))
    mono_plot = Scatter(x=times, y=np.mean(mono_layer_list, 1), name="gamma = " + str(gamma) + " mu = " + str(mu))
    rough_plot = Scatter(x=times, y=np.mean(rough_list, 1), name="gamma = " + str(gamma) + " mu = " + str(mu))
    coverage_plot = Scatter(x=times, y=np.mean(coverage_list, 1), name="gamma = " + str(gamma) + " mu = " + str(mu))
    return [avg_plot, mono_plot, rough_plot, coverage_plot]


def plot(avg_traces, mono_layer_traces, rough_traces, coverage_traces):
    # plot stuff
    plot_avg(avg_traces)
    plot_mono(mono_layer_traces)
    plot_rough(rough_traces)
    plot_coverage(coverage_traces)


def plot_avg(avg_traces):
    plotly.offline.plot({
        "data": avg_traces,
        "layout": Layout(title="Average Layer Height vs Time")
    }, filename="layer.html")


def plot_mono(mono_layer_traces):
    plotly.offline.plot({
        "data": mono_layer_traces,
        "layout": Layout(title="Number of Mono-Layers vs Time")
    }, filename="layer.html")


def plot_rough(rough_traces):
    plotly.offline.plot({
        "data": rough_traces,
        "layout": Layout(title="Surface Roughness vs Time")
    }, filename="layer.html")


def plot_coverage(coverage_traces):
    plotly.offline.plot({
        "data": coverage_traces,
        "layout": Layout(title="Step Coverage vs Time")
    }, filename="layer.html")


if __name__ == '__main__':
    main()
