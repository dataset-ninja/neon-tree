# https://zenodo.org/record/5914554#.Yj2n739Bzmh

import os
import xml.etree.ElementTree as ET

import cv2
import numpy as np
import supervisely as sly
import tifffile
from dotenv import load_dotenv
from PIL import Image
from supervisely.io.fs import (
    file_exists,
    get_file_ext,
    get_file_name,
    get_file_name_with_ext,
    get_file_size,
)

Image.MAX_IMAGE_PIXELS = None

# https://zenodo.org/record/5914554#.Yj2n739Bzmh

import os
import xml.etree.ElementTree as ET

import cv2
import numpy as np
import supervisely as sly
import tifffile
from dotenv import load_dotenv
from PIL import Image
from supervisely.io.fs import (
    file_exists,
    get_file_ext,
    get_file_name,
    get_file_name_with_ext,
    get_file_size,
)

Image.MAX_IMAGE_PIXELS = None

import os
import xml.etree.ElementTree as ET

import supervisely as sly
from supervisely.io.fs import (
    file_exists,
    get_file_ext,
    get_file_name,
    get_file_name_with_ext,
    get_file_size,
)


def convert_and_upload_supervisely_project(
    api: sly.Api, workspace_id: int, project_name: str
) -> sly.ProjectInfo:
    # project_name = "NeonTree"
    images_path = "/home/grokhi/rawdata/neon-tree-evaluation/training/RGB"
    eval_images_path = "/home/grokhi/rawdata/neon-tree-evaluation/evaluation/evaluation/RGB"
    bboxes_path = "/home/grokhi/rawdata/neon-tree-evaluation/annotations/annotations"
    image_ext = ".tif"
    bbox_ext = ".xml"
    batch_size = 5
    group_tag_name = "grid_id"

    def create_ann(image_path):
        labels = []
        tags = []

        image = Image.open(image_path)
        img_height = image.height
        img_wight = image.width

        image_name = get_file_name(image_path)
        if image_name.split("_")[0][0] == "2":
            site_id_value = image_name.split("_")[1]
            site_id = sly.Tag(site_id_meta, value=site_id_value)
            site_name_value = site_id_to_name[site_id_value]
            site_name = sly.Tag(site_name_meta, value=site_name_value)
            tags.append(site_name)
        elif image_name.split("_")[0] == "unnamed":
            site_id = sly.Tag(unnamed_meta)
        else:
            site_id_value = image_name.split("_")[0]
            site_id = sly.Tag(site_id_meta, value=site_id_value)
            site_name_value = site_id_to_name[site_id_value]
            site_name = sly.Tag(site_name_meta, value=site_name_value)
            tags.append(site_name)

            im_id_value = image_name[:-5]
            group_tag = sly.Tag(group_tag_meta, value=im_id_value)
            tags.append(group_tag)

        tags.append(site_id)

        ann_path = os.path.join(bboxes_path, image_name + ".xml")
        if file_exists(ann_path) is False:
            return sly.Annotation(img_size=(img_height, img_wight), img_tags=tags)

        tree = ET.parse(ann_path)
        root = tree.getroot()
        bndboxes = root.findall(".//bndbox")
        for bbox in bndboxes:
            top = int(bbox.find(".//ymin").text)
            left = int(bbox.find(".//xmin").text)
            bottom = int(bbox.find(".//ymax").text)
            right = int(bbox.find(".//xmax").text)

            rectangle = sly.Rectangle(top=top, left=left, bottom=bottom, right=right)
            label = sly.Label(rectangle, obj_class)
            labels.append(label)

        return sly.Annotation(img_size=(img_height, img_wight), labels=labels, img_tags=tags)

    obj_class = sly.ObjClass("tree", sly.Rectangle)
    site_id_meta = sly.TagMeta("site_id", sly.TagValueType.ANY_STRING)
    site_name_meta = sly.TagMeta("site_name", sly.TagValueType.ANY_STRING)
    unnamed_meta = sly.TagMeta("unnamed", sly.TagValueType.NONE)

    group_tag_meta = sly.TagMeta(group_tag_name, sly.TagValueType.ANY_STRING)

    site_id_to_name = {
        "ABBY": "Abby Road",
        "BART": "Barlett Experimental Forest",
        "BLAN": "Blandy Experimental Farm",
        "BONA": "Caribou-Poker Creeks Research Watershed",
        "CLBJ": "Lyndon B.Johnson National Grassland",
        "DEJU": "Delta Junction",
        "DELA": "Dead Lake",
        "DSNY": "Disney Wilderness Preserve",
        "GRSM": "Great Smoky Mountains National Park",
        "GUAN": "Guanica Forest",
        "HARV": "Harvard Forest",
        "HEAL": "Healy Neon",
        "JERC": "The Jones Center At Ichauway",
        "JORN": "Jornada Experimental Range Neon",
        "KONZ": "Konza Prairie Agroecosystem",
        "LAJA": "Lajas Experimental Station",
        "LENO": "Lenoir Landing",
        "MLBS": "Mountain Lake Biological Station",
        "MOAB": "Moab",
        "NIWO": "Niwot Ridge",
        "NOGP": "Northern Great Plains Research Laboratory",
        "OAES": "Marvin Klemme Range Research Station",
        "ONAQ": "Onaqui",
        "OSBS": "Ordway-Swisher Biological Station",
        "PUUM": "Puu Makaala Natural Area Reserve",
        "RMNP": "Rocky Mountaion",
        "TOOL": "Toolik Field Station",
        "SCBI": "Smithsonian Conservation Biology Institute",
        "SERC": "Smithsonian Environmental Research Center",
        "SJER": "San Joaquin Experimental Range",
        "SOAP": "Soaproot Saddle",
        "SRER": "Santa Rita Experimental Range",
        "STEI": "Steigerwaldt-Chequamegom",
        "TALL": "Talladega National Forest",
        "TEAK": "Lower Teakettle",
        "UKFS": "University of Kansas Field Station",
        "UNDE": "University of Notre Dame Environmental Research Center",
        "WREF": "Wind River Experimental Forest",
        "YELL": "Yellowstone National Park",
    }

    project = api.project.create(workspace_id, project_name, change_name_if_conflict=True)
    meta = sly.ProjectMeta(
        obj_classes=[obj_class],
        tag_metas=[site_id_meta, group_tag_meta, unnamed_meta, site_name_meta],
    )
    api.project.update_meta(project.id, meta.to_json())
    api.project.images_grouping(id=project.id, enable=True, tag_name=group_tag_name)

    ds_to_data_path = {"training": images_path, "evaluation": eval_images_path}

    for ds_name, images_path in ds_to_data_path.items():
        dataset = api.dataset.create(project.id, ds_name, change_name_if_conflict=True)

        images_names = [
            im_name for im_name in os.listdir(images_path) if get_file_ext(im_name) == image_ext
        ]

        progress = sly.Progress("Create dataset {}".format(ds_name), len(images_names))

        for img_names_batch in sly.batched(images_names, batch_size=batch_size):
            img_pathes_batch = [os.path.join(images_path, im_name) for im_name in img_names_batch]

            img_infos = api.image.upload_paths(dataset.id, img_names_batch, img_pathes_batch)
            img_ids = [im_info.id for im_info in img_infos]

            anns = [create_ann(image_path) for image_path in img_pathes_batch]
            api.annotation.upload_anns(img_ids, anns)

            progress.iters_done_report(len(img_names_batch))
    return project
