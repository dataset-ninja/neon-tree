Dataset **NeonTreeEvaluation: RGB** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/s/G/AC/JO00n3KfGKCFIfyWwdNczCRyM0rv7cNYuDEAID4QZfTVKi9UPYTPqMlq9PBRWykqI7kqAhEhIvHdGjLIg6iZYLrbHQC4QIO86aSNNVtLiVmBOX3Gac7Q6tTf7nRW.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='NeonTreeEvaluation: RGB', dst_dir='~/dataset-ninja/')
```
Make sure not to overlook the [python code example](https://developer.supervisely.com/getting-started/python-sdk-tutorials/iterate-over-a-local-project) available on the Supervisely Developer Portal. It will give you a clear idea of how to effortlessly work with the downloaded dataset.

The data in original format can be downloaded here:

- [annotations.zip](https://zenodo.org/record/5914554/files/annotations.zip?download=1)
- [evaluation.zip](https://zenodo.org/record/5914554/files/evaluation.zip?download=1)
- [training.zip](https://zenodo.org/record/5914554/files/training.zip?download=1)
