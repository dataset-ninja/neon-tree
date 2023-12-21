from typing import Dict, List, Optional, Union

from dataset_tools.templates import (
    AnnotationType,
    Category,
    CVTask,
    Domain,
    Industry,
    License,
    Research,
)

##################################
# * Before uploading to instance #
##################################
PROJECT_NAME: str = "NeonTreeEvaluation: RGB"
PROJECT_NAME_FULL: Optional[str] = "Data for the NeonTreeEvaluation Benchmark (RGB)"
HIDE_DATASET = False  # set False when 100% sure about repo quality

##################################
# * After uploading to instance ##
##################################
LICENSE: License = License.CC_BY_4_0()
APPLICATIONS: List[Union[Industry, Domain, Research]] = [Research.Ecological(), Domain.Forestry()]
CATEGORY: Category = Category.Environmental()

CV_TASKS: List[CVTask] = [CVTask.ObjectDetection()]
ANNOTATION_TYPES: List[AnnotationType] = [AnnotationType.ObjectDetection()]

RELEASE_DATE: Optional[str] = "2022-01-27"  # e.g. "YYYY-MM-DD"
if RELEASE_DATE is None:
    RELEASE_YEAR: int = None

HOMEPAGE_URL: str = "https://zenodo.org/record/5914554#.Yj2n739Bzmh"
# e.g. "https://some.com/dataset/homepage"

PREVIEW_IMAGE_ID: int = 11868945
# This should be filled AFTER uploading images to instance, just ID of any image.

GITHUB_URL: str = "https://github.com/dataset-ninja/neon-tree"
# URL to GitHub repo on dataset ninja (e.g. "https://github.com/dataset-ninja/some-dataset")

##################################
### * Optional after uploading ###
##################################
DOWNLOAD_ORIGINAL_URL: Optional[Union[str, dict]] = {
    "annotations.zip": "https://zenodo.org/record/5914554/files/annotations.zip?download=1",
    "evaluation.zip": "https://zenodo.org/record/5914554/files/evaluation.zip?download=1",
    "training.zip": "https://zenodo.org/record/5914554/files/training.zip?download=1",
}
# Optional link for downloading original dataset (e.g. "https://some.com/dataset/download")

CLASS2COLOR: Optional[Dict[str, List[str]]] = None
# If specific colors for classes are needed, fill this dict (e.g. {"class1": [255, 0, 0], "class2": [0, 255, 0]})

PAPER: Optional[str] = "https://www.biorxiv.org/content/10.1101/2020.11.16.385088v1"
BLOGPOST: Optional[Union[str, List[str], Dict[str, str]]] = None
REPOSITORY: Optional[Union[str, List[str], Dict[str, str]]] = {
    "GitHub": "https://github.com/weecology/NeonTreeEvaluation_package"
}

CITATION_URL: Optional[str] = "https://zenodo.org/record/5914554/export/hx"
AUTHORS: Optional[List[str]] = ["Ben Weinstein", "Sergio Marconi", "Ethan White"]
AUTHORS_CONTACTS: Optional[List[str]] = ["ben.weinstein@weecology.org"]

ORGANIZATION_NAME: Optional[Union[str, List[str]]] = "University of Florida"
ORGANIZATION_URL: Optional[Union[str, List[str]]] = "https://www.ufl.edu/"

SLYTAGSPLIT: Optional[Dict[str, List[str]]] = {
    "__PRETEXT__": "Additionally, the images has ***site_id*** and ***site_name***. The images in *evaluation* split are grouped by ***grid_id***. Also, 175 images are marked with ***unnamed*** tag"
}
TAGS: List[str] = None

##################################
###### ? Checks. Do not edit #####
##################################


def check_names():
    fields_before_upload = [PROJECT_NAME]  # PROJECT_NAME_FULL
    if any([field is None for field in fields_before_upload]):
        raise ValueError("Please fill all fields in settings.py before uploading to instance.")


def get_settings():
    if RELEASE_DATE is not None:
        global RELEASE_YEAR
        RELEASE_YEAR = int(RELEASE_DATE.split("-")[0])

    settings = {
        "project_name": PROJECT_NAME,
        "project_name_full": PROJECT_NAME_FULL or PROJECT_NAME,
        "hide_dataset": HIDE_DATASET,
        "license": LICENSE,
        "applications": APPLICATIONS,
        "category": CATEGORY,
        "cv_tasks": CV_TASKS,
        "annotation_types": ANNOTATION_TYPES,
        "release_year": RELEASE_YEAR,
        "homepage_url": HOMEPAGE_URL,
        "preview_image_id": PREVIEW_IMAGE_ID,
        "github_url": GITHUB_URL,
    }

    if any([field is None for field in settings.values()]):
        raise ValueError("Please fill all fields in settings.py after uploading to instance.")

    settings["release_date"] = RELEASE_DATE
    settings["download_original_url"] = DOWNLOAD_ORIGINAL_URL
    settings["class2color"] = CLASS2COLOR
    settings["paper"] = PAPER
    settings["repository"] = REPOSITORY
    settings["blog"] = BLOGPOST
    settings["citation_url"] = CITATION_URL
    settings["authors"] = AUTHORS
    settings["authors_contacts"] = AUTHORS_CONTACTS
    settings["organization_name"] = ORGANIZATION_NAME
    settings["organization_url"] = ORGANIZATION_URL
    settings["slytagsplit"] = SLYTAGSPLIT
    settings["tags"] = TAGS

    return settings
