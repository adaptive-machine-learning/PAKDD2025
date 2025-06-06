from typing import Dict, Optional, Tuple

import pandas as pd
from capymoa.ocl.evaluation import OCLMetrics
from matplotlib import pyplot as plt
from matplotlib.axes import Axes
from matplotlib.figure import Figure, SubFigure

plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = ["Noto Sans"]
plt.rcParams["font.size"] = 9
pt = 1 / 72.27
figsize_169 = (455 * pt, 256 * pt)
figsize = (figsize_169[0], 0.45 * figsize_169[0])


def table(metrics: Dict[str, OCLMetrics]) -> pd.DataFrame:
    rows = []
    for name, m in metrics.items():
        rows.append(
            {
                "name": name,
                "Final Accuracy": m.accuracy_final * 100,
                "Average Accuracy": m.accuracy_seen_avg * 100,
                "Online Accuracy": m.ttt.cumulative.accuracy(),
                "CPU Time (s)": m.ttt.cpu_time(),
            }
        )
    return pd.DataFrame(rows).round(1)


def plot_multiple(
    metrics: Dict[str, OCLMetrics],
    ax: Optional[Axes] = None,
    acc_online: bool = False,
    acc_all: bool = False,
    acc_seen: bool = False,
) -> Tuple[Optional[Figure | SubFigure], Axes]:
    if ax is None:
        _, ax = plt.subplots(figsize=figsize)

    cmap = plt.get_cmap("tab10")
    for i, (name, m) in enumerate(metrics.items()):
        color = cmap(i)
        if acc_all:
            ax.plot(
                m.anytime_task_index,
                m.anytime_accuracy_all * 100,
                "--",
                color=color,
                label=f"{name} (all)",
            )
            ax.scatter(
                m.task_index,
                100 * m.accuracy_all,
                color=color,
                s=20,
            )

        if acc_seen:
            ax.plot(
                m.anytime_task_index,
                m.anytime_accuracy_seen * 100,
                "-",
                color=color,
                label=f"{name}",
            )
            ax.scatter(
                m.task_index,
                100 * m.accuracy_seen,
                color=color,
                s=20,
            )
            # add label at the end of the line
            ax.text(
                m.anytime_task_index[-1],
                m.anytime_accuracy_seen[-1] * 100,
                f"{m.anytime_accuracy_seen[-1] * 100:.1f}%",
                color=color,
                fontsize=8,
                verticalalignment="bottom",
            )

        if acc_online:
            ys = m.ttt.metrics_per_window()["accuracy"]
            ax.plot(
                m.ttt_windowed_task_index,
                ys,
                "-",
                color=color,
                label=f"{name} (online)",
                alpha=0.2,
            )

    ax.legend(
        loc="upper left",
        bbox_to_anchor=(1, 1),
        bbox_transform=ax.transAxes,
        fontsize=8,
        frameon=False,
    )
    ax.set_ylabel("Accuracy")
    ax.set_xlabel("Task")
    ax.set_xlim(0, len(next(iter(metrics.values())).task_index) * 1.1)

    return ax.get_figure(), ax


def ocl_plot(
    m: OCLMetrics,
    ax: Axes,
    task_acc: bool = True,
    online_acc: bool = False,
    acc_all: bool = False,
    acc_seen: bool = False,
):
    n_tasks = len(m.accuracy_matrix)
    cmap = plt.get_cmap("tab10")

    if task_acc:
        for task in range(n_tasks):
            color = cmap(task)
            ax.scatter(
                m.task_index, 100 * m.accuracy_matrix[:, task], color=color, s=20
            )
            ax.plot(
                m.anytime_task_index,
                100 * m.anytime_accuracy_matrix[:, task],
                color=color,
                label=f"Task {task}",
            )

    if acc_all:
        ax.plot(
            m.anytime_task_index,
            m.anytime_accuracy_all * 100,
            "--",
            color=cmap(n_tasks),
            label="Acc. (all)",
        )

    if acc_seen:
        ax.plot(
            m.anytime_task_index,
            m.anytime_accuracy_seen * 100,
            "--",
            color=cmap(n_tasks + 1),
            label="Acc. (seen)",
        )

    if online_acc:
        ys = m.ttt.metrics_per_window()["accuracy"]
        ax.plot(
            m.ttt_windowed_task_index,
            ys,
            "-",
            color=cmap(n_tasks + 2),
            label="Online Acc.",
        )

    # add legend lhs outside of the plot
    ax.legend(
        loc="upper left",
        bbox_to_anchor=(1, 1),
        bbox_transform=ax.transAxes,
        fontsize=8,
        frameon=False,
    )
    ax.set_ylabel("Accuracy")
    ax.set_xlabel("Task")
