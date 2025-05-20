from matplotlib import pyplot as plt
from matplotlib.axes import Axes
from capymoa.ocl.evaluation import OCLMetrics


def plot_metrics(
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
