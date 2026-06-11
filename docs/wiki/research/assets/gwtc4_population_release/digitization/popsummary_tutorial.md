---
doc_id: asset_gwtc4_pop_release_tutorial
title: "GWTC-4.0 popsummary Tutorial (converted)"
doc_type: reference
stage: reference
status: reference
evidence_role: reference
depends_on:
  - asset_gwtc4_pop_release_digitization_index
next_gate: targeted manual extraction before numerical reuse
last_updated: 2026-06-11
---

# GWTC-4.0 popsummary Tutorial (converted)

# `popsummary` Tutorial

`popsummary` is a tool for reading and writing standard data products from LIGO-Virgo-KAGRA rates and populations analyses. It also defines the standard data product format, which is based on h5 files.

In this notebook, we will see how to read in data from a popsummary file. We will use the file `BBHMassSpinRedshift_BrokenPowerLawTwoPeaks_GaussianComponentSpins_PowerLawRedshift.h5`, which is our default mass, spin, and redshift model belonging to the strongly modeled approach.

See [this notebook](https://git.ligo.org/christian.adamcewicz/popsummary/-/blob/32f6353882ae3b83d76ca0163fb1a4fa95bde70b/bin/tutorial.ipynb) for a more comprehensive overview of popsummary.

```python
# imports
from popsummary.popresult import PopulationResult
import numpy as np
import matplotlib.pyplot as plt
```

The `PopulationResult` class can be used to read results from existing `popsummary` output files.

```python
# load in result file
filename = "data_release/BBHMassSpinRedshift_BrokenPowerLawTwoPeaks_GaussianComponentSpins_PowerLawRedshift.h5"
result = PopulationResult(fname=filename)
```

### Metadata

We can retrieve metadata from our file using the `get_metadata` function.

```python
# retrieve events
events = result.get_metadata('events')
print(events)
```

```python
# retrieve event pe labels
sample_IDs = result.get_metadata('event_sample_IDs')
print(sample_IDs)
```

```python
# retrieve event-level parameters
event_parameters = result.get_metadata('event_parameters')
print(event_parameters)
```

```python
# retrieve  hyperparameter names
hyperparameters = result.get_metadata('hyperparameters')
print(hyperparameters)
```

### Hyperparameter samples

We can use the `get_hyperparameter_samples` function to retrieve hyperposterior samples.

```python
# get hyperposterior samples
hyperposterior_samples = result.get_hyperparameter_samples()
```

We can also use the `hyperparameters` argument to only return samples for particular hyper-parameters, as well as `hyper_sample_idx` to retrieve particular draws. Let's look at `alpha_1` and `alpha_2`, the slopes of the two power laws used in the model.

```python
# get alpha_1 and alpha_2 samples
alpha_1_alpha_2_hyperposterior_samples = result.get_hyperparameter_samples(hyperparameters=['alpha_1', 'alpha_2'])

# get first alpha_1 sample
first_alpha_1_sample = result.get_hyperparameter_samples(hyper_sample_idx=0,
                                                      hyperparameters=['alpha_1'])
```

### Reweighted event samples

Reweighted event samples are retrieved using `get_reweighted_event_samples`, the default group being `posterior`.

```python
# retrieve reweighted event_samples
reweighted_event_samples = result.get_reweighted_event_samples()
```

We can also retrieve truncated datasets, sorting by event using the event names listed in the metadata (`event`), draw (`draw_idx`), hyper sample (`hyper_sample_idx`), or parameter name as listed in the metadata (`parameters`).

```python
# get reweighted samples for only GW150914_095045
GW150914_event_samples = result.get_reweighted_event_samples(events='GW150914_095045')

# get reweighted samples for GW230805_034249 and GW231231_154016
GW170809_GW170823_event_samples = result.get_reweighted_event_samples(events=['GW230805_034249', 'GW231231_154016'])

# get reweighted first 100 event samples for first hyperparameter
truncated_first_hyperparam_event_samples = result.get_reweighted_event_samples(draw_idx=slice(0,100),
                                                                               hyper_sample_idx=0)

# get reweighted chi_eff samples
chi_eff_event_samples = result.get_reweighted_event_samples(parameters='chi_eff')
```

### Reweighted injections

Reweighted injections are retrieved with `get_reweighted_injections`, with the default group being `posterior`.

```python
# retrieve reweighted event_samples
reweighted_injections = result.get_reweighted_injections()
```

### Rates on grids

We can retrieve rates computed on grids as well as grid point positions using the `get_rates_on_grids` function. The default group is `posterior`. We can retrieve the desired dataset using the `grid_key`. We are also able to retrieve additional attributes if we so desire using `return_attributes`.

```python
# retreive rates on grids from output file
q_pos, q_rates = result.get_rates_on_grids('mass_ratio')
```

We can also retrieve rates from particular hyper samples using the `hyper_sample_idx` argument.

```python
# retreive rates on grids from first hyper sample
q_pos, q_rates_first_sample = result.get_rates_on_grids('mass_ratio', hyper_sample_idx=0)
```
