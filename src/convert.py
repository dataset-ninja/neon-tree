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
    ds_name = "ds"
    image_ext = ".tif"
    # bbox_ext = ".xml"
    batch_size = 30

    def create_ann(image_path):
        labels = []

        image_np = sly.imaging.image.read(image_path)[:, :, 0]
        img_height = image_np.shape[0]
        img_wight = image_np.shape[1]

        ann_path = os.path.join(bboxes_path, get_file_name(image_path) + ".xml")
        if file_exists(ann_path) is False:
            return sly.Annotation(img_size=(image_np.shape[0], image_np.shape[1]))

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

        return sly.Annotation(img_size=(img_height, img_wight), labels=labels)

    obj_class = sly.ObjClass("tree", sly.Rectangle)

    project = api.project.create(workspace_id, project_name, change_name_if_conflict=True)
    meta = sly.ProjectMeta(obj_classes=[obj_class])
    api.project.update_meta(project.id, meta.to_json())

    images_path = "/home/alex/DATASETS/TODO/NeonTree/training/RGB"
    eval_images_path = "/home/alex/DATASETS/TODO/NeonTree/evaluation/evaluation/RGB"
    bboxes_path = "/home/alex/DATASETS/TODO/NeonTree/annotations/annotations"

    images_pathes = []
    for image_name in os.listdir(images_path):
        image_path = os.path.join(images_path, image_name)
        if get_file_size(image_path) < 10000000:  # cv2 can`t read files more 10Mb`
            images_pathes.append(image_path)

    eval_images_pathes = []
    for image_name in os.listdir(eval_images_path):
        if get_file_ext(image_name) == image_ext:
            eval_images_pathes.append(os.path.join(eval_images_path, image_name))

    all_images_pathes = images_pathes + eval_images_pathes

    dataset = api.dataset.create(project.id, ds_name, change_name_if_conflict=True)

    progress = sly.Progress("Create dataset {}".format(ds_name), len(all_images_pathes))

    for img_pathes_batch in sly.batched(all_images_pathes, batch_size=batch_size):
        img_names_batch = [get_file_name_with_ext(im_path) for im_path in img_pathes_batch]

        img_infos = api.image.upload_paths(dataset.id, img_names_batch, img_pathes_batch)
        img_ids = [im_info.id for im_info in img_infos]

        anns = [create_ann(image_path) for image_path in img_pathes_batch]
        api.annotation.upload_anns(img_ids, anns)

        progress.iters_done_report(len(img_names_batch))

    return project
