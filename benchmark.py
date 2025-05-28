from time import perf_counter

from capymoa.classifier import HoeffdingTree
from capymoa.ocl.ann import WNPerceptron
from capymoa.ocl.datasets import SplitMNIST
from capymoa.ocl.evaluation import ocl_train_eval_loop
from torch.optim import Adam

scenario = SplitMNIST(preload_test=True)
model = WNPerceptron(scenario.schema)
optimizer = Adam(model.parameters(), 0.001)
learner = HoeffdingTree(scenario.schema)

# train_streams = [DataLoader(ds, batch_size=256, shuffle=True) for ds in scenario.train_tasks]
# test_streams = [DataLoader(ds, batch_size=256, shuffle=False) for ds in scenario.test_tasks]

start = perf_counter()
results = ocl_train_eval_loop(
    learner,
    scenario.train_loaders(256),
    scenario.test_loaders(256),
    continual_evaluations=1,
    progress_bar=True,
)
end = perf_counter()
print(f"Training and evaluation took {end - start:.2f} seconds.")
print(results.accuracy_all_avg)

# fig, ax = plt.subplots(layout="constrained")
# ocl_plot(results, ax, True, True, True, True)
# fig.savefig("figure.png")
