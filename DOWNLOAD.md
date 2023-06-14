Dataset **NeonTreeEvaluation** can be downloaded in Supervisely format:

 [Download](https://assets.supervise.ly/supervisely-supervisely-assets-public/teams_storage/E/s/pG/W9kTnvQMrpmSEKOROcADNqnqYEwHLXSp0EZoqe4ktGqMTwabwTw8bVc14y3Afs1mUQK1zeLleT39XZDrrSxmSXBK0RAj8sCRIiiR04UHvVUmd50O8z7APaXlMonp.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='NeonTreeEvaluation', dst_path='~/dtools/datasets/NeonTreeEvaluation.tar')
```
The data in original format can be downloaded here:

- 🔗[annotations](https://zenodo.org/record/5914554/files/annotations.zip?download=1)
- 🔗[evaluation](https://zenodo.org/record/5914554/files/evaluation.zip?download=1)
- 🔗[training](https://zenodo.org/record/5914554/files/training.zip?download=1)
